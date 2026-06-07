from datetime import datetime
from pathlib import Path
import time

import cv2


OUTPUT_DIR = Path("outputs")


class FPSCounter:
    """Simple FPS counter for real-time video loops."""

    def __init__(self):
        self.previous_time = time.time()
        self.fps = 0.0

    def update(self):
        current_time = time.time()
        elapsed = current_time - self.previous_time

        if elapsed > 0:
            self.fps = 1.0 / elapsed

        self.previous_time = current_time
        return self.fps


def open_camera(camera_index=0):
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        raise RuntimeError(
            f"Could not open camera with index {camera_index}. "
            "Try another index, for example: --camera 1"
        )

    return cap


def draw_label(frame, text, position=(10, 30)):
    x, y = position

    cv2.rectangle(
        frame,
        (x - 5, y - 24),
        (x + 220, y + 8),
        (0, 0, 0),
        thickness=-1,
    )

    cv2.putText(
        frame,
        text,
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )

    return frame


def draw_fps(frame, fps):
    return draw_label(frame, f"FPS: {fps:.1f}", position=(10, 30))


def save_frame(frame, prefix):
    OUTPUT_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = OUTPUT_DIR / f"{prefix}_{timestamp}.png"

    cv2.imwrite(str(path), frame)
    print(f"Saved screenshot: {path}")

    return path


def show_help(window_name):
    print(f"\n{window_name}")
    print("Controls:")
    print("  q  - quit")
    print("  s  - save screenshot")
    print()
