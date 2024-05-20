from src import ServerFactory
from src.ServerFactory import build
import time, socket

from src import UIFactory
from src.UIFactory import build

# init settings
from settings import server_internal_port

# build server
server = None
try:
    server = ServerFactory.build()
except Exception as err:
    exit(1)

# build UI
ui = None
try:
    ui = UIFactory.build(server)
    ui.server = server
except Exception as err:
    exit(1)

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
    except KeyboardInterrupt:
        print("\nServer is shutting down...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        s.close()
        print("Socket closed.")




