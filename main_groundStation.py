from src import ServerFactory
from src.ServerFactory import build

from src import UIFactory
from src.UIFactory import build

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
    ui.server = server
except Exception as err:
    exit(1)

