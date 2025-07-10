# 🗑️ Waste Monitoring System

This project is a real-world slap in the face to inefficient garbage collection. Built using Raspberry Pi and ultrasonic sensors (HC-SR04), it tracks garbage bin levels, sends that data to the cloud, calculates optimized routes for bin collectors, and even notifies them via SMS. All the stats are viewable in a clean web dashboard.

## ⚙️ What It Does

- Measures garbage level in bins using ultrasonic sensors
- Sends data to a cloud-hosted MySQL database
- Analyzes whether a bin needs to be emptied
- Calculates the most efficient pickup route
- Notifies collection personnel when bins are nearly full
- Displays all info on a slick Flask-based web UI

## 🧰 Tech Stack

### 🛠️ Hardware
- Raspberry Pi
- HC-SR04 Ultrasonic Sensors
- Breadboard + Jumper Wires
- 330Ω and 470Ω resistors

### 💻 Software
- **Languages**: Python, HTML, CSS, JS
- **Backend**: Flask + Gunicorn
- **Frontend**: Bootstrap 4
- **Database**: MySQL (cloud)
- **Python Libs**: `RPi.GPIO`, `time`, `mysql.connector`, `requests`, `Flask`

## 🔌 System Flow

1. **Sensors** → measure bin levels.
2. **Raspberry Pi** → converts pulse+echo into distance.
3. **Python Scripts** → process and push data to cloud DB.
4. **Checker Module** → determines if bin is full (>80%).
5. **SMS Notifier** → sends alerts to garbage collectors.
6. **Optimizer** → figures out shortest pickup path.
7. **Web UI** → shows real-time graphs and bin status.

## 📊 Web UI Output

- Real-time bin fill levels
- Monthly graphs
- Alerts for bins >80% full
- Route info for collection

## 🧪 How to Run

1. Set up Raspberry Pi with Raspbian OS.
2. Wire up HC-SR04 sensors to GPIO.
3. Install required Python packages.
4. Connect to MySQL cloud DB.
5. Run `collect_data.py` on the Pi.
6. Start Flask app: `gunicorn app:app`
7. Open Web UI in browser.

## 🔮 Future Upgrades

- Scale to entire cities
- Google Maps API for route mapping
- Predictive analytics using ML
