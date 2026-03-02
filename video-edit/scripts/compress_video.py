#!/usr/bin/env python3
"""
Video Compressor: Quick compress videos for social media with presets.

Supports platform-specific presets (YouTube, Instagram, TikTok, Twitter, LinkedIn)
with optimal resolution, bitrate, and codec settings.

Usage:
    # Quick compress (auto-detect best settings)
    python3 compress_video.py input.mp4 output.mp4

    # Platform preset
    python3 compress_video.py input.mp4 output.mp4 --preset instagram-reel
    python3 compress_video.py input.mp4 output.mp4 --preset youtube
    python3 compress_video.py input.mp4 output.mp4 --preset twitter

    # Target file size
    python3 compress_video.py input.mp4 output.mp4 --target-size 25

    # Custom settings
    python3 compress_video.py input.mp4 output.mp4 --resolution 720 --crf 28 --audio-bitrate 128

Dependencies:
    brew install ffmpeg  # macOS
"""

import argparse
import json
import os
import subprocess
import sys
import time


# Platform presets: {max_res, max_fps, video_bitrate, audio_bitrate, max_duration, notes}
PRESETS = {
    "youtube": {
        "max_height": 1080,
        "max_fps": 60,
        "crf": 18,
        "audio_bitrate": "192k",
        "max_duration": None,
        "codec": "h264",
        "notes": "YouTube (high quality)",
    },
    "youtube-shorts": {
        "max_height": 1920,
        "max_width": 1080,
        "max_fps": 60,
        "crf": 20,
        "audio_bitrate": "192k",
        "max_duration": 60,
        "codec": "h264",
        "notes": "YouTube Shorts (max 60s, vertical)",
    },
    "instagram-reel": {
        "max_height": 1920,
        "max_width": 1080,
        "max_fps": 30,
        "crf": 23,
        "audio_bitrate": "128k",
        "max_duration": 90,
        "codec": "h264",
        "notes": "Instagram Reel (max 90s, vertical)",
    },
    "instagram-post": {
        "max_height": 1080,
        "max_width": 1080,
        "max_fps": 30,
        "crf": 23,
        "audio_bitrate": "128k",
        "max_duration": 60,
        "codec": "h264",
        "notes": "Instagram Post (max 60s, square/vertical)",
    },
    "tiktok": {
        "max_height": 1920,
        "max_width": 1080,
        "max_fps": 60,
        "crf": 23,
        "audio_bitrate": "128k",
        "max_duration": 180,
        "codec": "h264",
        "notes": "TikTok (max 3min, vertical)",
    },
    "twitter": {
        "max_height": 1080,
        "max_fps": 60,
        "crf": 23,
        "audio_bitrate": "128k",
        "max_duration": 140,
        "codec": "h264",
        "max_size_mb": 512,
        "notes": "Twitter/X (max 512MB)",
    },
    "linkedin": {
        "max_height": 1080,
        "max_fps": 30,
        "crf": 23,
        "audio_bitrate": "128k",
        "max_duration": 600,
        "codec": "h264",
        "max_size_mb": 200,
        "notes": "LinkedIn (max 10min, 200MB)",
    },
    "telegram": {
        "max_height": 720,
        "max_fps": 30,
        "crf": 28,
        "audio_bitrate": "96k",
        "max_duration": None,
        "codec": "h264",
        "max_size_mb": 50,
        "notes": "Telegram (max 50MB for bots)",
    },
    "whatsapp": {
        "max_height": 720,
        "max_fps": 30,
        "crf": 28,
        "audio_bitrate": "96k",
        "max_duration": 120,
        "codec": "h264",
        "max_size_mb": 16,
        "notes": "WhatsApp (max 16MB)",
    },
    "small": {
        "max_height": 480,
        "max_fps": 30,
        "crf": 30,
        "audio_bitrate": "64k",
        "max_duration": None,
        "codec": "h264",
        "notes": "Small file (low quality, fast sharing)",
    },
}


