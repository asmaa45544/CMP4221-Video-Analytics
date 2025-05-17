# CMP4221 - Intelligent Multi-Source Video Analytics and Streaming Platform

This is my final project for the Multimedia Systems and Communications (CMP4221) course.

It implements a real-time, multi-source video analytics platform using:

- 🎥 YOLOv5 for person detection
- 🌐 FastAPI for web streaming and REST control
- 📡 MQTT for real-time alerts
- 🗃️ Logging to CSV for tracking events
- 🎛️ Multi-camera and GStreamer-style input support

---

## 📁 Features

✅ Real-time person detection using YOLOv5  
✅ Stream output to browser via FastAPI (`/video`)  
✅ REST API to Start/Stop detection (`/start`, `/stop`)  
✅ CSV logging with timestamps  
✅ MQTT alerts when people are detected  
✅ Multi-camera support (Webcam + IP Camera)  
✅ Tested with GStreamer-compatible IP stream

---
## 🛠️ Setup Instructions

### ✅ Python Dependencies
Install with:

### ✅ GStreamer Installation (Windows)
1. Install GStreamer Runtime + Development (MSVC 64-bit) from:  
   https://gstreamer.freedesktop.org/download/

2. Add to system PATH:  
   `C:\gstreamer\1.0\msvc_x86_64\bin`

3. Test:

### ✅ MQTT Broker Setup

Use either:
- Public broker: `broker.hivemq.com` (port 1883)  
- OR install Mosquitto from: https://mosquitto.org/download/

Use:
to monitor alerts.

