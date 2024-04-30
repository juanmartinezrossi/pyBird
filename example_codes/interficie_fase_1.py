import tkinter as tk
from dronekit import *
import time
from pymavlink import mavutil


class ControlFrame:
    def buildFrame(self, fatherFrame):
        self.controlFrame = tk.LabelFrame(fatherFrame, text="Control")

        self.controlFrame.rowconfigure(0, weight=1)
        self.controlFrame.rowconfigure(1, weight=1)
        self.controlFrame.rowconfigure(2, weight=3)
        self.controlFrame.rowconfigure(3, weight=1)
        self.controlFrame.rowconfigure(4, weight=1)
        self.controlFrame.rowconfigure(5, weight=1)

        self.controlFrame.columnconfigure(0, weight=1)
        self.controlFrame.columnconfigure(1, weight=1)

        self.connectButton = tk.Button(self.controlFrame, text="Connect",
                                       bg='red', fg="white", command=self.connect)
        self.connectButton.grid(row=0, column=0, columnspan=2, padx=5, pady=5,
                                sticky=tk.N + tk.S + tk.E + tk.W)

        self.armButton = tk.Button(self.controlFrame, text="Arm",
                                   bg='red', fg="white", command=self.arm)
        self.armButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5,
                            sticky=tk.N + tk.S + tk.E + tk.W)

        self.altitude = tk.Entry(self.controlFrame)
        self.altitude.grid(row=2, column=0, padx=5, pady=5,
                           sticky=tk.N + tk.S + tk.E + tk.W)

        self.takeOffButton = tk.Button(self.controlFrame, text="TakeOff",
                                       bg='red', fg="white", command=self.takeOff)
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
                                  bg='#FFBB00', fg="black", command=self.goNW)
        self.NWButton.grid(row=0, column=0, padx=5, pady=5,
                           sticky=tk.N + tk.S + tk.E + tk.W)

        self.NButton = tk.Button(self.buttonsFrame, text="N", width=3,
                                 bg='#FFBB00', fg="black", command=self.goN)
        self.NButton.grid(row=0, column=1, padx=5, pady=5,
                          sticky=tk.N + tk.S + tk.E + tk.W)

        self.NEButton = tk.Button(self.buttonsFrame, text='\u2B08', width=3,
                                  bg='#FFBB00', fg="black", command=self.goNE)
        self.NEButton.grid(row=0, column=2, padx=5, pady=5,
                           sticky=tk.N + tk.S + tk.E + tk.W)

        self.WButton = tk.Button(self.buttonsFrame, text="W", width=3,
                                 bg='#FFBB00', fg="black", command=self.goW)
        self.WButton.grid(row=1, column=0, padx=5, pady=5,
                          sticky=tk.N + tk.S + tk.E + tk.W)

        self.StopButton = tk.Button(self.buttonsFrame, text="Stop", width=3,
                                    bg='#FFBB00', fg="black", command=self.stop)
        self.StopButton.grid(row=1, column=1, padx=5, pady=5,
                             sticky=tk.N + tk.S + tk.E + tk.W)

        self.EButton = tk.Button(self.buttonsFrame, text="E", width=3,
                                 bg='#FFBB00', fg="black", command=self.goE)
        self.EButton.grid(row=1, column=2, padx=5, pady=5,
                          sticky=tk.N + tk.S + tk.E + tk.W)

        self.SWButton = tk.Button(self.buttonsFrame, text='\u2B0B', width=3,
                                  bg='#FFBB00', fg="black", command=self.goSW)
        self.SWButton.grid(row=2, column=0, padx=5, pady=5,
                           sticky=tk.N + tk.S + tk.E + tk.W)

        self.SButton = tk.Button(self.buttonsFrame, text="S", width=3,
                                 bg='#FFBB00', fg="black", command=self.goS)
        self.SButton.grid(row=2, column=1, padx=5, pady=5,
                          sticky=tk.N + tk.S + tk.E + tk.W)

        self.SEButton = tk.Button(self.buttonsFrame, text='\u2B0A', width=3,
                                  bg='#FFBB00', fg="black", command=self.goSE)
        self.SEButton.grid(row=2, column=2, padx=5, pady=5,
                           sticky=tk.N + tk.S + tk.E + tk.W)

        self.RTLButton = tk.Button(self.controlFrame, text="RTL",
                                   bg='red', fg="white", command=self.returnToLaunch)
        self.RTLButton.grid(row=5, column=0, columnspan=2, padx=5, pady=5,
                            sticky=tk.N + tk.S + tk.E + tk.W)

        self.speedInput = tk.Entry(self.controlFrame)
        self.speedInput.grid(row=4, column=0, padx=5, pady=5,
                           sticky=tk.N + tk.S + tk.E + tk.W)

        self.speedButton = tk.Button(self.controlFrame, text="ApplySpeed",
                                     bg='red', fg='white', command=self.applySpeed)
        self.speedButton.grid(row=4,  column=1, padx=5, pady=5,
                                sticky=tk.N + tk.S + tk.E + tk.W)

        self.speed = 10
        self.vehicle = None
        return self.controlFrame

    def connect(self):
        connection_string = "tcp:127.0.0.1:5763"
        self.vehicle = connect(connection_string, wait_ready=False, baud=115200)


        # connection_string = "com7"
        # self.vehicle = connect(connection_string, wait_ready=False, baud=57600)

        self.vehicle.wait_ready(True, timeout=5000)

        self.connectButton['bg'] = 'green'
        self.connectButton['text'] = 'connected'


    def arm(self):
        """ Arms vehicle and fly to aTargetAltitude. """
        print("Basic pre-arm checks")  # Don't try to arm until autopilot is ready
        while not self.vehicle.is_armable:
            print(" Waiting for vehicle to initialise...")
            time.sleep(1)
        print("Arming motors")
        # Copter should arm in GUIDED mode
        self.vehicle.mode = VehicleMode("GUIDED")
        self.vehicle.armed = True
        # Confirm vehicle armed before attempting to take off
        while not self.vehicle.armed:
            print(" Waiting for arming...")
            time.sleep(1)


        self.armButton['bg'] = 'green'
        self.armButton['text'] = 'armed'


    def takeOff(self):
        altitude = int(self.altitude.get())
        self.vehicle.simple_takeoff(altitude)
        while True:
            print(" Altitude: ", self.vehicle.location.global_relative_frame.alt)
            # Break and return from function just below target altitude.
            if self.vehicle.location.global_relative_frame.alt >= altitude * 0.95:
                print("Reached target altitude")
                break
            time.sleep(1)


        self.takeOffButton['bg'] = 'green'
        self.takeOffButton['text'] = 'flying'


    def returnToLaunch(self):
        print("Return to land at maximum speed...")
        self.vehicle.mode = VehicleMode("RTL")


        while self.vehicle.armed:
            time.sleep(1)
            self.armButton['bg'] = 'red'
            self.armButton['text'] = 'Arm'
        self.takeOffButton['bg'] = 'red'
        self.takeOffButton['text'] = 'TakeOff'


    def prepare_command(self, velocity_x, velocity_y, velocity_z):
        """
        Move vehicle in direction based on specified velocity vectors.
        """
        msg = self.vehicle.message_factory.set_position_target_local_ned_encode(
            0,  # time_boot_ms (not used)
            0,
            0,  # target system, target component
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,  # frame
            0b0000111111000111,  # type_mask (only speeds enabled)
            0,
            0,
            0,  # x, y, z positions (not used)
            velocity_x,
            velocity_y,
            velocity_z,  # x, y, z velocity in m/s
            0,
            0,
            0,  # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
            0,
            0,
        )  # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

        return msg


    def stop(self):
        cmd = self.prepare_command(0, 0, 0)  # stop
        self.vehicle.send_mavlink(cmd)


        self.markDirection('Stop')


    def goN(self):
        cmd = self.prepare_command(self.speed, 0, 0)
        self.vehicle.send_mavlink(cmd)
        self.markDirection('N')


    def goS(self):
        cmd = self.prepare_command(-self.speed, 0, 0)
        self.vehicle.send_mavlink(cmd)
        self.markDirection('S')


    def goE(self):
        cmd = self.prepare_command(0, self.speed, 0)
        self.vehicle.send_mavlink(cmd)
        self.markDirection('E')


    def goW(self):
        cmd = self.prepare_command(0, -self.speed, 0)
        self.vehicle.send_mavlink(cmd)
        self.markDirection('W')


    def goNW(self):
        cmd = self.prepare_command(self.speed, -self.speed, 0)
        self.vehicle.send_mavlink(cmd)
        self.markDirection('NW')


    def goSW(self):
        cmd = self.prepare_command(-self.speed, -self.speed, 0)  # NORTH
        self.vehicle.send_mavlink(cmd)
        self.markDirection('SW')


    def goNE(self):
        cmd = self.prepare_command(self.speed, self.speed, 0)
        self.vehicle.send_mavlink(cmd)
        self.markDirection('NE')


    def goSE(self):
        cmd = self.prepare_command(-self.speed, self.speed, 0)  # NORTH
        self.vehicle.send_mavlink(cmd)
        self.markDirection('SE')

    def applySpeed(self):
        self.speed = int(self.speedInput.get())
        print(" Speed: ", self.speed)
        self.speedButton['bg'] = 'green'
        self.speedButton['text'] = 'applied'
        time.sleep(1)
        self.speedButton['bg'] = 'red'
        self.speedButton['text'] = 'ApplySpeed'


    def markDirection(self, direction):


        self.NWButton['bg'] = '#FFBB00'
        self.NButton['bg'] = '#FFBB00'
        self.NEButton['bg'] = '#FFBB00'
        self.WButton['bg'] = '#FFBB00'
        self.StopButton['bg'] = '#FFBB00'
        self.EButton['bg'] = '#FFBB00'
        self.SWButton['bg'] = '#FFBB00'
        self.SButton['bg'] = '#FFBB00'
        self.SEButton['bg'] = '#FFBB00'

        if direction == 'NW':
            self.NWButton['bg'] = 'darkOrange'
        if direction == 'N':
            self.NButton['bg'] = 'darkOrange'
        if direction == 'NE':
            self.NEButton['bg'] = 'darkOrange'
        if direction == 'W':
            self.WButton['bg'] = 'darkOrange'
        if direction == 'Stop':
            self.StopButton['bg'] = 'darkOrange'
        if direction == 'E':
            self.EButton['bg'] = 'darkOrange'
        if direction == 'SW':
            self.SWButton['bg'] = 'darkOrange'
        if direction == 'S':
            self.SButton['bg'] = 'darkOrange'
        if direction == 'SE':
            self.SEButton['bg'] = 'darkOrange'

master = tk.Tk()
master.title("Little ground station")
master.geometry("300x400")
confPanel = ControlFrame()
confPanelFrame = confPanel.buildFrame(master)
confPanelFrame.pack()
master.mainloop()
