from sense_emu import SenseHat
import paho.mqtt.client as mqtt

BROKER = "192.168.216.1"   # your PC’s IP address
TOPIC  = "sensehat/control"

sense = SenseHat()
ON  = (0,255,0)
OFF = (0,0,0)

def clear():
    sense.set_pixels([OFF]*64)

def draw_left():
    clear()
    for r in range(8): sense.set_pixel(0, r, ON)

def draw_right():
    clear()
    for r in range(8): sense.set_pixel(7, r, ON)

def draw_up():
    clear()
    for c in range(8): sense.set_pixel(c, 0, ON)

def draw_down():
    clear()
    for c in range(8): sense.set_pixel(c, 7, ON)

ACTIONS = {
    "left": draw_left,
    "right": draw_right,
    "up": draw_up,
    "down": draw_down,
    "clear": clear
}

def on_connect(client, userdata, flags, rc):
    print("Connected with code", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    cmd = msg.payload.decode().strip().lower()
    print("Received:", cmd)
    ACTIONS.get(cmd, clear)()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.loop_forever()
