import cv2

from src.utils import FPSCounter, draw_fps, open_camera, save_frame


def load_face_cascade():
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(cascade_path)

    if cascade.empty():
        raise RuntimeError("Could not load Haar Cascade face detector.")

    return cascade


def run(camera_index=0):
    cap = open_camera(camera_index)
    fps_counter = FPSCounter()
    face_cascade = load_face_cascade()

    window_name = "OpenCV Vision Lab - Face Blur"

    print("\nFace Blur")
    print("This demo detects faces and blurs them for privacy.")
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
            face_region = frame[y:y + h, x:x + w]
            blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
            frame[y:y + h, x:x + w] = blurred_face

            cv2.rectangle(frame, (x, y), (x + w, y + h), (80, 220, 80), 2)

        fps = fps_counter.update()
        frame = draw_fps(frame, fps)

        cv2.imshow(window_name, frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):
            save_frame(frame, "face_blur")

        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
