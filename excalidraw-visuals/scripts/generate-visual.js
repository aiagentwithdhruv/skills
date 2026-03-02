/**
 * Generate an Excalidraw-style visual using fal.ai (Flux Schnell / Nano Banana Pro)
 * Replaces kie.ai — faster, free tier, better quality.
 *
 * Usage:
 *   node generate-visual.js "<prompt>" <output-file.png> [aspect-ratio] [--input <image> ...]
 *
 * Aspect ratios: 16:9 (default), 1:1, 4:5
 * --input: one or more reference images (URLs only — fal.ai uses image URLs)
 * Requires FAL_KEY in .env file at project root
 */

const fs = require('fs');
const path = require('path');
const https = require('https');
const http = require('http');

const PROJECT_ROOT = path.resolve(__dirname, '../..');

// Load .env
for (const envDir of [PROJECT_ROOT, path.resolve(PROJECT_ROOT, '..'), process.cwd()]) {
  const envPath = path.join(envDir, '.env');
  if (fs.existsSync(envPath)) {
    const envContent = fs.readFileSync(envPath, 'utf-8');
    for (const line of envContent.split('\n')) {
      const trimmed = line.trim();
      if (trimmed && !trimmed.startsWith('#')) {
        const eqIndex = trimmed.indexOf('=');
        if (eqIndex > 0) {
          const key = trimmed.slice(0, eqIndex).trim();
          const value = trimmed.slice(eqIndex + 1).trim().replace(/^["']|["']$/g, '');
          if (!process.env[key]) process.env[key] = value;
        }
      }
    }
    break;
  }
}

const API_KEY = process.env.FAL_KEY;
if (!API_KEY) {
  console.error('Error: FAL_KEY not set. Add it to .env file.');
  console.error('Get your key at: https://fal.ai/dashboard/keys');
  process.exit(1);
}

// Parse arguments
const args = process.argv.slice(2);
const PROMPT = args[0];
const OUTPUT_FILE = args[1];

if (!PROMPT || !OUTPUT_FILE) {
  console.error('Usage: node generate-visual.js "<prompt>" <output-file.png> [aspect-ratio] [--input <image-url> ...]');
  process.exit(1);
}

// Parse aspect ratio and --input flag
let ASPECT_RATIO = '16:9';
const inputImages = [];

for (let i = 2; i < args.length; i++) {
  if (args[i] === '--input' && args[i + 1]) {
    i++;
    while (i < args.length && !args[i].startsWith('--')) {
      inputImages.push(args[i]);
      i++;
    }
    i--;
  } else if (!args[i].startsWith('--')) {
    ASPECT_RATIO = args[i];
  }
}

// Map aspect ratios to fal.ai format
const RATIO_MAP = {
  '16:9': 'landscape_16_9',
  '1:1': 'square_hd',
  '4:5': 'portrait_4_3',
  '4:3': 'landscape_4_3',
  '9:16': 'portrait_16_9',
};

const falSize = RATIO_MAP[ASPECT_RATIO] || 'landscape_16_9';

function httpsRequest(url, options, body) {
  return new Promise((resolve, reject) => {
    const client = url.startsWith('https') ? https : http;
    const req = client.request(url, options, (res) => {
      // Handle redirects
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        httpsRequest(res.headers.location, { ...options, method: 'GET' })
          .then(resolve)
          .catch(reject);
        return;
      }

      const chunks = [];
      res.on('data', (chunk) => chunks.push(chunk));
      res.on('end', () => {
        const buffer = Buffer.concat(chunks);
        if (options.binary) {
          resolve(buffer);
        } else {
          resolve(buffer.toString('utf-8'));
        }
      });
    });
    req.on('error', reject);
    if (body) req.write(body);
    req.end();
  });
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function downloadImage(url) {
  return httpsRequest(url, { method: 'GET', binary: true });
}

async function main() {
  console.log(`Generating Excalidraw visual via fal.ai (${falSize})...`);
  console.log(`Prompt length: ${PROMPT.length} chars`);
  if (inputImages.length > 0) {
    console.log(`Reference images: ${inputImages.length}`);
  }

  const model = 'fal-ai/nano-banana-2';
  const submitUrl = `https://queue.fal.run/${model}`;

  const payload = {
    prompt: PROMPT,
    image_size: falSize,
    num_images: 1,
    enable_safety_checker: false,
  };

  // Add image URL if provided (for image-to-image)
  if (inputImages.length > 0) {
    payload.image_url = inputImages[0];
  }

  const submitBody = JSON.stringify(payload);

  console.log('Submitting to fal.ai queue...');
  const submitResponse = await httpsRequest(submitUrl, {
    method: 'POST',
    headers: {
      'Authorization': `Key ${API_KEY}`,
      'Content-Type': 'application/json',
    },
  }, submitBody);

  const submitData = JSON.parse(submitResponse);

  // Check if result is immediate
  if (submitData.images && submitData.images.length > 0) {
    const imageUrl = submitData.images[0].url;
    console.log('Got immediate result. Downloading...');
    const imageBuffer = await downloadImage(imageUrl);
    const outputDir = path.dirname(OUTPUT_FILE);
    if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });
    fs.writeFileSync(OUTPUT_FILE, imageBuffer);
    console.log(`Saved to: ${OUTPUT_FILE}`);
    process.exit(0);
  }

  // Queue-based: poll for result
  const requestId = submitData.request_id;
  if (!requestId) {
    console.error('Error: No request_id or immediate result. Response:');
    console.error(submitResponse);
    process.exit(1);
  }

  console.log(`Request ID: ${requestId}`);
  console.log('Polling for result...');

  const statusUrl = `https://queue.fal.run/${model}/requests/${requestId}/status`;
  const resultUrl = `https://queue.fal.run/${model}/requests/${requestId}`;

  for (let i = 1; i <= 60; i++) {
    await sleep(2000);

    let statusData;
    try {
      const statusResponse = await httpsRequest(statusUrl, {
        method: 'GET',
        headers: { 'Authorization': `Key ${API_KEY}` },
      });
      statusData = JSON.parse(statusResponse);
    } catch (e) {
      console.log(`  Poll ${i}: connection error, retrying...`);
      continue;
    }

    const state = statusData.status || 'unknown';

    if (state === 'COMPLETED') {
      const resultResponse = await httpsRequest(resultUrl, {
        method: 'GET',
        headers: { 'Authorization': `Key ${API_KEY}` },
      });
      const resultData = JSON.parse(resultResponse);

      if (resultData.images && resultData.images.length > 0) {
        const imageUrl = resultData.images[0].url;
        console.log('Downloading image...');
        const imageBuffer = await downloadImage(imageUrl);
        const outputDir = path.dirname(OUTPUT_FILE);
        if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });
        fs.writeFileSync(OUTPUT_FILE, imageBuffer);
        console.log(`Saved to: ${OUTPUT_FILE}`);
        process.exit(0);
      }

      console.error('Error: No images in completed result.');
      process.exit(1);
    } else if (state === 'FAILED' || state === 'ERROR') {
      console.error('Error: Image generation failed.');
      console.error(JSON.stringify(statusData, null, 2));
      process.exit(1);
    }

    console.log(`  Status: ${state} (attempt ${i}/60)`);
  }

  console.error('Error: Timed out waiting for image generation.');
  process.exit(1);
}

main().catch((err) => {
  console.error('Error:', err);
  process.exit(1);
});
