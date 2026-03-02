#!/usr/bin/env python3
"""
Auto-Captions: Generate and burn styled subtitles into video.

Uses faster-whisper for transcription and FFmpeg for subtitle burning.
Supports word-level highlighting, custom fonts, colors, and positions.

Usage:
    # Basic - generate and burn captions
    python3 auto_captions.py input.mp4 output.mp4

    # SRT only (no burn)
    python3 auto_captions.py input.mp4 --srt-only

    # Custom style
    python3 auto_captions.py input.mp4 output.mp4 --font-size 28 --font-color yellow --position bottom

    # Word-level captions (1-3 words at a time, like CapCut/Submagic)
    python3 auto_captions.py input.mp4 output.mp4 --word-level --max-words 2

Dependencies:
    pip install faster-whisper
    brew install ffmpeg  # macOS
"""

import argparse
import os
import re
import subprocess
import tempfile
import time
from pathlib import Path


def get_video_info(input_path: str) -> dict:
    """Get video resolution and duration."""
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height",
        "-show_entries", "format=duration",
        "-of", "json", input_path
    ]
    import json
    result = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(result.stdout)
    stream = data.get("streams", [{}])[0]
    fmt = data.get("format", {})
    return {
        "width": int(stream.get("width", 1920)),
        "height": int(stream.get("height", 1080)),
        "duration": float(fmt.get("duration", 0)),
    }


def transcribe(input_path: str, model_size: str = "base", language: str = None) -> list[dict]:
    """
    Transcribe video using faster-whisper.
    Returns list of segments with word-level timestamps.
    """
    from faster_whisper import WhisperModel

    print(f"Loading Whisper model ({model_size})...")
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    print("Transcribing...")
    start_time = time.time()

    kwargs = {"word_timestamps": True}
    if language:
        kwargs["language"] = language

    segments_gen, info = model.transcribe(input_path, **kwargs)

    segments = []
    for seg in segments_gen:
        segment_data = {
            "start": seg.start,
            "end": seg.end,
            "text": seg.text.strip(),
            "words": [],
        }
        if seg.words:
            for w in seg.words:
                segment_data["words"].append({
                    "word": w.word.strip(),
                    "start": w.start,
                    "end": w.end,
                })
        segments.append(segment_data)

    elapsed = time.time() - start_time
    total_words = sum(len(s["words"]) for s in segments)
    print(f"Transcribed {len(segments)} segments, {total_words} words in {elapsed:.1f}s")
    print(f"Detected language: {info.language} ({info.language_probability:.0%})")

    return segments


