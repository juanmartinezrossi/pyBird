from settings import *
from src import Device


def build() -> Device:
    if device_type == 'ground_station':
        from src.DeviceGroundStation import DeviceGroundStation
        device = DeviceGroundStation()
    elif device_type == 'bird_raspberry':
        from src.DeviceBirdRaspberry import DeviceBirdRaspberry
        device = DeviceBirdRaspberry()
    else:
        raise Exception('No device selected')

    return device
