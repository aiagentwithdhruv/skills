#!/usr/bin/env python3
"""
Vertical Crop: Auto-crop horizontal (16:9) video to vertical (9:16) with face tracking.

Uses OpenCV face detection to keep the speaker centered in frame.
Perfect for converting talking-head videos into Shorts/Reels/TikToks.

Usage:
    # Basic - auto-detect face and crop
    python3 vertical_crop.py input.mp4 output.mp4

    # Custom aspect ratio
    python3 vertical_crop.py input.mp4 output.mp4 --ratio 4:5

    # Fixed position (no face tracking)
    python3 vertical_crop.py input.mp4 output.mp4 --position center

    # With smoothing (less jittery tracking)
    python3 vertical_crop.py input.mp4 output.mp4 --smoothing 30

Dependencies:
    pip install opencv-python numpy
    brew install ffmpeg  # macOS
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import cv2
import numpy as np


def get_video_info(input_path: str) -> dict:
    """Get video resolution, fps, and duration."""
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height,r_frame_rate,nb_frames",
        "-show_entries", "format=duration",
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
        "nb_frames": int(stream.get("nb_frames", 0)),
    }


def detect_faces_timeline(input_path: str, sample_interval: int = 5) -> list[dict]:
    """
    Sample frames and detect face positions throughout the video.
    Returns list of {frame_num, x_center, y_center, face_width, face_height}.
    """
    print("Detecting faces throughout video...")
    start_time = time.time()

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Error: Cannot open video")
        return []

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Use Haar cascade for face detection (fast, no extra deps)
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)

    detections = []
    frame_num = 0
    sampled = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_num % sample_interval == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(int(width * 0.05), int(height * 0.05)),
            )

            if len(faces) > 0:
                # Pick the largest face
                areas = [w * h for (x, y, w, h) in faces]
                best = np.argmax(areas)
                fx, fy, fw, fh = faces[best]

                detections.append({
                    "frame": frame_num,
                    "time": frame_num / fps,
                    "x_center": fx + fw // 2,
                    "y_center": fy + fh // 2,
                    "face_width": fw,
                    "face_height": fh,
                })

            sampled += 1
            if sampled % 100 == 0:
                pct = (frame_num / total_frames) * 100
                print(f"   Scanned {pct:.0f}% ({sampled} frames sampled, {len(detections)} faces found)")

        frame_num += 1

    cap.release()
    elapsed = time.time() - start_time
    print(f"Face detection: {len(detections)} detections from {sampled} samples in {elapsed:.1f}s")

    return detections


def smooth_positions(detections: list[dict], total_frames: int, window: int = 30) -> list[float]:
    """
    Interpolate and smooth face x-positions across all frames.
    Returns list of x_center for each frame.
    """
    if not detections:
        return []

    # Create sparse position map
    positions = {}
    for d in detections:
        positions[d["frame"]] = d["x_center"]

    # Interpolate for all frames
    all_x = []
    det_frames = sorted(positions.keys())

    for f in range(total_frames):
        if f in positions:
            all_x.append(positions[f])
        else:
            # Find nearest before and after
            before = [df for df in det_frames if df <= f]
            after = [df for df in det_frames if df >= f]

            if before and after:
                b = before[-1]
                a = after[0]
                if a == b:
                    all_x.append(positions[b])
                else:
                    # Linear interpolation
                    t = (f - b) / (a - b)
                    x = positions[b] + t * (positions[a] - positions[b])
                    all_x.append(x)
            elif before:
                all_x.append(positions[before[-1]])
            elif after:
                all_x.append(positions[after[0]])
            else:
                all_x.append(0)

    # Apply moving average smoothing
    if window > 1 and len(all_x) > window:
        kernel = np.ones(window) / window
        smoothed = np.convolve(all_x, kernel, mode="same")
        # Fix edges
        half = window // 2
        smoothed[:half] = smoothed[half]
        smoothed[-half:] = smoothed[-half - 1]
        return smoothed.tolist()

    return all_x


def crop_video(
    input_path: str,
    output_path: str,
    x_positions: list[float],
    video_info: dict,
    target_ratio: tuple[int, int] = (9, 16),
) -> bool:
    """
    Crop video to vertical using pre-computed x positions.
    Uses FFmpeg with crop filter and sendcmd for dynamic positioning.
    """
    src_w = video_info["width"]
    src_h = video_info["height"]
    fps = video_info["fps"]

    # Calculate crop dimensions
    ratio_w, ratio_h = target_ratio
    crop_h = src_h
    crop_w = int(crop_h * ratio_w / ratio_h)

    if crop_w > src_w:
        crop_w = src_w
        crop_h = int(crop_w * ratio_h / ratio_w)

    # Ensure even dimensions
    crop_w = crop_w - (crop_w % 2)
    crop_h = crop_h - (crop_h % 2)

    print(f"Crop: {src_w}x{src_h} -> {crop_w}x{crop_h} ({ratio_w}:{ratio_h})")

    if not x_positions:
        # Static center crop
        x_offset = (src_w - crop_w) // 2
        y_offset = (src_h - crop_h) // 2

        cmd = [
            "ffmpeg", "-y", "-i", input_path,
            "-vf", f"crop={crop_w}:{crop_h}:{x_offset}:{y_offset}",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-c:a", "copy",
            "-movflags", "+faststart",
            "-loglevel", "error",
            output_path
        ]

        print("Cropping (static center)...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    # Dynamic crop with face tracking
    # For FFmpeg, we'll compute the median x position and use a static crop
    # (Dynamic per-frame crop requires complex sendcmd which is unreliable)
    # Instead, we split into segments with similar positions

    # Use median position for stability
    median_x = int(np.median(x_positions))
    x_offset = max(0, min(median_x - crop_w // 2, src_w - crop_w))
    y_offset = (src_h - crop_h) // 2

    # Check if face moves significantly (>20% of frame width)
    x_range = max(x_positions) - min(x_positions)
    movement_pct = x_range / src_w * 100

    if movement_pct > 20:
        print(f"Face moves {movement_pct:.0f}% of frame - using segmented tracking")
        return _segmented_crop(input_path, output_path, x_positions, video_info, crop_w, crop_h, target_ratio)

    print(f"Face stable (moves {movement_pct:.0f}%) - using static crop at x={x_offset}")

    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-vf", f"crop={crop_w}:{crop_h}:{x_offset}:{y_offset}",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "copy",
        "-movflags", "+faststart",
        "-loglevel", "error",
        output_path
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FFmpeg error: {result.stderr[:500]}")
        return False
    return True


def _segmented_crop(
    input_path: str,
    output_path: str,
    x_positions: list[float],
    video_info: dict,
    crop_w: int,
    crop_h: int,
    target_ratio: tuple[int, int],
) -> bool:
    """
    Split video into segments based on face position changes,
    crop each with appropriate offset, then concatenate.
    """
    src_w = video_info["width"]
    src_h = video_info["height"]
    fps = video_info["fps"]
    y_offset = (src_h - crop_h) // 2

    # Group frames into segments of ~2 seconds with consistent position
    segment_size = int(fps * 2)
    segments = []
    i = 0

    while i < len(x_positions):
        end = min(i + segment_size, len(x_positions))
        chunk = x_positions[i:end]
        median_x = int(np.median(chunk))
        x_off = max(0, min(median_x - crop_w // 2, src_w - crop_w))

        start_time = i / fps
        end_time = end / fps

        segments.append({
            "start": start_time,
            "end": end_time,
            "x_offset": x_off,
        })
        i = end

    print(f"Processing {len(segments)} segments...")

    with tempfile.TemporaryDirectory() as tmpdir:
        seg_paths = []

        for idx, seg in enumerate(segments):
            seg_path = os.path.join(tmpdir, f"seg_{idx:04d}.mp4")
            duration = seg["end"] - seg["start"]

            cmd = [
                "ffmpeg", "-y",
                "-ss", str(seg["start"]),
                "-i", input_path,
                "-t", str(duration),
                "-vf", f"crop={crop_w}:{crop_h}:{seg['x_offset']}:{y_offset}",
                "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                "-c:a", "aac", "-b:a", "192k",
                "-loglevel", "error",
                seg_path
            ]
            subprocess.run(cmd, capture_output=True, text=True)
            seg_paths.append(seg_path)

            if (idx + 1) % 10 == 0:
                print(f"   {idx + 1}/{len(segments)} segments done")

        # Concatenate
        concat_file = os.path.join(tmpdir, "concat.txt")
        with open(concat_file, "w") as f:
            for sp in seg_paths:
                f.write(f"file '{sp}'\n")

        cmd = [
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0",
            "-i", concat_file,
            "-c", "copy",
            "-movflags", "+faststart",
            "-loglevel", "error",
            output_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Concat error: {result.stderr[:500]}")
            return False

    return True


def main():
    parser = argparse.ArgumentParser(description="Auto-crop horizontal video to vertical with face tracking")
    parser.add_argument("input", help="Input video file")
    parser.add_argument("output", help="Output video file")
    parser.add_argument("--ratio", type=str, default="9:16",
                        help="Target aspect ratio (default: 9:16)")
    parser.add_argument("--position", type=str, default="auto",
                        choices=["auto", "left", "center", "right"],
                        help="Crop position (default: auto = face tracking)")
    parser.add_argument("--smoothing", type=int, default=30,
                        help="Smoothing window in frames (default: 30)")
    parser.add_argument("--sample-interval", type=int, default=5,
                        help="Sample every N frames for face detection (default: 5)")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file not found: {args.input}")
        return

    # Parse ratio
    ratio_parts = args.ratio.split(":")
    if len(ratio_parts) != 2:
        print(f"Error: Invalid ratio format. Use W:H (e.g., 9:16)")
        return
    target_ratio = (int(ratio_parts[0]), int(ratio_parts[1]))

    info = get_video_info(args.input)
    print(f"Input: {info['width']}x{info['height']} @ {info['fps']:.1f}fps, {info['duration']:.1f}s")

    # Check if already vertical
    if info["width"] < info["height"]:
        print("Video is already vertical! No cropping needed.")
        return

    start_time = time.time()

    if args.position == "auto":
        # Face tracking mode
        detections = detect_faces_timeline(args.input, sample_interval=args.sample_interval)

        if detections:
            total_frames = int(info["duration"] * info["fps"])
            x_positions = smooth_positions(detections, total_frames, window=args.smoothing)
        else:
            print("No faces detected, falling back to center crop")
            x_positions = []
    else:
        # Fixed position mode
        x_positions = []
        if args.position == "left":
            ratio_w, ratio_h = target_ratio
            crop_w = int(info["height"] * ratio_w / ratio_h)
            x_positions = [crop_w // 2] * int(info["duration"] * info["fps"])
        elif args.position == "right":
            ratio_w, ratio_h = target_ratio
            crop_w = int(info["height"] * ratio_w / ratio_h)
            x_positions = [info["width"] - crop_w // 2] * int(info["duration"] * info["fps"])
        # center = empty list = static center crop

    # Crop
    success = crop_video(args.input, args.output, x_positions, info, target_ratio)

    if success:
        elapsed = time.time() - start_time
        out_info = get_video_info(args.output)
        out_size = os.path.getsize(args.output) / (1024 * 1024)
        print(f"\nDone in {elapsed:.1f}s")
        print(f"Output: {out_info['width']}x{out_info['height']}, {out_size:.1f} MB")
        print(f"Saved: {args.output}")
    else:
        print("Crop failed!")


if __name__ == "__main__":
    main()