def format_srt_time(seconds: float) -> str:
    """Convert seconds to SRT timestamp format (HH:MM:SS,mmm)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def segments_to_srt(segments: list[dict]) -> str:
    """Convert segments to SRT format."""
    srt_lines = []
    for i, seg in enumerate(segments, 1):
        start = format_srt_time(seg["start"])
        end = format_srt_time(seg["end"])
        srt_lines.append(f"{i}")
        srt_lines.append(f"{start} --> {end}")
        srt_lines.append(seg["text"])
        srt_lines.append("")
    return "\n".join(srt_lines)


def words_to_srt(segments: list[dict], max_words: int = 3, max_chars: int = 40) -> str:
    """
    Convert word-level timestamps to SRT with short phrases.
    Groups words into chunks of max_words for punchy captions.
    """
    all_words = []
    for seg in segments:
        all_words.extend(seg.get("words", []))

    if not all_words:
        # Fallback to segment-level
        return segments_to_srt(segments)

    srt_lines = []
    idx = 1
    i = 0

    while i < len(all_words):
        chunk = []
        chunk_chars = 0

        while i < len(all_words) and len(chunk) < max_words:
            word = all_words[i]["word"]
            if chunk_chars + len(word) + 1 > max_chars and chunk:
                break
            chunk.append(all_words[i])
            chunk_chars += len(word) + 1
            i += 1

        if not chunk:
            break

        start = format_srt_time(chunk[0]["start"])
        end = format_srt_time(chunk[-1]["end"])
        text = " ".join(w["word"] for w in chunk)

        srt_lines.append(f"{idx}")
        srt_lines.append(f"{start} --> {end}")
        srt_lines.append(text)
        srt_lines.append("")
        idx += 1

    return "\n".join(srt_lines)


def build_ass_style(
    font_size: int = 22,
    font_name: str = "Arial",
    font_color: str = "white",
    outline_color: str = "black",
    outline_width: int = 3,
    position: str = "bottom",
    bold: bool = True,
    shadow: int = 1,
) -> str:
    """Build ASS subtitle style string for FFmpeg."""
    # ASS color format: &HBBGGRR (BGR, not RGB)
    color_map = {
        "white": "&H00FFFFFF",
        "yellow": "&H0000FFFF",
        "cyan": "&H00FFFF00",
        "green": "&H0000FF00",
        "red": "&H000000FF",
        "orange": "&H000080FF",
        "pink": "&H00FF00FF",
    }

    primary = color_map.get(font_color.lower(), "&H00FFFFFF")
    outline = color_map.get(outline_color.lower(), "&H00000000")

    # Position: bottom=2, top=6, middle=5
    alignment = {"bottom": 2, "top": 6, "middle": 5}.get(position, 2)

    # Margin from edge
    margin_v = 40 if position == "bottom" else 30

    style = (
        f"FontName={font_name},"
        f"FontSize={font_size},"
        f"PrimaryColour={primary},"
        f"OutlineColour={outline},"
        f"Bold={1 if bold else 0},"
        f"Outline={outline_width},"
        f"Shadow={shadow},"
        f"Alignment={alignment},"
        f"MarginV={margin_v}"
    )
    return style


def burn_subtitles(
    input_path: str,
    srt_path: str,
    output_path: str,
    font_size: int = 22,
    font_name: str = "Arial",
    font_color: str = "white",
    outline_color: str = "black",
    outline_width: int = 3,
    position: str = "bottom",
    bold: bool = True,
) -> bool:
    """Burn SRT subtitles into video with FFmpeg."""
    print("Burning subtitles into video...")
    start_time = time.time()

    style = build_ass_style(
        font_size=font_size,
        font_name=font_name,
        font_color=font_color,
        outline_color=outline_color,
        outline_width=outline_width,
        position=position,
        bold=bold,
    )

    # Escape special characters in path for FFmpeg filter
    escaped_srt = srt_path.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")

    vf = f"subtitles='{escaped_srt}':force_style='{style}'"

    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-vf", vf,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "copy",
        "-movflags", "+faststart",
        "-loglevel", "error",
        output_path
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"FFmpeg error: {result.stderr[:500]}")
        # Try hardware encoder on macOS
        if "videotoolbox" not in " ".join(cmd):
            cmd_hw = [c if c != "libx264" else "h264_videotoolbox" for c in cmd]
            cmd_hw = [c for c in cmd_hw if c not in ["-preset", "fast", "-crf", "18"]]
            idx = cmd_hw.index("h264_videotoolbox")
            cmd_hw.insert(idx + 1, "-b:v")
            cmd_hw.insert(idx + 2, "8M")
            result = subprocess.run(cmd_hw, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Hardware encoder also failed: {result.stderr[:500]}")
                return False

    elapsed = time.time() - start_time
    print(f"Subtitles burned in {elapsed:.1f}s")
    return True


def main():
    parser = argparse.ArgumentParser(description="Auto-generate and burn captions into video")
    parser.add_argument("input", help="Input video file")
    parser.add_argument("output", nargs="?", help="Output video file (omit with --srt-only)")
    parser.add_argument("--srt-only", action="store_true",
                        help="Only generate SRT file, don't burn into video")
    parser.add_argument("--srt-path", type=str, default=None,
                        help="Custom path for SRT output")
    parser.add_argument("--model", type=str, default="base",
                        choices=["tiny", "base", "small", "medium", "large-v3"],
                        help="Whisper model size (default: base)")
    parser.add_argument("--language", type=str, default=None,
                        help="Force language (e.g., en, es, hi)")
    parser.add_argument("--word-level", action="store_true",
                        help="Use word-level captions (short punchy phrases)")
    parser.add_argument("--max-words", type=int, default=3,
                        help="Max words per caption in word-level mode (default: 3)")
    parser.add_argument("--font-size", type=int, default=22,
                        help="Caption font size (default: 22)")
    parser.add_argument("--font-name", type=str, default="Arial",
                        help="Caption font (default: Arial)")
    parser.add_argument("--font-color", type=str, default="white",
                        choices=["white", "yellow", "cyan", "green", "red", "orange", "pink"],
                        help="Caption text color (default: white)")
    parser.add_argument("--outline-color", type=str, default="black",
                        help="Caption outline color (default: black)")
    parser.add_argument("--position", type=str, default="bottom",
                        choices=["bottom", "top", "middle"],
                        help="Caption position (default: bottom)")
    parser.add_argument("--bold", action="store_true", default=True,
                        help="Bold text (default: True)")

    args = parser.parse_args()

    if not args.srt_only and not args.output:
        parser.error("output is required unless --srt-only is specified")

    if not os.path.exists(args.input):
        print(f"Error: Input file not found: {args.input}")
        return

    info = get_video_info(args.input)
    print(f"Video: {info['width']}x{info['height']}, {info['duration']:.1f}s")

    # Auto-scale font size for vertical video
    if info["width"] < info["height"]:
        adjusted_size = int(args.font_size * 1.3)
        print(f"Vertical video detected, scaling font: {args.font_size} -> {adjusted_size}")
        args.font_size = adjusted_size

    # Transcribe
    segments = transcribe(args.input, model_size=args.model, language=args.language)

    if not segments:
        print("No speech detected!")
        return

    # Generate SRT
    if args.word_level:
        srt_content = words_to_srt(segments, max_words=args.max_words)
        print(f"Generated word-level captions (max {args.max_words} words each)")
    else:
        srt_content = segments_to_srt(segments)
        print(f"Generated {len(segments)} caption segments")

    # Save SRT
    if args.srt_path:
        srt_path = args.srt_path
    else:
        stem = Path(args.input).stem
        srt_path = str(Path(args.input).parent / f"{stem}.srt")

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content)
    print(f"SRT saved: {srt_path}")

    if args.srt_only:
        print("Done (SRT only mode)")
        return

    # Burn subtitles
    success = burn_subtitles(
        input_path=args.input,
        srt_path=srt_path,
        output_path=args.output,
        font_size=args.font_size,
        font_name=args.font_name,
        font_color=args.font_color,
        outline_color=args.outline_color,
        position=args.position,
        bold=args.bold,
    )

    if success:
        out_size = os.path.getsize(args.output) / (1024 * 1024)
        print(f"Output: {args.output} ({out_size:.1f} MB)")
    else:
        print("Failed to burn subtitles")


if __name__ == "__main__":
    main()
