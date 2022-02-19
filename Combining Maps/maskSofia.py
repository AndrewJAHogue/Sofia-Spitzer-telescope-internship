import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import filetree as ft
import stars as st

path = '/media/al-chromebook/USB20FD/Python/Research/ToGiveHankings/'
# go through each chosen file I made
chosen = '15.0_3036.fits' 
star = 'sgrb/'
sofia1 = path + star + chosen
# sofia1 = st.isoOne.sofia

hdu = fits.open(sofia1)[0]
sofia1_data = hdu.data

bad = sofia1_data < 0.0147

copy = sofia1_data.copy()

copy[bad] = np.nan 


import lineplots as plt

x = st.isoOne.A.x1
y = st.isoOne.A.y1
path = ft.FitsFolder()
new = path + star + '/noise_masked_' + chosen
fits.writeto(new, copy, hdu.header, overwrite=True)
files = [sofia1, new]
plt.MultiLinePlot(x, y, files, legend=True)