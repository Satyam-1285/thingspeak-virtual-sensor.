import requests
import time
import random

api_key = "WK4DEJ5FHVIXPEFZ"
url = f" https://api.thingspeak.com/update?api_key=WK4DEJ5FHVIXPEFZ&field1=34"

while True:
    # Simulate a sensor reading
    temp = random.uniform(20.0, 30.0) 
    
    # Send to ThingSpeak
    response = requests.get(f"{url}&field1={temp}")
    print(f"Sent {temp:.2f} to ThingSpeak. Status: {response.status_code}")
    
    # ThingSpeak free tier requires a 15-second delay between updates
    time.sleep(16)
