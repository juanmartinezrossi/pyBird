from src import ServerFactory
from src.ServerFactory import build
from src import UIFactory
from src.UIFactory import build
from src import DeviceFactory
from src.DeviceFactory import build

import time, socket, threading

# init settings
from settings import server_internal_port

# build server
server = None
try:
    server = ServerFactory.build()
except Exception as e:
    print(f"An error occurred: {e}")

# build UI
ui = None
try:
    ui_thread = threading.Thread(target=UIFactory.build, args=(server,))
    ui_thread.daemon = True
    ui_thread.start()
except Exception as e:
    print(f"An error occurred: {e}")

# build device
device = None
try:
    device = DeviceFactory.build()
except Exception as e:
    print(f"An error occurred: {e}")


# listener
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', server_internal_port))
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
                    topic, message = data.decode().split(':')
                    print(f"Received message from topic '{topic}': {message}")
                    response = device.handle_message_and_get_response(message)
                    if response == '':
                        pass
                    else:
                        server.send_message("Telemetry", response)
    except KeyboardInterrupt:
        print("\nServer is shutting down...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        s.close()
        print("Socket closed.")




