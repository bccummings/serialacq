import sys
from glob import glob
import numpy as np
import serial

from find_devices import find_serial_devices
from devices.biomonitor import Biomonitor

if __name__ == '__main__':
    ports = find_serial_devices()

    device = Biomonitor(ports[0])
    c, v, t = device.parse_input()
    print(c, v, t)
