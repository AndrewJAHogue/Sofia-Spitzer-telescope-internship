from math import floor

import sys
sys.path.append('./Pixel Intensity Plots/modules/')

import stars as st

import filetree as ft
file1 = st.isoOne
parent = ft.FitsFolder()
sofia = file1.sofia
spit = file1.spitzer


    # sofia = fitsfolder + "/Forcast25_isoField1.fits"
    # spit = fitsfolder + "/Reprojected Spitzer24 IsoFields @ Forcast25 isoField1.fits"

from convolutions import ConvolveShift

# Star A
oneAcollims = [390, 410, 0, 0.05] ## columnlimits = [xmin, xmax, ymin, ymax]
oneArowlims = [240, 310, None, 0.05] ## rowlimits = [xmin, xmax, ymin, ymax]
# ConvolveShift(path, x1, y1, oneBcollims, oneBrowlims, 0.01, 0.005)



# Star B 
path = parent + 'ForcastOne/B/'
x1 = file1.B.x1
y1 = file1.B.y1
oneBcollims = [340, 400, 0, 0.6]
oneBrowlims = [300, 380, 0, 0.5]
# ConvolveShift(path, x1, y1, 0.0, 0.007, oneBcollims, oneBrowlims)


# Star C
path = parent + 'ForcastOne/C/'
x1 = file1.C.x1
y1 = file1.C.y1
oneCcollims = [400, 440, 0, 0.045]
oneCrowlims = [400, 440, 0, 0.035]
ConvolveShift(sofia, spit, path, x1, y1, -.9, 0.0075, oneCcollims, oneCrowlims)