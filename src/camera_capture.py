import cv2

from src.utils import FPSCounter, draw_fps, open_camera, save_frame


def run(camera_index=0):
    cap = open_camera(camera_index)
    fps_counter = FPSCounter()

    window_name = "OpenCV Vision Lab - Camera Capture"
    print("\nCamera Capture")
    print("Press 'q' to quit.")
    print("Press 's' to save a screenshot.\n")

    while True:
        success, frame = cap.read()

        if not success:
            print("Failed to read frame from camera.")
            break

        fps = fps_counter.update()
        frame = draw_fps(frame, fps)

        cv2.imshow(window_name, frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):
            save_frame(frame, "camera_capture")

        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
