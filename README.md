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
