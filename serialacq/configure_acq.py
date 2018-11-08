import numpy as np
from collections import deque
import datetime

def gen_filename():
    fname = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S.csv")
    return fname

def init_savefile(folderpath):
    fname = folderpath + '/' + gen_filename()
    outfile = open(fname,'a')
    outfile.write('chan,value,time\n')
    return outfile

def write_data(outfile, c, v, t):
    outfile.write('{},{},{}\n'.format(c, v, t))
