import cv2

# Replace with your actual phone stream URL
ipcam_url = "http://192.168.1.100:8080/video"

cap = cv2.VideoCapture(ipcam_url, cv2.CAP_FFMPEG)  # or CAP_GSTREAMER

if not cap.isOpened():
    print("❌ Could not open IP camera stream.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("GStreamer-Compatible IP Stream", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
