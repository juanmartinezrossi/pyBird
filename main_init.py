import argparse
import logging
from datetime import timedelta, datetime
from src.UIFactory import build as ui_build

import settings
from settings import *

if __name__ == "__main__":
    # Build UI
    ui = None
    try:
        ui = ui_build()
    except Exception as err:
        exit(1)
