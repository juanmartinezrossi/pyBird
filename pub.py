import paho.mqtt.client as mqtt
import  time

broker_address ="broker.hivemq.com"
broker_port = 1883

client = mqtt.Client("Publisher")
client.connect(broker_address, broker_port)
client.publish('command', 'arm')
time.sleep(5)
client.publish ('command', 'takeoff')
print ("Goodbye")
