import time
from abc import abstractmethod
import socket
import tkinter as tk
from settings import ui_internal_port


class UI:
    def __init__(self, title: str, geometry: str):
        #print("inicializando UI")
        self.title = title
        self.geometry = geometry
        self.master = tk.Tk()
        self.master.title(self.title)
        self.master.geometry(self.geometry)
        #print("geometry applied")
        #print("UI inicializada")

    @abstractmethod
    def buildFrame(self, fatherframe: tk):
        self.frame = fatherframe
        return self.frame

