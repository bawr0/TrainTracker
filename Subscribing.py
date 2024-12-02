import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "train/location"

def on_message(client, userdata, message):
    data = message.payload.decode("utf-8")
    latitude, longitude = data.split(",")
    print(f"Train Location - Latitude: {latitude}, Longitude: {longitude}")

client = mqtt.Client()
client.connect(broker, port, 60)
client.subscribe(topic)
client.on_message = on_message

print(f"Subscribed to {topic}. Waiting for updates...")
client.loop_forever()
