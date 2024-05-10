import paho.mqtt.client as mqtt
import time

broker_address ="broker.hivemq.com"
broker_port = 1883

client = mqtt.Client("Publisher")
client.connect(broker_address, broker_port)

while True:
    client.publish('Command', 'arm')
    time.sleep(5)
    client.publish ('Command', 'takeoff')
    time.sleep(5)
print ("Goodbye")
