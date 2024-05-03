from settings import *
from src import Server


def build() -> Server:
    if device_type == 'ground_station':
        pass
    elif device_type == 'bird_raspberry':
        pass
    else:
        raise Exception('No device selected')

    return None
