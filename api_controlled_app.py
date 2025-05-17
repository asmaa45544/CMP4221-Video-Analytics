from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import threading
import cv2
from ultralytics import YOLO

app = FastAPI()
model = YOLO("yolov5s.pt")

detection_thread = None
stop_event = threading.Event()

def detection_loop():
    cap = cv2.VideoCapture(0)
    while not stop_event.is_set():
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

        cv2.imshow("Controlled Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>YOLO Stream Control</title></head>
        <body>
            <h2>Control Stream</h2>
            <form action="/start"><button>▶️ Start Detection</button></form><br>
            <form action="/stop"><button>⛔ Stop Detection</button></form>
        </body>
    </html>
    """

@app.get("/start")
def start_detection():
    global detection_thread, stop_event
    if detection_thread is None or not detection_thread.is_alive():
        stop_event.clear()
        detection_thread = threading.Thread(target=detection_loop)
        detection_thread.start()
        return {"status": "Detection started"}
    else:
        return {"status": "Detection is already running"}

@app.get("/stop")
def stop_detection():
    global stop_event
    stop_event.set()
    return {"status": "Detection stopping"}
