import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "silentSOS/laptop"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected!")
        client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"📩 SOS Received: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
print("🎧 Listening for SOS...")
client.loop_forever()