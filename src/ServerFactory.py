from settings import *
from src import Server


def build() -> Server:
    if device_type == 'ground_station':
        from src.ServerCommand import ServerCommand
        server = ServerCommand()
    elif device_type == 'bird_raspberry':
        print("Method not implemented")
        #from src.ServerTelemetryAndMedia import ServerTelemetryAndMedia
        #server = ServerTelemetryAndMedia()
    else:
        raise Exception('No device selected')

    return server
