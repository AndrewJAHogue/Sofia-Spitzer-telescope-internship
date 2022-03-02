import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import filetree as ft
import stars as st
output = np.array([])
def NoiseMask(files, stars, noise_level):
    global output
    for s, f in enumerate(files):
        star = stars[s]
        hdu = fits.open(f)[0]
        f_data = hdu.data

        bad = f_data < noise_level

        copy = f_data.copy()

        copy[bad] = np.nan 

        import lineplots as plt

        path = ft.FitsFolder()
        new = path + 'Forcast' + star + '/noise_masked_' + str(noise_level) + '.fits'
        print(f'File written at {new}')
        fits.writeto(new, copy, hdu.header, overwrite=True)
        output = np.append(output, new)
        # output = [f, new]
        # plt.MultiLinePlot(x, y, output, legend=True)


# --------The input files----------------
path = '/media/al-chromebook/USB20FD/Python/Research/ToGiveHankings/'
# go through each chosen file I made
f = {'One': '8.5_3036.fits', 'Two': '12.0_3031.fits', 'sgrb': '15.0_3036.fits'}
files = np.array([])
stars_folders = np.array([])
for key in f:
    chosen = f[key]
    p = path + key + '/' + chosen
    files = np.append(files, p)
    stars_folders = np.append(stars_folders, key)

# ----------RUN-------------------------
NoiseMask(files, stars_folders, 0.0147)


# ------------Check a Single file-----------
import sys
sys.path.append('./Pixel Intensity Plots/modules/')
sys.path.append('./modules/')

from lineplots import MultiLinePlot
import stars as st

x = st.isoOne.A.x1
y = st.isoOne.A.y1
output = [output[0]]
output = np.append(output, st.isoOne.sofia)
output = np.flip(output)

MultiLinePlot(x,y, output, legend=True)
