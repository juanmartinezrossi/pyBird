from src import ServerFactory
from src.ServerFactory import build
import time, socket, select

from src import UIFactory
from src.UIFactory import build

# init settings
from settings import server_internal_port, ui_internal_port

# build internal sockets
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_ui = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind(('localhost', server_internal_port))
socket_ui.bind(('localhost', ui_internal_port))
socket_server.listen()
socket_ui.listen()
sockets_list = [socket_server, socket_ui]

# build server
server = None
try:
    server = ServerFactory.build()
except Exception as err:
    exit(1)

# build UI
ui = None
try:
    ui = UIFactory.build()
except Exception as err:
    exit(1)

# listener
try:
    while True:
        read_sockets, _, _ = select.select(sockets_list, [], [])
        for sock in read_sockets:
            conn, addr = sock.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    if sock == socket_server:
                        topic, message = data.decode().split(';')
                        print(f"Received message from topic '{topic}': {message}")
                    elif sock == socket_ui:


except KeyboardInterrupt:
    print("\nServer is shutting down...")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    socket_server.close()
    socket_ui.close()
    print("Sockets closed.")




