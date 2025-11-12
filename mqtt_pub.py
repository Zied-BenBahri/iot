import time
import paho.mqtt.client as mqtt

BROKER = "192.168.216.1"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

for i in range(5):
    message = f"Temperature: {20 + i}°C"
    client.publish("sensor/room1/temperature", message)
    print("Published:", message)
    time.sleep(1)

client.disconnect()
