import cv2

from src.utils import FPSCounter, draw_fps, open_camera, save_frame


def load_cascade(filename):
    cascade_path = cv2.data.haarcascades + filename
    cascade = cv2.CascadeClassifier(cascade_path)

    if cascade.empty():
        raise RuntimeError(f"Could not load Haar Cascade file: {filename}")

    return cascade


def run(camera_index=0):
    cap = open_camera(camera_index)
    fps_counter = FPSCounter()

    face_cascade = load_cascade("haarcascade_frontalface_default.xml")
    eye_cascade = load_cascade("haarcascade_eye.xml")

    window_name = "OpenCV Vision Lab - Face and Eye Detection"

    print("\nFace and Eye Detection")
    print("Press 'q' to quit.")
    print("Press 's' to save a screenshot.\n")

    while True:
        success, frame = cap.read()

        if not success:
            print("Failed to read frame from camera.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(60, 60),
        )

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (80, 220, 80), 2)

            face_gray = gray[y:y + h, x:x + w]
            face_color = frame[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(
                face_gray,
                scaleFactor=1.1,
                minNeighbors=8,
                minSize=(20, 20),
            )

            for ex, ey, ew, eh in eyes:
                cv2.rectangle(
                    face_color,
                    (ex, ey),
                    (ex + ew, ey + eh),
                    (255, 180, 80),
                    2,
                )

        fps = fps_counter.update()
        frame = draw_fps(frame, fps)

        cv2.imshow(window_name, frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):
            save_frame(frame, "face_eye_detection")

        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
