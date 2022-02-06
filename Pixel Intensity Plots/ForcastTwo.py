from math import floor
from random import gauss
import numpy as np

from astropy.io import fits
from astropy.convolution import Gaussian2DKernel, convolve, interpolate_replace_nans, convolve_fft

import sys
sys.path.append('./modules/')

import stars as st
import filetree as ft
file1 = st.isoTwo

parent = ft.FitsFolder()

from convolutions import ConvolveShift

file = parent + 'ForcastTwo/'
# Star A
path = file + 'A/'
x1 = file1.A.x1
y1 = file1.A.y1
oneAcollims = [350, 410, 0, 0.1] ## columnlimits = [xmin, xmax, ymin, ymax]
oneArowlims = [240, 310, None, 0.05] ## rowlimits = [xmin, xmax, ymin, ymax]
# ConvolveShift(path, x1, y1, 0.00, 0.005)



# Star B 
path = file + 'B/'
x1 = file1.B.x1
y1 = file1.B.y1
oneBcollims = [340, 400, 0, 0.6]
oneBrowlims = [300, 380, 0, 0.5]
# ConvolveShift(path, x1, y1, 0.0, 0.000)


# Star C
path = file + 'C/'
x1 = file1.C.x1
y1 = file1.C.y1
oneCcollims = [400, 440, 0, 0.045]
oneCrowlims = [400, 440, 0, 0.035]
ConvolveShift(path, x1, y1, 0.001, 0.005, oneCcollims, oneCrowlims)