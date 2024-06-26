import paho.mqtt.client as mqtt

broker_address ="broker.hivemq.com"
broker_port = 1883

def on_message(client, userdata, message):
    if message.topic == "DJM-Command":
        command = str(message.payload.decode("utf-8"))
        print ("command received: ",command)

client = mqtt.Client("Subscriber")
client.on_message = on_message
client.connect(broker_address, broker_port)
print ("Waiting commands...")
client.subscribe("DJM-Command")
client.loop_forever()
