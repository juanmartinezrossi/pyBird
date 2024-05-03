import time
from abc import abstractmethod


class Server:
    def __init__(self):
        self.commNetwork = None

    def config(self):
        pass