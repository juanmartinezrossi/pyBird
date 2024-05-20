from settings import *
from src import Server


def build() -> Server:
    if device_type == 'ground_station':
        from src.ServerCommand import ServerCommand
        server = ServerCommand("ground_station")
        server.connect()
        server.listen_telemetry()
        if mode_capture:
            server.listen_media()
        server.loop()

    elif device_type == 'bird_raspberry':
        if mode_capture:
            #raise Exception("bird_raspberry + mode_capture: method not implemented")
            from src.ServerTelemetryAndMedia import ServerTelemetryAndMedia
            server = ServerTelemetryAndMedia()
        else:
            from src.ServerTelemetry import ServerTelemetry
            server = ServerTelemetry("bird_telemeter")
            server.connect()
        server.listen_commands()
        server.loop()

    elif device_type == 'simulation':
        from src.ServerSimulation import ServerSimulation
        server = ServerSimulation("simulation")
        server.connect()
        server.listen_telemetry()
        server.listen_commands()
        if mode_capture:
            server.listen_media()
        server.loop()

    else:
        raise Exception('No device selected')

    return server

