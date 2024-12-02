import paho.mqtt.client as mqtt
import time

broker = "broker.hivemq.com"
port = 1883
topic = "train/location"

client = mqtt.Client()
client.connect(broker, port, 60)

def publish_location():
    latitude = 30.0000
    longitude = -120.0000

    while True:
        message = f"{latitude},{longitude}"
        client.publish(topic, message)
        print(f"Published: {message}")
        time.sleep(5)

publish_location()
