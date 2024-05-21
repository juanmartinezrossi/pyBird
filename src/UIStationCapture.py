import tkinter as tk
from tkinter import *
from dronekit import *
import time
from pymavlink import mavutil
from PIL import Image
from PIL import ImageTk

from src.UI import UI
from src.Server import Server
from src.ServerCommand import ServerCommand

class UIStationCapture(UI):
    def __init__(self,title: str, geometry: str, server: ServerCommand):
        self.title = title
        self.geometry = geometry
        self.master = tk.Tk()
        self.master.title(self.title)
        self.master.geometry(self.geometry)
        self.server = server
        self.uiFrame = self.buildFrame(self.master)
        self.uiFrame.pack()
        self.master.mainloop()

    def buildFrame(self, fatherFrame: tk):
        self.controlFrame = tk.LabelFrame(fatherFrame, text="Control and Capture")

        self.controlFrame.rowconfigure(0, weight=1)
        self.controlFrame.rowconfigure(1, weight=1)
        self.controlFrame.rowconfigure(2, weight=3)
        self.controlFrame.rowconfigure(3, weight=1)
        self.controlFrame.rowconfigure(4, weight=1)
        self.controlFrame.rowconfigure(5, weight=1)
        self.controlFrame.rowconfigure(6, weight=1)

        self.controlFrame.columnconfigure(0, weight=1)
        self.controlFrame.columnconfigure(1, weight=1)
        self.controlFrame.columnconfigure(2, weight=1)
        self.controlFrame.columnconfigure(3, weight=3)

        self.startCaptureButton = tk.Button(self.controlFrame, text="Start Capture",
                                           bg="blue", fg="white", command=self.command_start_capture)
        self.startCaptureButton.grid(row=0, column=2, columnspan=2, padx=30, pady=5)

        self.stopCaptureButton = tk.Button(self.controlFrame, text="Stop Capture",
                                            bg="blue", fg="white", command=self.command_stop_capture)
        self.stopCaptureButton.grid(row=1, column=2, columnspan=2, padx=30, pady=5)

        self.takePictureButton = tk.Button(self.controlFrame, text="Take Picture",
                                           bg="blue", fg="white", command=self.command_take_picture)
        self.takePictureButton.grid(row=2, column=2, columnspan=2, padx=30, pady=5)

        self.picturePanel = Canvas(self.controlFrame)
        self.picturePanel.grid(row=6, column=3, columnspan=2)

        self.connectButton = tk.Button(self.controlFrame, text="Connect",
                                       bg='blue', fg="white", command=self.command_connect)
        self.connectButton.grid(row=0, column=0, columnspan=2, padx=5, pady=5,
                                sticky=tk.N + tk.S + tk.E + tk.W)

        self.armButton = tk.Button(self.controlFrame, text="Arm",
                                   bg='blue', fg="white", command=self.command_arm)
        self.armButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5,
                            sticky=tk.N + tk.S + tk.E + tk.W)

        self.altitude = tk.Entry(self.controlFrame)
        self.altitude.grid(row=2, column=0, padx=5, pady=5,
                           sticky=tk.N + tk.S + tk.E + tk.W)

        self.takeOffButton = tk.Button(self.controlFrame, text="TakeOff",
                                       bg='blue', fg="white", command=self.command_takeoff)
        self.takeOffButton.grid(row=2, column=1, padx=5, pady=5,
                                sticky=tk.N + tk.S + tk.E + tk.W)

        self.buttonsFrame = tk.LabelFrame(self.controlFrame, text='go')
        self.buttonsFrame.grid(row=3, column=0, columnspan=2, padx=15, pady=5)
        self.buttonsFrame.rowconfigure(0, weight=1)
        self.buttonsFrame.rowconfigure(1, weight=1)
        self.buttonsFrame.rowconfigure(2, weight=1)

        self.buttonsFrame.columnconfigure(0, weight=1)
        self.buttonsFrame.columnconfigure(1, weight=1)
        self.buttonsFrame.columnconfigure(2, weight=1)

        self.NWButton = tk.Button(self.buttonsFrame, text='\u2B09', width=3,
                                  bg='#FFBB00', fg="black", command=self.command_goNW)
        self.NWButton.grid(row=0, column=0, padx=5, pady=5,
                           sticky=tk.N + tk.S + tk.E + tk.W)

        self.NButton = tk.Button(self.buttonsFrame, text="N", width=3,
                                 bg='#FFBB00', fg="black", command=self.command_goN)
        self.NButton.grid(row=0, column=1, padx=5, pady=5,
                          sticky=tk.N + tk.S + tk.E + tk.W)

        self.NEButton = tk.Button(self.buttonsFrame, text='\u2B08', width=3,
                                  bg='#FFBB00', fg="black", command=self.command_goNE)
        self.NEButton.grid(row=0, column=2, padx=5, pady=5,
                           sticky=tk.N + tk.S + tk.E + tk.W)

        self.WButton = tk.Button(self.buttonsFrame, text="W", width=3,
                                 bg='#FFBB00', fg="black", command=self.command_goW)
        self.WButton.grid(row=1, column=0, padx=5, pady=5,
                          sticky=tk.N + tk.S + tk.E + tk.W)

        self.StopButton = tk.Button(self.buttonsFrame, text="Stop", width=3,
                                    bg='#FFBB00', fg="black", command=self.command_stop)
        self.StopButton.grid(row=1, column=1, padx=5, pady=5,
                             sticky=tk.N + tk.S + tk.E + tk.W)

        self.EButton = tk.Button(self.buttonsFrame, text="E", width=3,
                                 bg='#FFBB00', fg="black", command=self.command_goE)
        self.EButton.grid(row=1, column=2, padx=5, pady=5,
                          sticky=tk.N + tk.S + tk.E + tk.W)

        self.SWButton = tk.Button(self.buttonsFrame, text='\u2B0B', width=3,
                                  bg='#FFBB00', fg="black", command=self.command_goSW)
        self.SWButton.grid(row=2, column=0, padx=5, pady=5,
                           sticky=tk.N + tk.S + tk.E + tk.W)

        self.SButton = tk.Button(self.buttonsFrame, text="S", width=3,
                                 bg='#FFBB00', fg="black", command=self.command_goS)
        self.SButton.grid(row=2, column=1, padx=5, pady=5,
                          sticky=tk.N + tk.S + tk.E + tk.W)

        self.SEButton = tk.Button(self.buttonsFrame, text='\u2B0A', width=3,
                                  bg='#FFBB00', fg="black", command=self.command_goSE)
        self.SEButton.grid(row=2, column=2, padx=5, pady=5,
                           sticky=tk.N + tk.S + tk.E + tk.W)

        self.RTLButton = tk.Button(self.controlFrame, text="RTL",
                                   bg='blue', fg="white", command=self.command_RTL)
        self.RTLButton.grid(row=5, column=0, columnspan=2, padx=5, pady=5,
                            sticky=tk.N + tk.S + tk.E + tk.W)

        self.speedInput = tk.Entry(self.controlFrame)
        self.speedInput.grid(row=4, column=0, padx=5, pady=5,
                             sticky=tk.N + tk.S + tk.E + tk.W)

        self.speedButton = tk.Button(self.controlFrame, text="ApplySpeed",
                                     bg='blue', fg='white', command=self.command_apply_speed)
        self.speedButton.grid(row=4, column=1, padx=5, pady=5,
                              sticky=tk.N + tk.S + tk.E + tk.W)

        return self.controlFrame

    def command_start_capture(self):
        order = "StartCapture"
        self.server.send_command(order)

    def command_stop_capture(self):
        order = "StopCapture"
        self.server.send_command(order)

    def command_take_picture(self):
        order = "TakePicture"
        self.server.send_command(order)

    def get_altitude(self):
        return self.altitude

    def get_speed(self):
        return self.speedInput

    def command_connect(self):
        order = "Connect"
        self.server.send_command(order)

    def command_arm(self):
        order = "Arm"
        self.server.send_command(order)

    def command_RTL(self):
        order = "RTL"
        self.server.send_command(order)

    def command_takeoff(self):
        order = "TakeOff"
        altitude = self.altitude.get()
        self.server.send_command(order, altitude)

    def command_apply_speed(self):
        order = "ApplySpeed"
        speed = self.speedInput.get()
        self.server.send_command(order, speed)

    def command_goN(self):
        order = "N"
        self.server.send_command(order)

    def command_goW(self):
        order = "W"
        self.server.send_command(order)

    def command_goS(self):
        order = "S"
        self.server.send_command(order)

    def command_goE(self):
        order = "E"
        self.server.send_command(order)

    def command_goNW(self):
        order = "NW"
        self.server.send_command(order)

    def command_goNE(self):
        order = "NE"
        self.server.send_command(order)

    def command_goSE(self):
        order = "SE"
        self.server.send_command(order)

    def command_goSW(self):
        order = "SW"
        self.server.send_command(order)

    def command_stop(self):
        order = "Stop"
        self.server.send_command(order)

