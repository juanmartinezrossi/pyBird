import paho.mqtt.client as mqtt
import socket
from abc import abstractmethod

from settings import server_broker_address, server_broker_port, usb_comm_port, server_internal_port


def on_message(client, userdata, message):
    command = message.payload.decode("utf-8")
    get_message(message.topic, command)


def get_message(topic, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', server_internal_port))
        s.sendall(f"{topic}:{message}".encode())


class Server:
    def __init__(self, clientName: str):
        self.clientName = clientName
        self.broker_address = server_broker_address
        self.broker_port = server_broker_port
        self.client = mqtt.Client(self.clientName)
        self.client.on_message = on_message

    def connect(self):
        self.client.connect(self.broker_address, self.broker_port)
        print(f'server connected to broker address: {self.broker_address} through port: {self.broker_port}')

    def loop(self):
        self.client.loop_start()
        print("Server listening...")

    def subscribe_to_topic(self, topic: str):
        self.client.subscribe(topic)
        print(f'Subscribed to topic: {topic}')

    def send_message(self, topic: str, message: str):
        print(f"Sending message ({topic}): {message}")
        self.client.publish(topic, message)

    def disconnect(self):
        self.client.disconnect()
        self.client.loop_stop()

