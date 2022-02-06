## this file is meant as a quick way to run python commands, for whatever project I'm doing. Anything I want to keep needs to be saved in its own file

# import numpy as np
# import matplotlib.pyplot as plt
from astropy.io import fits

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
import filetree as ft
file1 = st.isoOne
# x2 = file1.A.x2
# y2 = file1.A.y2
parent = ft.FitsFolder()

from convolutions import ConvolveShift

# Star A
path = parent + 'ForcastOne/A/'
x1 = file1.A.x1
y1 = file1.A.y1
oneAcollims = [390, 410, 0, 0.05] ## columnlimits = [xmin, xmax, ymin, ymax]
oneArowlims = [240, 310, None, 0.05] ## rowlimits = [xmin, xmax, ymin, ymax]
ConvolveShift(path, x1, y1, 0.01, 0.01, oneAcollims, oneArowlims)
ConvolveShift(path, x1, y1, 0.001, 0.005, oneAcollims, oneArowlims)
import matplotlib.pyplot as plt

plt.show()
