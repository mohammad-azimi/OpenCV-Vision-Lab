import cv2
import numpy as np

from src.utils import FPSCounter, draw_fps, open_camera, save_frame


def nothing(_):
    pass


def create_trackbars(window_name):
    cv2.namedWindow(window_name)

    cv2.createTrackbar("Lower H", window_name, 35, 179, nothing)
    cv2.createTrackbar("Lower S", window_name, 80, 255, nothing)
    cv2.createTrackbar("Lower V", window_name, 80, 255, nothing)

    cv2.createTrackbar("Upper H", window_name, 85, 179, nothing)
    cv2.createTrackbar("Upper S", window_name, 255, 255, nothing)
    cv2.createTrackbar("Upper V", window_name, 255, 255, nothing)


def get_hsv_range(window_name):
    lower_h = cv2.getTrackbarPos("Lower H", window_name)
    lower_s = cv2.getTrackbarPos("Lower S", window_name)
    lower_v = cv2.getTrackbarPos("Lower V", window_name)

    upper_h = cv2.getTrackbarPos("Upper H", window_name)
    upper_s = cv2.getTrackbarPos("Upper S", window_name)
    upper_v = cv2.getTrackbarPos("Upper V", window_name)

    lower = np.array([lower_h, lower_s, lower_v])
    upper = np.array([upper_h, upper_s, upper_v])

    return lower, upper


def run(camera_index=0):
    cap = open_camera(camera_index)
    fps_counter = FPSCounter()

    window_name = "OpenCV Vision Lab - Color Detection"
    create_trackbars(window_name)

    print("\nColor Detection")
    print("Move the HSV sliders to detect different colors.")
    print("Press 'q' to quit.")
    print("Press 's' to save a screenshot.\n")

    while True:
        success, frame = cap.read()

        if not success:
            print("Failed to read frame from camera.")
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower, upper = get_hsv_range(window_name)

        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(frame, frame, mask=mask)

        fps = fps_counter.update()
        result = draw_fps(result, fps)

        cv2.imshow(window_name, result)
        cv2.imshow("Color Mask", mask)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):
            save_frame(result, "color_detection")

        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
