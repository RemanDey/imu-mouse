# 📱 Gyroscope-Controlled Wireless Mouse (Phyphox + Python)

Turn your smartphone into a **motion-controlled wireless air mouse** using its built-in gyroscope and WiFi. This project uses the phyphox app to stream real-time sensor data, which is processed in Python to control your computer’s cursor.

---

## 🚀 Features
- 📡 Wireless control over WiFi (HTTP-based)
- 🎮 Real-time cursor movement using gyroscope data
- 📱 Uses phyphox (no custom mobile app required)
- 🐍 Simple Python implementation (`requests` + `pyautogui`)
- ⚡ Quick setup with minimal dependencies

---

## 🧠 How It Works

1. The phyphox app reads **gyroscope data** from your phone  
2. It exposes this data via a built-in **HTTP server**  
3. The Python script continuously fetches this data  
4. Angular velocity values are mapped to cursor movement  

👉 This creates a **relative air mouse**, where rotating the phone moves the cursor.

---

## 🛠️ Tech Stack

- **Python**
  - `requests` – HTTP communication  
  - `pyautogui` – cursor control  

- **Mobile App**
  - phyphox  

- **Sensors**
  - Gyroscope (IMU)

---

## ⚙️ Setup Instructions

### 1. Install dependencies
```bash
pip install requests pyautogui
