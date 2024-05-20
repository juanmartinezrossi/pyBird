from src.Server import Server


class ServerTelemetryAndMedia(Server):
    def __init__(self, clientName: str):
        super().__init__(clientName)

    def send_telemetry(self, *args: str):
        message = ';'.join(args)
        self.send_message("Telemetry", message)

    def send_media(self, *args: str):
        message = ';'.join(args)
        self.send_message("Media", message)

    def listen_commands(self):
        self.subscribe_to_topic('Command')

