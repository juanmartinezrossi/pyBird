from src.Server import Server
from settings import mode_capture


class ServerCommand(Server):
    def __init__(self, clientName: str):
        #print(f"inicializando clase padre con clientName: {clientName}")
        super().__init__(clientName)
        #print("inicializando subscripciones")
        self.subscribe_to_topic("telemetry")
        if mode_capture:
            self.subscribe_to_topic("media")
        #print("inicializado")

    def send_command(self, *args: str):
        message = ';'.join(args)
        self.send_message("Command", message)





