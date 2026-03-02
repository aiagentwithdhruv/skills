#!/usr/bin/env python3
"""
YouTube Clip: Download YouTube videos and extract intelligent clips.

Uses yt-dlp for downloading, faster-whisper for transcription,
and Claude for intelligent chapter/clip identification.

Usage:
    # Download full video
    python3 youtube_clip.py "https://youtube.com/watch?v=..." --download-only

    # Download + auto-clip into chapters
    python3 youtube_clip.py "https://youtube.com/watch?v=..." --output-dir clips/

    # Extract specific time range
    python3 youtube_clip.py "https://youtube.com/watch?v=..." --start 60 --end 180 -o clip.mp4

    # Auto-detect best clips (AI-powered)
    python3 youtube_clip.py "https://youtube.com/watch?v=..." --auto-clip --max-clips 5

Dependencies:
    pip install yt-dlp faster-whisper anthropic
    brew install ffmpeg  # macOS
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path


def download_video(
    url: str,
    output_dir: str,
    max_quality: str = "1080",
    audio_only: bool = False,
) -> str:
    """Download YouTube video using yt-dlp. Returns path to downloaded file."""
    os.makedirs(output_dir, exist_ok=True)

    output_template = os.path.join(output_dir, "%(title)s.%(ext)s")

    cmd = ["yt-dlp"]

    if audio_only:
        cmd.extend(["-x", "--audio-format", "mp3"])
    else:
        cmd.extend([
            "-f", f"bestvideo[height<={max_quality}]+bestaudio/best[height<={max_quality}]",
            "--merge-output-format", "mp4",
        ])

    cmd.extend([
        "-o", output_template,
        "--no-playlist",
        "--write-subs",
        "--sub-langs", "en",
        "--write-auto-subs",
        url
    ])

    print(f"Downloading: {url}")
    print(f"Max quality: {max_quality}p")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Download error: {result.stderr[:500]}")
        return ""

    # Find the downloaded file
    for line in result.stdout.split("\n"):
        if "Destination:" in line or "has already been downloaded" in line:
            match = re.search(r'(?:Destination:|downloaded)\s*(.+?)(?:\s*$)', line)
            if match:
                path = match.group(1).strip()
                if os.path.exists(path):
                    return path

    # Fallback: find most recent mp4 in output dir
    mp4s = sorted(Path(output_dir).glob("*.mp4"), key=os.path.getmtime, reverse=True)
    if mp4s:
        return str(mp4s[0])

    mp3s = sorted(Path(output_dir).glob("*.mp3"), key=os.path.getmtime, reverse=True)
    if mp3s:
        return str(mp3s[0])

    print("Could not find downloaded file")
    return ""


def get_video_info(path: str) -> dict:
    """Get video duration and resolution."""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-show_entries", "stream=width,height",
        "-of", "json", path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(result.stdout)
    stream = data.get("streams", [{}])[0]
    fmt = data.get("format", {})
    return {
        "width": int(stream.get("width", 0)),
        "height": int(stream.get("height", 0)),
        "duration": float(fmt.get("duration", 0)),
    }


def get_youtube_chapters(url: str) -> list[dict]:
    """Extract YouTube chapters if available."""
    cmd = ["yt-dlp", "--dump-json", "--no-download", url]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        return []

    data = json.loads(result.stdout)
    chapters = data.get("chapters", [])

    if chapters:
        print(f"Found {len(chapters)} YouTube chapters")
        return [
            {
                "title": ch.get("title", f"Chapter {i+1}"),
                "start": ch["start_time"],
                "end": ch["end_time"],
            }
            for i, ch in enumerate(chapters)
        ]

    return []


def transcribe_for_chapters(video_path: str, model_size: str = "base") -> list[dict]:
    """Transcribe video and return timestamped text chunks."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("faster-whisper not installed. Install: pip install faster-whisper")
        return []

    print(f"Transcribing with Whisper ({model_size})...")
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(video_path, word_timestamps=False)

    chunks = []
    for seg in segments:
        chunks.append({
            "start": seg.start,
            "end": seg.end,
            "text": seg.text.strip(),
        })

    print(f"Transcribed {len(chunks)} segments")
    return chunks


def ai_generate_chapters(chunks: list[dict], duration: float) -> list[dict]:
    """Use Claude to identify natural chapter breaks from transcript."""
    try:
        import anthropic
    except ImportError:
        print("anthropic not installed. Install: pip install anthropic")
        return []

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("ANTHROPIC_API_KEY not set")
        return []

    # Build transcript with timestamps
    transcript = "\n".join(
        f"[{c['start']:.0f}s-{c['end']:.0f}s] {c['text']}"
        for c in chunks
    )

    # Truncate if too long
    if len(transcript) > 15000:
        transcript = transcript[:15000] + "\n... [truncated]"

    prompt = f"""Analyze this video transcript and identify natural chapter/topic breaks.
Create 5-15 chapters with meaningful titles.

TRANSCRIPT:
{transcript}

VIDEO DURATION: {duration:.0f} seconds ({duration/60:.1f} minutes)

Rules:
- First chapter MUST start at 0
- Chapters should be 1-5 minutes each
- Titles should be concise (2-6 words)
- Identify topic transitions, not arbitrary time splits

Return JSON array only:
[{{"title": "Introduction", "start": 0, "end": 120}}, ...]"""

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text.strip()

    # Parse JSON from response
    json_match = re.search(r'\[[\s\S]*\]', text)
    if not json_match:
        print("Failed to parse AI chapter response")
        return []

    try:
        chapters = json.loads(json_match.group())
        print(f"AI generated {len(chapters)} chapters")
        return chapters
    except json.JSONDecodeError:
        print("Invalid JSON in AI response")
        return []


