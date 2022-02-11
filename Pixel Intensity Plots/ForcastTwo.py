
from astropy.io import fits
from astropy.convolution import Gaussian2DKernel, convolve, interpolate_replace_nans, convolve_fft

import sys
sys.path.append('./Pixel Intensity Plots/modules/')

import stars as st
import filetree as ft
file1 = st.isoTwo
sofia = file1.sofia
spit = file1.spitzer

parent = ft.FitsFolder()

from convolutions import ConvolveShift

file = parent + 'ForcastTwo/'
# Star A
path = file + 'A/'
x1 = file1.A.x1
y1 = file1.A.y1
oneAcollims = [350, 450, 0, 0.1] ## columnlimits = [xmin, xmax, ymin, ymax]
oneArowlims = [300, 360, None, 0.08] ## rowlimits = [xmin, xmax, ymin, ymax]
# ConvolveShift(sofia, spit, path, x1, y1, 0.005, 0.012, oneAcollims, oneArowlims)



# Star B 
path = file + 'B/'
x1 = file1.B.x1
x2 = file1.B.x2
y1 = file1.B.y1
y2 = file1.B.y2
oneBcollims = [y1 - 50, y2, 0, .3]
oneBrowlims = [x1 - 50, x2, 0, .3]
# ConvolveShift(sofia, spit, path, x1, y1, 0.001, 0.0095, oneBcollims, oneBrowlims, increment=0.005)


# Star C
path = file + 'C/'
x1 = file1.C.x1
x2 = file1.C.x2
y1 = file1.C.y1
y2 = file1.C.y2
oneCcollims = [y1 - 50, y2, 0, 0.045]
oneCrowlims = [x1 - 50, x2, 0, 0.035]
# ConvolveShift(sofia, spit, path, x1, y1, 0.005, 0.0075, oneCcollims, oneCrowlims, increment=.005)

# Star D
path = file + 'D/'
ft.FolderCheck('D/', True)
x1 = file1.D.x1
x2 = file1.D.x2
y1 = file1.D.y1
y2 = file1.D.y2
oneCcollims = [y1 - 50, y2, 0, 0.045]
oneCrowlims = [x1 - 50, x2, 0, 0.035]
# ConvolveShift(sofia, spit, path, x1, y1, -0.001, 0.008, oneCcollims, oneCrowlims)