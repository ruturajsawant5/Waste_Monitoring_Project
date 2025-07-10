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

## 🌍 Environment Variables

The following environment variables are required for the application to function properly:

### 📦 Database Configuration

- `DB_HOST` – Hostname or IP of the MySQL database (default: `"your-db-host"`)
- `DB_USER` – MySQL username (default: `"your-db-user"`)
- `DB_PASSWORD` – MySQL password (default: `"your-db-password"`)
- `DB_NAME` – Name of the MySQL database (default: `"your-db-name"`)

### 📲 SMS Notification Configuration

- `SMS_AUTH_TOKEN` – Authorization token for the SMS API provider
- `DEFAULT_TEST_NUMBER` – Phone number to send test or fallback SMS alerts to
