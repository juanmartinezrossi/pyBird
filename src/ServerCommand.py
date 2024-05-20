from src.Server import Server
from settings import mode_capture, ui_internal_port
import socket


class ServerCommand(Server):
    def __init__(self, clientName: str):
        super().__init__(clientName)

    def send_command(self, *args: str):
        message = ';'.join(args)
        self.send_message("Command", message)

    def listen_telemetry(self):
        self.subscribe_to_topic("Telemetry")

    def listen_media(self):
        self.subscribe_to_topic("Media")

    def internal_istener(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', ui_internal_port))
            s.listen()
            try:
                while True:
                    conn, addr = s.accept()
                    with conn:
                        print('Connected by', addr)
                        while True:
                            data = conn.recv(1024)
                            if not data:
                                break
                            # Process the received data (split into topic and message)
                            message = data.decode().split(':')
                            print(f"Received message from topic '{topic}': {message}")
            except KeyboardInterrupt:
                print("\nServer is shutting down...")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                s.close()
                print("Socket closed.")

