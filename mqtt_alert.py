import cv2
import paho.mqtt.client as mqtt
from ultralytics import YOLO

# Connect to MQTT Broker (free public one)
mqtt_broker = "broker.hivemq.com"
mqtt_topic = "cmp4221/yolo/alerts"

client = mqtt.Client()
client.connect(mqtt_broker, 1883, 60)

# YOLO + Webcam
model = YOLO("yolov5s.pt")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    person_count = 0

    for box in results.boxes:
        if int(box.cls[0]) == 0:  # class 0 = person
            person_count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.putText(frame, f"People: {person_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Send alert if person found
    if person_count > 0:
        message = f"🚨 Person detected: {person_count}"
        client.publish(mqtt_topic, message)

    cv2.imshow("YOLO MQTT Alerts", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