def extract_clip(
    input_path: str,
    output_path: str,
    start: float,
    end: float,
    reencode: bool = False,
) -> bool:
    """Extract a clip from video using FFmpeg."""
    duration = end - start

    cmd = ["ffmpeg", "-y", "-ss", str(start), "-i", input_path, "-t", str(duration)]

    if reencode:
        cmd.extend(["-c:v", "libx264", "-preset", "fast", "-crf", "18", "-c:a", "aac", "-b:a", "192k"])
    else:
        cmd.extend(["-c", "copy", "-avoid_negative_ts", "make_zero"])

    cmd.extend(["-movflags", "+faststart", "-loglevel", "error", output_path])

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0


def sanitize_filename(name: str) -> str:
    """Remove/replace characters that are invalid in filenames."""
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', '_', name)
    return name[:80]


def main():
    parser = argparse.ArgumentParser(description="Download YouTube videos and extract clips")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-o", "--output", type=str, default=None,
                        help="Output file path (for single clip extraction)")
    parser.add_argument("--output-dir", type=str, default=".tmp/clips",
                        help="Output directory for clips (default: .tmp/clips)")
    parser.add_argument("--download-only", action="store_true",
                        help="Only download, don't clip")
    parser.add_argument("--max-quality", type=str, default="1080",
                        choices=["480", "720", "1080", "1440", "2160"],
                        help="Max video quality (default: 1080)")
    parser.add_argument("--audio-only", action="store_true",
                        help="Download audio only (MP3)")
    parser.add_argument("--start", type=float, default=None,
                        help="Clip start time in seconds")
    parser.add_argument("--end", type=float, default=None,
                        help="Clip end time in seconds")
    parser.add_argument("--auto-clip", action="store_true",
                        help="Auto-generate clips using AI chapter detection")
    parser.add_argument("--use-yt-chapters", action="store_true", default=True,
                        help="Use YouTube chapters if available (default: True)")
    parser.add_argument("--max-clips", type=int, default=None,
                        help="Max number of clips to extract")
    parser.add_argument("--whisper-model", type=str, default="base",
                        help="Whisper model for transcription (default: base)")
    parser.add_argument("--reencode", action="store_true",
                        help="Re-encode clips (slower but more precise cuts)")

    args = parser.parse_args()

    start_time = time.time()

    # Step 1: Download
    video_path = download_video(
        args.url,
        output_dir=args.output_dir,
        max_quality=args.max_quality,
        audio_only=args.audio_only,
    )

    if not video_path:
        print("Download failed!")
        sys.exit(1)

    file_size = os.path.getsize(video_path) / (1024 * 1024)
    print(f"Downloaded: {video_path} ({file_size:.1f} MB)")

    if args.download_only:
        print("Done (download only)")
        return

    info = get_video_info(video_path)
    print(f"Video: {info['width']}x{info['height']}, {info['duration']:.1f}s")

    # Step 2: Extract specific range
    if args.start is not None:
        end = args.end or info["duration"]
        output = args.output or os.path.join(args.output_dir, "clip.mp4")

        print(f"Extracting: {args.start:.1f}s - {end:.1f}s")
        success = extract_clip(video_path, output, args.start, end, reencode=args.reencode)

        if success:
            clip_size = os.path.getsize(output) / (1024 * 1024)
            print(f"Clip saved: {output} ({clip_size:.1f} MB)")
        else:
            print("Clip extraction failed!")
        return

    # Step 3: Auto-clip mode
    if args.auto_clip:
        chapters = []

        # Try YouTube chapters first
        if args.use_yt_chapters:
            chapters = get_youtube_chapters(args.url)

        # Fall back to AI-generated chapters
        if not chapters:
            print("No YouTube chapters found, using AI analysis...")
            chunks = transcribe_for_chapters(video_path, model_size=args.whisper_model)
            if chunks:
                chapters = ai_generate_chapters(chunks, info["duration"])

        if not chapters:
            print("Could not generate chapters. Try --start/--end for manual clipping.")
            return

        # Limit clips
        if args.max_clips:
            chapters = chapters[:args.max_clips]

        # Extract each chapter
        clips_dir = os.path.join(args.output_dir, "chapters")
        os.makedirs(clips_dir, exist_ok=True)

        print(f"\nExtracting {len(chapters)} clips:")
        for i, ch in enumerate(chapters):
            title = ch.get("title", f"clip_{i+1}")
            safe_title = sanitize_filename(title)
            clip_path = os.path.join(clips_dir, f"{i+1:02d}_{safe_title}.mp4")

            start = ch["start"]
            end = ch["end"]
            duration = end - start

            print(f"  {i+1}. [{start:.0f}s-{end:.0f}s] ({duration:.0f}s) {title}")

            success = extract_clip(video_path, clip_path, start, end, reencode=args.reencode)
            if not success:
                print(f"     Failed!")

        elapsed = time.time() - start_time
        print(f"\nDone! {len(chapters)} clips extracted in {elapsed:.1f}s")
        print(f"Clips at: {clips_dir}")
        return

    print("No action specified. Use --download-only, --start/--end, or --auto-clip")


if __name__ == "__main__":
    main()
