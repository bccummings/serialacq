import sys
from glob import glob
import numpy as np
import serial

from find_ports import find_serial_devices
from devices.biomonitor import Biomonitor
from configure_acq import init_savefile, write_data

if __name__ == '__main__':
    ports = find_serial_devices()

    device = Biomonitor(ports[0])

    for i in range(15): # test
        c, v, t = device.parse_input()
