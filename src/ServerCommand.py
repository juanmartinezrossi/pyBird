from src.Server import Server
from settings import mode_capture


class ServerCommand(Server):
    def __init__(self, clientName: str):
        super().__init__(clientName)

    def send_command(self, *args: str):
        message = ';'.join(args)
        self.send_message("Command", message)

    def listen_telemetry(self):
        self.subscribe_to_topic("Telemetry")

    def listen_media(self):
        self.subscribe_to_topic("Media")

