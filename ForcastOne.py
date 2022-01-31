from math import floor
from random import gauss
import numpy as np

from astropy.io import fits
from astropy.convolution import Gaussian2DKernel, convolve, interpolate_replace_nans, convolve_fft

import sys
sys.path.append('./modules/')

import stars as st

# file1 = st.isoOne
# x1 = file1.A.x1
# y1 = file1.A.y1
# print(f'x1: {x1} \ny1: {y1}')
# sofia = "../fits/Forcast25_isoField1.fits"
# spit = "../fits/Reprojected Spitzer24 IsoFields @ Forcast25 isoField1.fits"
# x2 = file1.A.x2
# y2 = file1.A.y2

file1 = st.isoOne
x1 = file1.C.x1
y1 = file1.C.y1
print(f'x1: {x1} \ny1: {y1}')
# x2 = file1.A.x2
# y2 = file1.A.y2
path = './fits/ForcastOne/B/'


# Star A
oneAcollims = [390, 410, 0, 0.05] ## columnlimits = [xmin, xmax, ymin, ymax]
oneArowlims = [240, 310, None, 0.05] ## rowlimits = [xmin, xmax, ymin, ymax]


from convolutions import ConvolveShift

# Star B 
oneBcollims = [390, 420, 0, 0.04]
oneBrowlims = [390, 440, 0, 0.04]
ConvolveShift(path, x1, y1, oneBcollims, oneBrowlims, 0.01, .001)