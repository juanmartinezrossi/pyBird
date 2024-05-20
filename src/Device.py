import time
from abc import abstractmethod


class Device:
    def __init__(self):
        pass

    @abstractmethod
    def handle_message_and_get_response(self) -> str:
        pass

