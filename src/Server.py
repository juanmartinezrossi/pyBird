import paho.mqtt.client as mqtt
import time
from abc import abstractmethod

from settings import server_broker_address, server_broker_port, mode_simulation, usb_comm_port


class Server:

    def __init__(self, clientName: str):
        self.clientName = clientName
        self.broker_address = server_broker_address
        self.broker_port = server_broker_port
        self.client = mqtt.Client(self.clientName)
        self.client.connect(self.broker_address, self.broker_port)
        self.client.loop_start()

    def config(self):
        pass

    def subscribe_to_topic(self, topic: str):
        self.client.subscribe(topic)

    def send_message(self, topic: str, message: str):
        self.client.publish(topic, message)

    def disconnect(self):
        self.client.disconnect()
        self.client.loop_stop()

    def on_message(client, userdata, message):
        command = message.payload.decode("utf-8")
        return command

