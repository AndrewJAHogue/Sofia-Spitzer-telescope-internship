
from astropy.io import fits
from astropy.convolution import Gaussian2DKernel, convolve, interpolate_replace_nans, convolve_fft

import sys
sys.path.append('./Pixel Intensity Plots/modules/')

import stars as st
import filetree as ft
file1 = st.sgrb
sofia = file1.sofia
spit = file1.spitzer

parent = ft.FitsFolder()

from convolutions import ConvolveShift

file = parent + 'sgrb/'

# # Star A
# path = file + 'A/'
# ft.FolderCheck('sgrb/A', True)
# x1 = file1.A.x1
# x2 = file1.A.x2
# y1 = file1.A.y1
# y2 = file1.A.y2
# column_limits = [y1, y2, 0, None] ## columnlimits = [xmin, xmax, ymin, ymax]
# row_limits = [x1, x2, None, None] ## rowlimits = [xmin, xmax, ymin, ymax]
# ConvolveShift(sofia, spit, path, x1, y1, 0.000, 0.00, column_limits, row_limits)

# # Star B
# path = file + 'B/'
# ft.FolderCheck('sgrb/B', True)
# x1 = file1.B.x1
# x2 = file1.B.x2
# y1 = file1.B.y1
# y2 = file1.B.y2
# column_limits = [y1, y2, 0, None] ## columnlimits = [xmin, xmax, ymin, ymax]
# row_limits = [x1, x2, None, None] ## rowlimits = [xmin, xmax, ymin, ymax]
# ConvolveShift(sofia, spit, path, x1, y1, 0.000, 0.00, column_limits, row_limits)

# # # Star C
# path = file + 'C/'
# ft.FolderCheck('sgrb/C', True)
# x1 = file1.C.x1
# x2 = file1.C.x2
# y1 = file1.C.y1
# y2 = file1.C.y2
# column_limits = [y1 - 50, y2, 0, None] ## columnlimits = [xmin, xmax, ymin, ymax]
# row_limits = [x1 - 50, x2, None, None] ## rowlimits = [xmin, xmax, ymin, ymax]
# ConvolveShift(sofia, spit, path, x1, y1, 0.000, 0.00, column_limits, row_limits)

# # Star D
# path = file + 'D/'
# ft.FolderCheck('sgrb/D', True)
# x1 = file1.D.x1
# x2 = file1.D.x2
# y1 = file1.D.y1
# y2 = file1.D.y2
# column_limits = [y1 - 50, y2, None, None] ## columnlimits = [xmin, xmax, ymin, ymax]
# row_limits = [x1 - 50, x2, None, None] ## rowlimits = [xmin, xmax, ymin, ymax]
# ConvolveShift(sofia, spit, path, 460, y1, 0.000, 0.0, column_limits, row_limits)

# # Star E
# path = file + 'E/'
# ft.FolderCheck('sgrb/E', True)
# x1 = file1.E.x1
# x2 = file1.E.x2
# y1 = file1.E.y1
# y2 = file1.E.y2
# column_limits = [y1 - 50, y2, 0, None] ## columnlimits = [xmin, xmax, ymin, ymax]
# row_limits = [x1 - 50, x2, None, None] ## rowlimits = [xmin, xmax, ymin, ymax]
# ConvolveShift(sofia, spit, path, x1, y1, 0.000, 0.01, column_limits, row_limits)

# # Star F
# path = file + 'F/'
# ft.FolderCheck('sgrb/F', True)
# x1 = file1.F.x1
# x2 = file1.F.x2 + 25
# y1 = file1.F.y1
# y2 = file1.F.y2 + 25
# column_limits = [y1 - 25, y2, 0, .25] ## columnlimits = [xmin, xmax, ymin, ymax]
# row_limits = [x1 - 25, x2, 0, 0.25] ## rowlimits = [xmin, xmax, ymin, ymax]
# ConvolveShift(sofia, spit, path, x1, y1, 0.000, 0.0, column_limits, row_limits)

# Star G
path = file + 'G/'
ft.FolderCheck('sgrb/G', True)
x1 = file1.G.x1
x2 = file1.G.x2
y1 = file1.G.y1
y2 = file1.G.y2
column_limits = [y1 - 25, y2, 0, None] ## columnlimits = [xmin, xmax, ymin, ymax]
row_limits = [x1 - 25, x2, None, None] ## rowlimits = [xmin, xmax, ymin, ymax]
ConvolveShift(sofia, spit, path, x1, y1, 0.000, 0.0, column_limits, row_limits)

# # Star H
# path = file + 'I/'
# ft.FolderCheck('sgrb/I', True)
# x1 = file1.I.x1
# x2 = file1.I.x2
# y1 = file1.I.y1
# y2 = file1.I.y2
# column_limits = [y1, y2, 0, None] ## columnlimits = [xmin, xmax, ymin, ymax]
# row_limits = [x1, x2, None, None] ## rowlimits = [xmin, xmax, ymin, ymax]
# ConvolveShift(sofia, spit, path, x1, y1, 0.000, 0.01, column_limits, row_limits)

# # Star I
# path = file + 'I/'
# ft.FolderCheck('sgrb/I', True)
# x1 = file1.I.x1
# x2 = file1.I.x2
# y1 = file1.I.y1
# y2 = file1.I.y2
# column_limits = [y1, y2, 0, None] ## columnlimits = [xmin, xmax, ymin, ymax]
# row_limits = [x1, x2, None, None] ## rowlimits = [xmin, xmax, ymin, ymax]
# ConvolveShift(sofia, spit, path, x1, y1, 0.000, 0.01, column_limits, row_limits)

