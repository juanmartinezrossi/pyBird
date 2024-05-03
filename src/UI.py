import time
from abc import abstractmethod
import tkinter as tk


class UI:
    def __init__(self, title: str, geometry: str):
        self.title = title
        self.geometry = geometry
        self.master = tk.Tk()
        self.master.title(self.title)
        self.master.geometry(self.geometry)
        self.uiFrame = self.buildFrame(self.master)
        self.uiFrame.pack()
        self.master.mainloop()

    @abstractmethod
    def buildFrame(self, fatherframe: tk):
        self.frame = fatherframe
        return self.frame