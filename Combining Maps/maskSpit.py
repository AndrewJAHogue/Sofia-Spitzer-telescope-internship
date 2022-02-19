import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits
import filetree as ft
import stars as st


path = ft.FitsFolder()
# change file out for each spitzer24 file
spit = st.isoOne.spitzer

hdu = fits.open(spit)[0]
spit_data = hdu.data

bad = spit_data > 0.0149

copy = spit_data.copy()

copy[bad] = np.nan 
bad = spit_data < 0
copy[bad] = np.nan 

new = path + '/masked spitzers/noise_masked_' + 'spitzerOne.fits'
fits.writeto(new, copy, hdu.header, overwrite=True)

# import matplotlib.pyplot as plt
# plt.plot(copy, label="masked")
# # plt.plot(spit_data, label="original")
# plt.show()