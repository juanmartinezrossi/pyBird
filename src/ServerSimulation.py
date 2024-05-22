from src.Server import Server
from settings import mode_capture


class ServerSimulation(Server):
    def __init__(self, clientName: str):
        super().__init__(clientName)

    def send_command(self, *args: str):
        message = ';'.join(args)
        self.send_message("DJM-Command", message)

    def listen_telemetry(self):
        self.subscribe_to_topic("DJM-Telemetry")

    def listen_media(self):
        self.subscribe_to_topic("DJM-Media")

    def send_telemetry(self, *args: str):
        message = ';'.join(args)
        self.send_message("DJM-Telemetry", message)

    def listen_commands(self):
        self.subscribe_to_topic("DJM-Command")

