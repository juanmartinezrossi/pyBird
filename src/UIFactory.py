from settings import *
from src import UI
from src import Server


def build(server: Server) -> UI:
    if device_type == 'ground_station':
        if mode_capture:
            #from src.UIStationCapture import UIStationCapture
            #ui = UIStationCapture()
            print("Method not implemented")
            pass
        else:
            #interfaz fase 1
            from src.UIStation import UIStation
            ui = UIStation(ui_title, ui_geometry, server)

    elif device_type == 'bird_raspberry':
        from src.UIDummy import UIDummy
        ui = UIDummy('', '')

    elif device_type == 'simulation':
        if mode_capture:
            #from src.UIStationCapture import UIStationCapture
            #ui = UIStationCapture()
            print("Method not implemented")
            pass
        else:
            #interfaz fase 1
            from src.UIStation import UIStation
            ui = UIStation(ui_title, ui_geometry, server)
    else:
        raise Exception('No device selected')

    return ui
