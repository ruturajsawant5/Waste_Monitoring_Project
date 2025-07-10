# 🐍 Raspberry Pi Scripts – Waste Monitoring System

This folder contains the Python scripts that run on the Raspberry Pi to:

- Read bin level data from HC-SR04 ultrasonic sensors
- Process the raw pulse/echo readings into distance
- Push processed data to the cloud MySQL database
- Trigger alerts if bin fill exceeds threshold

## 🚀 How to Run

### 1. Install Requirements

Make sure you're on the Pi (Raspbian OS) and run:

```bash
pip install -r requirements.txt
python script.py
```
