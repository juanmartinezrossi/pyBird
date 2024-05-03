from settings import *
from src import UI
import tkinter as tk

def build() -> UI:
    if device_type == 'ground_station':
        if mode_capture:
            from src.UIStationCapture import UIStationCapture
            ui = UIStationCapture()
        else:
            title = "Little ground station"
            geometry = "300x400"
            from src.UIStation import UIStation
            ui = UIStation(title, geometry)
    elif device_type == 'bird_raspberry':
        from src.UIDummy import UIDummy
        ui = UIDummy()
    else:
        raise Exception('No device selected')

    return ui