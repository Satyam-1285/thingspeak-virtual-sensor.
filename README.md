# 📡 Virtual IoT Sensor: Python to ThingSpeak

This project demonstrates how to interact with the **ThingSpeak IoT Platform** without requiring physical hardware like an Arduino or ESP8266. It uses a Python script to simulate a temperature sensor and sends data to a cloud dashboard using HTTP requests.

## 🚀 Features
* **Zero Hardware:** Run the entire IoT stack on your laptop.
* **Real-time Data:** Streams simulated temperature readings every 16 seconds.
* **Cloud Visualization:** View live graphs and analytics on the ThingSpeak dashboard.
* **Error Handling:** Includes basic status code checks for API communication.



## 🛠️ How It Works
1. The Python script generates a random float value (simulating a sensor).
2. It packages this value into a URL with your unique **WK4DEJ5FHVIXPEFZ**.
3. It sends a `GET` request to the ThingSpeak servers.
4. ThingSpeak logs the data and updates your private/public channel charts.

## 📋 Prerequisites
* Python 3.x
* A ThingSpeak Account ([Sign up here](https://thingspeak.com/))
* `requests` library:
  ```bash
  pip install requests
