import cv2
import threading
from ultralytics import YOLO

model = YOLO("yolov5s.pt")

def detect_from_camera(source, window_name):
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print(f"❌ Could not open source: {source}")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        count = 0
        for box in results.boxes:
            if int(box.cls[0]) == 0:
                count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.putText(frame, f"People: {count}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyWindow(window_name)

# 🖥️ Camera 1 = laptop webcam
# 📱 Camera 2 = phone (update IP if needed)
phone_stream = "http://192.168.1.100:8080/video"

thread1 = threading.Thread(target=detect_from_camera, args=(0, "Camera 1"))
thread2 = threading.Thread(target=detect_from_camera, args=(phone_stream, "Camera 2"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
