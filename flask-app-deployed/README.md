# 🌐 Waste Monitoring System – Web GUI

This is the Flask-based frontend for the Smart Waste Monitoring System. It pulls garbage bin data from a MySQL cloud database and displays it using graphs and a web dashboard.

## 📊 Features

- Real-time bin fill-level display
- Graphical analysis of waste data
- Auto-refreshing dashboard
- Pulls data directly from cloud MySQL

## 🚀 Deployment

### ✅ Method 1: Python + Gunicorn

pip install -r requirements.txt  
gunicorn app:app --bind 0.0.0.0:5000

### 🐳 Method 2: Docker

docker build -t waste-monitor-gui .  
docker run -d -p 5000:5000 waste-monitor-gui

## ⚙️ Environment Variables

DB_HOST=<your-db-host>  
DB_USER=<your-db-username>  
DB_PASS=<your-db-password>  
DB_NAME=<your-db-name>
