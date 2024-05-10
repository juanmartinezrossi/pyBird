import paho.mqtt.client as mqtt
import time

broker_address = "broker.hivemq.com"
broker_port = 1883


def on_message(client, userdata, message):
    time.sleep(5)
    command = message.payload.decode("utf-8")
    print("Command received:", command)
    if command == "arm":
        print("Sending command: armed")
        client.publish('response', 'armed')


client = mqtt.Client("Drone")
client.on_message = on_message
client.connect(broker_address, broker_port)

client.subscribe("Command")
client.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
