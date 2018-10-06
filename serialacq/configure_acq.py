import numpy as np
from collections import deque
from time import time

def init_savefile(fname):
    with open(fname,'a') as outfile:
        outfile.write('chan,value,time')

def write_data(fname, c, v, t):
    with open(fname, 'a') as outfile:
        outfile.write('{},{},{}'.format(c, v, t))
