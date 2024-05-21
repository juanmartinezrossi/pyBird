from settings import *
from src import Device


def build() -> Device:
    if device_type == 'ground_station':
        from src.DeviceGroundStation import DeviceGroundStation
        device = DeviceGroundStation()
    elif device_type == 'bird_raspberry':
        if mode_capture:
            from src.DeviceBirdRaspiCam import DeviceBirdRaspiCam
            device = DeviceBirdRaspiCam()
        else:
            from src.DeviceBirdRaspberry import DeviceBirdRaspberry
            device = DeviceBirdRaspberry()
    elif device_type == 'simulation':
        from src.DeviceSimulation import DeviceSimulation
        device = DeviceSimulation()
    else:
        raise Exception('No device selected')

    return device
