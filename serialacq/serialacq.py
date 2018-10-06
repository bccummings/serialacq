import sys
from glob import glob
import numpy as np
import serial

from find_devices import find_serial_devices

if __name__ == '__main__':
    ports = find_serial_devices()
    print(ports)
