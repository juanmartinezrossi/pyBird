from src.Device import Device
from settings import connection_string, connection_baud
from dronekit import *
from pymavlink import mavutil


class DeviceBirdRaspberry(Device):
    def __init__(self):
        self.vehicle = None
        self.speed = 10

    def handle_message_and_get_response(self, message: str):
        response = ''
        message_vector = message.split(";")
        if message_vector[0] == "Connect":
            response = self.connect()
        elif message_vector[0] == "Arm":
            response = self.arm()
        elif message_vector[0] == "RTL":
            response = self.returnToLaunch()
        elif message_vector[0] == "TakeOff":
            response = self.takeOff(int(message_vector[1]))
        elif message_vector[0] == "ApplySpeed":
            response = self.applySpeed(int(message_vector[1]))
        elif message_vector[0] == "N":
            response = self.goN()
        elif message_vector[0] == "W":
            response = self.goW()
        elif message_vector[0] == "S":
            response = self.goS()
        elif message_vector[0] == "E":
            response = self.goE()
        elif message_vector[0] == "NW":
            response = self.goNW()
        elif message_vector[0] == "NE":
            response = self.goNE()
        elif message_vector[0] == "SE":
            response = self.goSE()
        elif message_vector[0] == "SW":
            response = self.goSW()
        elif message_vector[0] == "Stop":
            response = self.stop()
        else:
            print(f"Unknown command: {message_vector[0]}")
        return response


    def connect(self):
        print(f"Connecting with connection_string: {connection_string}, baud = {connection_baud}")
        self.vehicle = connect(connection_string, wait_ready=False, baud=connection_baud)
        self.vehicle.wait_ready(True, timeout=5000)
        return 'Connected'
        # responder que está conectado

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
        return 'Armed'

    def takeOff(self, altitude: int):
        self.vehicle.simple_takeoff(altitude)
        while True:
            print(" Altitude: ", self.vehicle.location.global_relative_frame.alt)
            # Break and return from function just below target altitude.
            if self.vehicle.location.global_relative_frame.alt >= altitude * 0.95:
                print("Reached target altitude")
                break
            time.sleep(1)
        return 'Reached'

    def returnToLaunch(self):
        print("Return to land at maximum speed...")
        self.vehicle.mode = VehicleMode("RTL")
        return 'Returning'

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
        return ''

    def goN(self):
        cmd = self.prepare_command(self.speed, 0, 0)
        self.vehicle.send_mavlink(cmd)
        return ''

    def goS(self):
        cmd = self.prepare_command(-self.speed, 0, 0)
        self.vehicle.send_mavlink(cmd)
        return ''

    def goE(self):
        cmd = self.prepare_command(0, self.speed, 0)
        self.vehicle.send_mavlink(cmd)
        return ''

    def goW(self):
        cmd = self.prepare_command(0, -self.speed, 0)
        self.vehicle.send_mavlink(cmd)
        return ''

    def goNW(self):
        cmd = self.prepare_command(self.speed, -self.speed, 0)
        self.vehicle.send_mavlink(cmd)
        return ''

    def goSW(self):
        cmd = self.prepare_command(-self.speed, -self.speed, 0)  # NORTH
        self.vehicle.send_mavlink(cmd)
        return ''

    def goNE(self):
        cmd = self.prepare_command(self.speed, self.speed, 0)
        self.vehicle.send_mavlink(cmd)
        return ''

    def goSE(self):
        cmd = self.prepare_command(-self.speed, self.speed, 0)  # NORTH
        self.vehicle.send_mavlink(cmd)
        return ''

    def applySpeed(self, speed: int):
        self.speed = speed
        print(" Speed: ", self.speed)
        return ''

