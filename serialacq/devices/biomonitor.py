import sys
import numpy as np
import serial

class Biomonitor():
    '''The biomonitor device'''

    def __init__(self, portID):
        '''Constructor'''
        self.port = portID
        self.baud_rate = 9600

        self.validate_input()

    def parse_input(self):
        '''Grab one line of input and parse it'''

        with serial.Serial(self.port, self.baud_rate) as ser:
            try:
                output = ser.readline().decode('utf-8')
                output = output.split(' ')

                channel_number = int(output[1])
                value = int(output[2], 16)
                timestamp = int(output[3], 16) * 1e-6
            except:
                pass

        return channel_number, value, timestamp

    def validate_input(self):
        '''
        Check to make sure we can read and interpret values from the board.
        Called during constructor function.
        '''

        try:
            c, v, t = self.parse_input()
            print('Connected to port {}'.format(self.port))

        except:
            print('Could not connect to biomonitor device')
