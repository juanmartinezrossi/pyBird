from src import ServerFactory
from src.ServerFactory import build
import time, socket

from src import UIFactory
from src.UIFactory import build

from settings import server_internal_port

#build server
server = None
try:
    server = ServerFactory.build()
except Exception as err:
    exit(0)

#build UI
ui = None
try:
    ui = UIFactory.build(server)
except Exception as err:
    exit(1)

# init verification
if ui.server is server:
        print("ui.server is the same object as server")
    else:
        print("ui.server is not the same object as server")

#listener
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', server_internal_port))
    s.listen()
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



