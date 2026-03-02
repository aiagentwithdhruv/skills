# Nano Banana 2 - Master JSON Prompt Reference Guide

This guide defines the ultimate JSON schema for prompting the Nano Banana 2 (Gemini 3.1 Flash) AI image generation model. Using this structured format ensures high consistency, detailed control, and takes advantage of the model's precise instruction-following capabilities.

## The JSON Schema

```json
{
  "prompt": "string - A dense, ultra-descriptive narrative merging subject, outfit, environment, and camera details. Use highly specific, unflattering language to force realism. (e.g., 'Ultra-realistic close-up mirror selfie... Natural male skin texture with visible pores, mild redness, subtle freckles, light acne marks. No makeup, no grooming enhancement. Direct on-camera flash creating sharp highlights. 85mm lens, f/1.8, ISO 200. Documentary realism. Do not beautify or alter facial features.')",
  
  "negative_prompt": "string - Comma-separated list of blockers (e.g., 'blurry, low resolution, distorted face, extra fingers, overexposed, heavy makeup, unrealistic skin, cartoon, CGI, oversaturated colors, anatomy normalization, datasets-average body')",
  
  "settings": {
    "resolution": "string - e.g., '1024x1792', '4k'",
    "style": "string - e.g., 'photorealistic, documentary realism', 'candid amateur', 'fashion photography, flash photography'",
    "lighting": "string - e.g., 'natural golden hour', 'harsh overhead fluorescent', 'direct on-camera flash, high contrast'",
    "camera_angle": "string - e.g., 'high-angle arm-extended selfie', 'side profile view'",
    "depth_of_field": "string - e.g., 'shallow depth of field', 'deep, infinite focus'",
    "quality": "string - e.g., 'high detail, unretouched skin', 'visible film grain, slightly soft'"
  }
}
```

## How to Use This Dual Paradigm

You now have two core ways to construct a prompt:

1.  **The Dense Narrative (Classic V4 Paradigm):** Use the dense text-based `prompt` string when feeding a standard model/API. **Language Masterclass:** Use explicit camera mathematics (`85mm lens, f/2.0, ISO 200`), explicitly call for imperfections (`mild redness, light acne marks`), describe lighting behavior (`creating sharp highlights on skin`), and include direct negative commands *within* the positive prompt (`Do not beautify or alter facial features`, `unretouched skin`).
2.  **The Deep Grid (V3 Paradigm):** If you need absolute 2x2 grid control or explicit JSON constraints to break the model's structure down, map it out using the complex JSON objects (subject, lighting, camera).

