# Nano Banana 2 - Gemini Project Organizer

This document tracks our progress, generated assets, and custom scripts for the Nano Banana 2 image generation project using Anti-Gravity and Gemini 3.1 Pro.

## Project Structure

It is critical to **always keep prompts and images organized** within the project directory.

- `/images/` - All generated images must be saved here. Keep them organized by category if necessary.
- `/prompts/` - Saved JSON prompt configurations corresponding to the generated images must be stored here.
- `/scripts/` - Utility scripts for batch processing, API interaction, or prompt generation.
- `master_prompt_reference.md` - The compiled JSON schema and guide (To be created).

## Image Generation Workflow

Whenever the user requests to generate an image, you must use the **Nano Banana image generation skill**. 

1. Use the skill to generate the image based on the user's requirements.
2. Save the resulting image to the correctly categorized subfolder inside the `/images/` directory (e.g., `/images/infographics/`). **If a specific category cannot be determined, save it to `/images/miscellaneous/`.** This is mandatory for every single generation.
3. Save the corresponding prompt configuration to the `/prompts/` directory, mirroring the exact same subfolder used for the image (e.g., `/prompts/infographics/` or `/prompts/miscellaneous/`).
4. **Parallel Processing:** When you are processing multiple images at the same time, you MUST run their generation commands in parallel to save time.

## Current Phase: Schema Validation

**Goal:** Generate complex test images using the newly designed JSON schema to validate its effectiveness. Ensure that any output generated is properly filed according to the project structure.

## Scripts Log

| Script Name | Purpose | Status |
|-------------|---------|--------|
| `generate_kie.py` | Python script to hit Kie.ai API, poll, and download image safely | Active |
