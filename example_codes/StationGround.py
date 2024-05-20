import paho.mqtt.client as mqtt
import time

broker_address = "broker.hivemq.com"
broker_port = 1883


def on_message(client, userdata, message):
    time.sleep(5)
    command = message.payload.decode("utf-8")
    print("Command received:", command)
    if command == "Armed":
        print("Sending command: takeoff")
        client.publish('Command', 'takeoff')


client = mqtt.Client("GroundStation")
client.on_message = on_message
client.connect(broker_address, broker_port)

client.subscribe("response")
client.loop_start()

print("Sending command: arm")
client.publish('Command', 'arm')

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
