import argparse

from src.camera_capture import run as run_camera
from src.color_detection import run as run_color
from src.face_blur import run as run_blur
from src.face_eye_detection import run as run_face
from src.motion_detection import run as run_motion
from src.multiview_display import run as run_multiview


DEMOS = {
    "camera": run_camera,
    "color": run_color,
    "face": run_face,
    "motion": run_motion,
    "blur": run_blur,
    "multiview": run_multiview,
}


def main():
    parser = argparse.ArgumentParser(
        description="OpenCV Vision Lab - real-time computer vision demos"
    )
    parser.add_argument(
        "demo",
        choices=[*DEMOS.keys(), "list"],
        help="Demo to run",
    )
    parser.add_argument(
        "--camera",
        type=int,
        default=0,
        help="Camera index. Default: 0",
    )

    args = parser.parse_args()

    if args.demo == "list":
        print("Available demos:")
        for demo_name in DEMOS:
            print(f"  - {demo_name}")
        return

    DEMOS[args.demo](camera_index=args.camera)


if __name__ == "__main__":
    main()
