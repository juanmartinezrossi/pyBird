# primary parameters
device_type = 'ground_station'  # options: ground_station, bird_raspberry, simulation
comm_network = 'local '  # options: 'local', 'remote'
mode_capture = False
drone_available = True
usb_comm_port = 9
connection_baud = 115200  # options: '115200' (local), '57600' (usb and udp->usb)
connection_string = '/dev/ttyS0'  # options: 'tcp:127.0.0.1:5763', f'com{usb_comm_port}', 'udp:127.0.0.1:14550', '/dev/ttyS0'
# if connection_string is udp, execute in Windows powershell:
# mavproxy --master=com9 --out=udp:127.0.0.1:14550 --out= udp:127.0.0.1:14551
server_broker_address = "broker.hivemq.com"
server_broker_port = 1883
server_internal_port = 1880
ui_internal_port = 1881
capture_storage_path = './storage/capture'


# secondary parameters (do not edit)
ui_title = "pyBird Ground Station"
ui_geometry = "600x600"