def get_video_info(input_path: str) -> dict:
    """Get video metadata."""
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height,r_frame_rate,codec_name,bit_rate",
        "-show_entries", "format=duration,size,bit_rate",
        "-of", "json", input_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(result.stdout)
    stream = data.get("streams", [{}])[0]
    fmt = data.get("format", {})

    fps_str = stream.get("r_frame_rate", "30/1")
    if "/" in fps_str:
        num, den = fps_str.split("/")
        fps = float(num) / float(den)
    else:
        fps = float(fps_str)

    return {
        "width": int(stream.get("width", 1920)),
        "height": int(stream.get("height", 1080)),
        "fps": fps,
        "duration": float(fmt.get("duration", 0)),
        "size_mb": int(fmt.get("size", 0)) / (1024 * 1024),
        "bitrate": int(fmt.get("bit_rate", 0)),
        "codec": stream.get("codec_name", "unknown"),
    }


def calculate_bitrate_for_size(target_size_mb: float, duration: float, audio_bitrate_kbps: int = 128) -> int:
    """Calculate video bitrate to hit target file size."""
    target_bits = target_size_mb * 8 * 1024 * 1024
    audio_bits = audio_bitrate_kbps * 1000 * duration
    video_bits = target_bits - audio_bits
    video_bitrate = max(int(video_bits / duration), 100000)  # min 100kbps
    return video_bitrate


def compress(
    input_path: str,
    output_path: str,
    max_height: int = 1080,
    max_width: int = None,
    max_fps: int = None,
    crf: int = 23,
    audio_bitrate: str = "128k",
    max_duration: float = None,
    target_bitrate: int = None,
    codec: str = "h264",
    two_pass: bool = False,
) -> bool:
    """Compress video with given settings."""
    info = get_video_info(input_path)

    # Build video filter
    vf_parts = []

    # Scale down if needed
    needs_scale = False
    scale_w = info["width"]
    scale_h = info["height"]

    if info["height"] > max_height:
        scale_h = max_height
        scale_w = -2  # auto-calculate maintaining aspect ratio
        needs_scale = True

    if max_width and info["width"] > max_width:
        scale_w = max_width
        if not needs_scale:
            scale_h = -2
        needs_scale = True

    if needs_scale:
        vf_parts.append(f"scale={scale_w}:{scale_h}")

    # FPS limit
    if max_fps and info["fps"] > max_fps:
        vf_parts.append(f"fps={max_fps}")

    vf = ",".join(vf_parts) if vf_parts else None

    # Choose encoder
    encoder = "libx264"
    if codec == "h265":
        encoder = "libx265"

    # Try hardware encoder on macOS
    hw_encoder = None
    if sys.platform == "darwin":
        hw_check = subprocess.run(
            ["ffmpeg", "-hide_banner", "-encoders"],
            capture_output=True, text=True, timeout=5
        )
        if codec == "h264" and "h264_videotoolbox" in hw_check.stdout:
            hw_encoder = "h264_videotoolbox"
        elif codec == "h265" and "hevc_videotoolbox" in hw_check.stdout:
            hw_encoder = "hevc_videotoolbox"

    # Build command
    cmd = ["ffmpeg", "-y", "-i", input_path]

    # Duration limit
    if max_duration and info["duration"] > max_duration:
        cmd.extend(["-t", str(max_duration)])
        print(f"Trimming to {max_duration}s (original: {info['duration']:.1f}s)")

    # Video filter
    if vf:
        cmd.extend(["-vf", vf])

    # Encoder settings
    if hw_encoder and not target_bitrate:
        cmd.extend(["-c:v", hw_encoder, "-b:v", f"{crf}M"])
    elif target_bitrate:
        cmd.extend(["-c:v", encoder, "-b:v", str(target_bitrate)])
    else:
        cmd.extend(["-c:v", encoder, "-preset", "fast", "-crf", str(crf)])

    # Audio
    cmd.extend(["-c:a", "aac", "-b:a", audio_bitrate])

    # Faststart for web playback
    cmd.extend(["-movflags", "+faststart", "-loglevel", "error", output_path])

    print("Compressing...")
    start_time = time.time()

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        # Fallback to software encoder
        if hw_encoder:
            print("Hardware encoder failed, trying software...")
            cmd = [c if c != hw_encoder else encoder for c in cmd]
            if encoder == "libx264":
                # Add preset and CRF for software
                idx = cmd.index(encoder)
                cmd.insert(idx + 1, "-preset")
                cmd.insert(idx + 2, "fast")
                cmd.insert(idx + 3, "-crf")
                cmd.insert(idx + 4, str(crf))
                # Remove -b:v if present
                try:
                    bv_idx = cmd.index("-b:v")
                    del cmd[bv_idx:bv_idx + 2]
                except ValueError:
                    pass
            result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Compression failed: {result.stderr[:500]}")
            return False

    elapsed = time.time() - start_time
    return True


