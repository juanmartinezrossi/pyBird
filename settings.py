
#primary parameters
device_type = 'ground_station' #options: ground_station, bird_raspberry
mode_capture = True
mode_simulation = True
usb_comm_port = 9

#secondary parameters (do not edit)
simulated_device_type = None
comm_network = None

#conditional parameters (do not edit)
if mode_simulation:
    comm_network = 'local'
    if device_type == 'ground_station':
        simulated_device_type = 'bird_raspberry'
    elif device_type == 'bird_raspberry':
        simulated_device_type == 'ground_station'
if not mode_simulation:
    comm_network = 'remote'