When sending data to the **Kie.ai API**, compile your choices into a single JSON object (using the Dense Narrative structure above) and pass it as a stringified payload into the `input.prompt` field!
{
  "task": "string - High-level goal (e.g., 'sports_selfie_collage', 'single_macro_portrait')",
  
  "output": {
    "type": "string - e.g., 'single_image', '4-panel_collage'",
    "layout": "string - e.g., '1x1', '2x2_grid', 'side-by-side'",
    "aspect_ratio": "string - e.g., '3:4', '16:9', '4:5'",
    "resolution": "string - e.g., 'ultra_high', 'medium_low'",
    "camera_style": "string - e.g., 'smartphone_front_camera', 'professional_dslr'"
  },

  "image_quality_simulation": {
    "sharpness": "string - e.g., 'tack_sharp', 'slightly_soft_edges'",
    "noise": "string - e.g., 'unfiltered_sensor_grain', 'visible_film_grain', 'clean_digital'",
    "compression_artifacts": "boolean - true if attempting to simulate uploaded UGC",
    "dynamic_range": "string - e.g., 'limited', 'hdr_capable'",
    "white_balance": "string - e.g., 'slightly_warm', 'cool_fluorescent'",
    "lens_imperfections": [
      "array of strings - e.g., 'subtle chromatic aberration', 'minor lens distortion', 'vignetting'"
    ]
  },

  "subject": {
    "identity": "string - Specific identity or consistency tags.",
    "appearance": {
      "gender_or_type": "string",
      "age_or_condition": "string",
      "ethnicity_or_origin": "string",
      "skin_texture": "string - Highly specific, e.g., 'realistic, visible pores, natural imperfections'",
      "hair": "string - e.g., 'natural blonde, tied back in sporty ponytail'",
      "makeup": "string - e.g., 'minimal, natural, slightly flushed from activity'",
      "expression": "string - e.g., 'casual confident smile, candid selfie energy'"
    },
    "outfit": {
      "type": "string - e.g., 'sporty', 'casual streetwear'",
      "top": "string - e.g., 'athletic sports bra'",
      "bottom": "string - e.g., 'high-waisted leggings'",
      "colors": "string - e.g., 'neutral or soft sporty tones'"
    }
  },

  "multi_panel_layout": {
    "grid_panels": [
      {
        "panel": "string - e.g., 'top_left', 'full_frame' (if not a grid)",
        "pose": "string - e.g., 'slight upward selfie angle, relaxed smile'",
        "action": "string - e.g., 'holding phone with one hand, casual posture'"
      }
    ]
  },

  "environment": {
    "location": "string - e.g., 'gym or outdoor sports area'",
    "background": "string - What is behind the subject (e.g., 'blurred gym equipment')",
    "lighting": {
      "type": "string - e.g., 'natural or overhead gym lighting', 'harsh direct sunlight'",
      "quality": "string - e.g., 'uneven, realistic, non-studio', 'high-contrast dramatic'"
    }
  },

  "embedded_text_and_overlays": {
    "text": "string (optional)",
    "location": "string (optional)"
  },

  "structural_preservation": {
    "preservation_rules": [
      "array of strings - e.g., 'Exact physical proportions must be preserved'"
    ]
  },

  "controlnet": {
    "pose_control": {
      "model_type": "string - e.g., 'DWPose'",
      "purpose": "string",
      "constraints": ["array of strings"],
      "recommended_weight": "number"
    },
    "depth_control": {
      "model_type": "string - e.g., 'ZoeDepth'",
      "purpose": "string",
      "constraints": ["array of strings"],
      "recommended_weight": "number"
    }
  },

  "explicit_restrictions": {
    "no_professional_retouching": "boolean - typically true for realism",
    "no_studio_lighting": "boolean - typically true for candid shots",
    "no_ai_beauty_filters": "boolean - mandatory true to avoid plastic look",
    "no_high_end_camera_look": "boolean - true if simulating smartphones"
  },

  "negative_prompt": {
    "forbidden_elements": [
      "array of strings - Massive list of 'AI style' blockers required for extreme realism. Example stack: 'anatomy normalization', 'body proportion averaging', 'dataset-average female anatomy', 'wide-angle distortion not in reference', 'lens compression not in reference', 'cropping that removes volume', 'depth flattening', 'mirror selfies', 'reflections', 'beautification filters', 'skin smoothing', 'plastic skin', 'airbrushed texture', 'stylized realism', 'editorial fashion proportions'."
    ]
  }
}
```

## How to Use This Template

This reference guide is designed to produce **hyper-realistic, consistently structured images**. When generating prompts for Nano Banana 2:

1. **Be Granular, Not Vague:** Do not just say "a woman." Use the `character_or_object_details` block to define exactly how the skin reflects light, the specific clothing material, and micro-textures like pores or weathering.
2. **Lock the Camera and Light:** Real photography relies on physics. Always define the `lens` (e.g., "90mm macro"), the `camera.height`, and the exact `lighting.direction`.
3. **Use the `structural_preservation` Block:** If you are trying to maintain exact body types, physical laws, or character consistency, use this block to explicitly tell the model *not* to average out the data.
4. **Heavily Populate the `negative_prompt`:** To combat "AI look," you must explicitly forbid "plastic skin," "smoothing," "beautification filters," and "anatomy normalization."
5. **Drop Unused Fields:** If you are generating a landscape, omit the `pose_and_action` block entirely. The JSON should only contain blocks relevant to the scene.

## Best Practices for Nano Banana 2 Prompting

1.  **Leverage Character Consistency:** Use the `character_consistency_tags` to define specific traits you want to persist if we are generating multiple shots of the same subject.
2.  **Exploit Text Accuracy:** Nano Banana 2 is exceptionally good at text rendering. If you want neon signs, graffiti, or labels, explicitly state the exact string in `text_elements`.
3.  **High-Fidelity Textures:** The model excels at photorealism and textures. Be specific in `style_and_rendering` (e.g., "visible film grain", "hyper-detailed skin pores").
4.  **Keep it Focused:** While JSON allows for massive detail, start with the core elements (Subject, Lighting, Style) before overly complicating the scene.
5.  **Use Iteration:** We will use this schema to generate an initial image, review, and then simply tweak one or two JSON values (like `lighting_style` or `camera_angle`) for the next generation.
