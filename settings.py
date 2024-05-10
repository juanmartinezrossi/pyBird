
#primary parameters
device_type = 'bird_raspberry' #options: ground_station, bird_raspberry, simulation
mode_capture = False
usb_comm_port = 9
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

