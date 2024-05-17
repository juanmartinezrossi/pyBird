
#primary parameters
device_type = 'ground_station' #options: ground_station, bird_raspberry, simulation
mode_capture = False
usb_comm_port = 9
connection_baud=115200 #options: '115200' (local), '57600' (usb)
connection_string = 'tcp:127.0.0.1:5763' #options: 'tcp:127.0.0.1:5763', f'com{usb_comm_port}'
server_broker_address="broker.hivemq.com"
server_broker_port=1883
server_internal_port=1880


#secondary parameters (do not edit)
simulated_device_type = None
comm_network = None
ui_title = "Little Ground Station"
ui_geometry = "300x400"

#conditional parameters (do not edit)
if device_type == 'simulation':
    comm_network = 'local'
else:
    comm_network = 'remote'

