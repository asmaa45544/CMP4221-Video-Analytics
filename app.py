from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
import cv2
from ultralytics import YOLO

app = FastAPI()
model = YOLO("yolov5s.pt")
cap = cv2.VideoCapture(0)

def generate_frames():
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

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
        <head><title>YOLOv5 Stream</title></head>
        <body>
            <h2>Real-Time Stream (via FastAPI)</h2>
            <img src="/video" width="640" />
        </body>
    </html>
    """

@app.get("/video")
def video():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")
