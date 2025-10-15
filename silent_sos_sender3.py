import paho.mqtt.client as mqtt
# MQTT Broker details
BROKER = "test.mosquitto.org"
PORT = 8884
TOPIC = "silentSOS/laptop"

def send_sos():
    client = mqtt.Client()
    client.connect(BROKER, PORT)
    message = "🔕 Silent SOS: Emergency from Laptop"
    client.publish(TOPIC, message)
    client.disconnect()
    print("✅ SOS sent silently!")

# --- Hidden trigger simulation ---
input("Press Enter (secretly) to send SOS... ")
send_sos()