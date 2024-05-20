from src.Device import Device


class DeviceGroundStation(Device):
    def __init__(self):
        pass

    def handle_message_and_get_response(self, message: str):
        response = ''
        message_vector = message.split(";")
        if message_vector[0] == "Connected":
            print("The bird is CONNECTED")
        elif message_vector[0] == "Armed":
            print("The bird is ARMED")
        elif message_vector[0] == "Reached":
            print("Altitude Reached")
        elif message_vector[0] == "Returning":
            print("The bird is Returning to Land")
        else:
            print(f"Unknown command: {message_vector[0]}")
        return response



