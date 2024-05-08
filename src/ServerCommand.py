from src.Server import Server
from settings import mode_capture


class ServerCommand(Server):
    def __init__(self):
        self.subscribe_to_topic("telemetry")
        if mode_capture:
            self.subscribe_to_topic("media")

    def send_command(self, command: str):
        self.send_message("command", command)





