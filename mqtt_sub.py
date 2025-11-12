import paho.mqtt.client as mqtt

BROKER = "192.168.216.1"   # your PC's IP
TOPIC  = "sensor/#"

def on_connect(client, userdata, flags, rc):
    print("Connected with code", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"{msg.topic} -> {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.loop_forever()
