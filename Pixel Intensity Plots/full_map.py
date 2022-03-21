from math import floor

import sys
sys.path.append('./Pixel Intensity Plots/modules/')
sys.path.append('./modules/')

import stars as st

import filetree as ft
file1 = st.isoOne
parent = ft.FitsFolder()
sofia = parent + 'Full Maps/'
sofia += 'F0217_FO_IMA_70030015_FORF253_MOS_0001-0348_final_MATT_Corrected.fits'
spit = parent + 'Full Maps/'
spit += 'Spitzer_GCmosaic_24um_onFORCASTheader_JyPix.fits'

from convolutions import ConvolveShift

path = parent + 'Combined Maps/Full Maps/'
x1 = 3130
x2 = file1.A.x2
y1 = 406
y2 = file1.A.y2
sigma_offset = 0.01
shift = 0.0085
# column_limits = [y1 - 25, y2, 0, 0.05] ## columnlimits = [xmin, xmax, ymin, ymax]
# row_limits = [x1 - 25, x2, None, 0.05] ## rowlimits = [xmin, xmax, ymin, ymax]
ConvolveShift(sofia, spit, path, x1, y1, -1, 0.00)
# ConvolveShift(sofia, spit, path, x1, y1, 0.01, 0.0085, column_limits, row_limits)
