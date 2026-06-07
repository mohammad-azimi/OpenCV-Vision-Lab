import cv2

from src.utils import FPSCounter, draw_fps, open_camera, save_frame


def run(camera_index=0):
    cap = open_camera(camera_index)
    fps_counter = FPSCounter()

    background_subtractor = cv2.createBackgroundSubtractorMOG2(
        history=500,
        varThreshold=50,
        detectShadows=True,
    )

    window_name = "OpenCV Vision Lab - Motion Detection"

    print("\nMotion Detection")
    print("Move in front of the camera to see motion boxes.")
    print("Press 'q' to quit.")
    print("Press 's' to save a screenshot.\n")

    while True:
        success, frame = cap.read()

        if not success:
            print("Failed to read frame from camera.")
            break

        foreground_mask = background_subtractor.apply(frame)

        _, threshold = cv2.threshold(
            foreground_mask,
            244,
            255,
            cv2.THRESH_BINARY,
        )

        contours, _ = cv2.findContours(
            threshold,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        for contour in contours:
            area = cv2.contourArea(contour)

            if area < 900:
                continue

            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (80, 220, 80), 2)
            cv2.putText(
                frame,
                "Motion",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (80, 220, 80),
                2,
                cv2.LINE_AA,
            )

        fps = fps_counter.update()
        frame = draw_fps(frame, fps)

        cv2.imshow(window_name, frame)
        cv2.imshow("Motion Mask", threshold)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):
            save_frame(frame, "motion_detection")

        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
