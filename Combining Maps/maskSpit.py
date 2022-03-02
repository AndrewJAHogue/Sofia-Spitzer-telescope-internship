import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits
import filetree as ft
import stars as st

files = np.array([])
path = ft.FitsFolder()
# change file out for each spitzer24 file
spits = [ st.isoOne.spitzer, st.isoTwo.spitzer, st.sgrb.spitzer ]
def NoiseMask(noise_level):
    global files
    for i, spit in enumerate(spits):
        i += 1
        hdu = fits.open(spit)[0]
        spit_data = hdu.data

        bad = spit_data > noise_level

        copy = spit_data.copy()

        copy[bad] = np.nan
        bad = spit_data < 0
        copy[bad] = np.nan
        if i == 3:
            i = 'SGRB'
        new = path + '/masked spitzers/noise_masked_' + 'spitzer' + str(i) + '.fits'
        print(f'File written at {new}')
        fits.writeto(new, copy, hdu.header, overwrite=True)
        files = np.append(files, new)
        import matplotlib.pyplot as plt
        plt.plot(copy, label="masked")
        plt.plot(spit_data, label="original")
        plt.show()


NoiseMask(0.0147)

import sys
sys.path.append('./Pixel Intensity Plots/modules/')
sys.path.append('./modules/')

from lineplots import MultiLinePlot
import stars as st

x = st.isoOne.A.x1
y = st.isoOne.A.y1
files = [files[0]]
files = np.append(files, st.isoOne.spitzer)
files = np.flip(files)

MultiLinePlot(x,y, files, legend=True)