import cv2
import numpy as np

from src.utils import FPSCounter, draw_fps, draw_label, open_camera, save_frame


def resize_frame(frame, width=420, height=280):
    return cv2.resize(frame, (width, height))


def run(camera_index=0):
    cap = open_camera(camera_index)
    fps_counter = FPSCounter()

    window_name = "OpenCV Vision Lab - Multi View"

    print("\nMulti View Display")
    print("Press 'q' to quit.")
    print("Press 's' to save a screenshot.\n")

    while True:
        success, frame = cap.read()

        if not success:
            print("Failed to read frame from camera.")
            break

        original = resize_frame(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        gray = resize_frame(gray)

        edges = cv2.Canny(frame, 100, 200)
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        edges = resize_frame(edges)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        hsv = resize_frame(hsv)

        draw_label(original, "Original")
        draw_label(gray, "Grayscale")
        draw_label(edges, "Edges")
        draw_label(hsv, "HSV View")

        top = np.hstack((original, gray))
        bottom = np.hstack((edges, hsv))
        combined = np.vstack((top, bottom))

        fps = fps_counter.update()
        combined = draw_fps(combined, fps)

        cv2.imshow(window_name, combined)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):
            save_frame(combined, "multiview")

        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
