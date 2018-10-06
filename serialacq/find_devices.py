import sys
from glob import glob
import numpy as np
import serial

def find_serial_devices():
    '''
    Detects platform and generates a list of serial ports
    Based on code from lightscalar/livestream repo
    '''
    if sys.platform.startswith("win"):
        ports = ["COM{}".format((i + 1)) for i in range(256)]
    elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
        # this excludes your current terminal "/dev/tty"
        ports = glob("/dev/tty[A-Za-z]*")
    elif sys.platform.startswith("darwin"):
        ports = glob("/dev/tty.usbmodem*")
    else:
        raise EnvironmentError("Unsupported platform")

    if not ports:
        raise EnvironmentError("No USB device detected")
    else:
        return ports
