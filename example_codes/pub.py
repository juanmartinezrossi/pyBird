import paho.mqtt.client as mqtt
import time

broker_address ="broker.hivemq.com"
broker_port = 1883

client = mqtt.Client("Publisher")
client.connect(broker_address, broker_port)
Topic = 'Telemetry'

while True:
    client.publish(Topic, 'Arm')
    time.sleep(5)
    client.publish(Topic, 'TakeOff')
    time.sleep(5)
print ("Goodbye")