def main():
    parser = argparse.ArgumentParser(description="Compress video for social media")
    parser.add_argument("input", help="Input video file")
    parser.add_argument("output", help="Output video file")
    parser.add_argument("--preset", type=str, default=None,
                        choices=list(PRESETS.keys()),
                        help="Platform preset")
    parser.add_argument("--resolution", type=int, default=None,
                        help="Max height in pixels (e.g., 720, 1080)")
    parser.add_argument("--crf", type=int, default=23,
                        help="Quality (0=lossless, 51=worst, default: 23)")
    parser.add_argument("--audio-bitrate", type=str, default="128k",
                        help="Audio bitrate (default: 128k)")
    parser.add_argument("--target-size", type=float, default=None,
                        help="Target file size in MB")
    parser.add_argument("--max-duration", type=float, default=None,
                        help="Max duration in seconds (trims if longer)")
    parser.add_argument("--list-presets", action="store_true",
                        help="List all available presets")

    args = parser.parse_args()

    if args.list_presets:
        print("Available presets:\n")
        for name, cfg in PRESETS.items():
            notes = cfg.get("notes", "")
            max_h = cfg.get("max_height", "?")
            crf = cfg.get("crf", "?")
            dur = cfg.get("max_duration")
            dur_str = f", max {dur}s" if dur else ""
            size = cfg.get("max_size_mb")
            size_str = f", max {size}MB" if size else ""
            print(f"  {name:20s} {notes} (max {max_h}p, CRF {crf}{dur_str}{size_str})")
        return

    if not os.path.exists(args.input):
        print(f"Error: File not found: {args.input}")
        return

    info = get_video_info(args.input)
    print(f"Input: {info['width']}x{info['height']} @ {info['fps']:.1f}fps")
    print(f"Duration: {info['duration']:.1f}s ({info['duration']/60:.1f} min)")
    print(f"Size: {info['size_mb']:.1f} MB | Codec: {info['codec']}")

    # Apply preset
    if args.preset:
        p = PRESETS[args.preset]
        print(f"\nPreset: {p['notes']}")

        max_height = p.get("max_height", 1080)
        max_width = p.get("max_width")
        max_fps = p.get("max_fps")
        crf = p.get("crf", 23)
        audio_bitrate = p.get("audio_bitrate", "128k")
        max_duration = p.get("max_duration")
        codec = p.get("codec", "h264")
        max_size = p.get("max_size_mb")

        # Calculate bitrate if size-limited
        target_bitrate = None
        if max_size and info["size_mb"] > max_size:
            dur = min(info["duration"], max_duration) if max_duration else info["duration"]
            target_bitrate = calculate_bitrate_for_size(max_size * 0.95, dur)
            print(f"Size-limited: targeting {max_size}MB -> {target_bitrate/1000:.0f} kbps")
    else:
        max_height = args.resolution or 1080
        max_width = None
        max_fps = None
        crf = args.crf
        audio_bitrate = args.audio_bitrate
        max_duration = args.max_duration
        codec = "h264"
        target_bitrate = None

        if args.target_size:
            dur = min(info["duration"], max_duration) if max_duration else info["duration"]
            audio_kbps = int(audio_bitrate.replace("k", ""))
            target_bitrate = calculate_bitrate_for_size(args.target_size * 0.95, dur, audio_kbps)
            print(f"Target: {args.target_size}MB -> {target_bitrate/1000:.0f} kbps video")

    start_time = time.time()

    success = compress(
        input_path=args.input,
        output_path=args.output,
        max_height=max_height,
        max_width=max_width if args.preset else None,
        max_fps=max_fps,
        crf=crf,
        audio_bitrate=audio_bitrate,
        max_duration=max_duration,
        target_bitrate=target_bitrate,
        codec=codec,
    )

    if success:
        elapsed = time.time() - start_time
        out_info = get_video_info(args.output)
        print(f"\nDone in {elapsed:.1f}s")
        print(f"Output: {out_info['width']}x{out_info['height']}, {out_info['size_mb']:.1f} MB")
        ratio = (1 - out_info["size_mb"] / info["size_mb"]) * 100
        print(f"Compressed: {info['size_mb']:.1f} MB -> {out_info['size_mb']:.1f} MB ({ratio:.0f}% smaller)")
    else:
        print("Compression failed!")


if __name__ == "__main__":
    main()
