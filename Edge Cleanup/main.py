import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import lineplots as plt
import filetree as ft
import stars as st
parent = ft.FitsFolder()
sofia = parent + 'Full Maps/F0217_FO_IMA_70030015_FORF253_MOS_0001-0348_final_MATT_Corrected.fits'
spit = parent + 'Full Maps/Spitzer_GCmosaic_24um_onFORCASTheader_JyPix.fits'


new_path = parent + 'EdgeMasked/'
ft.FolderCheck('EdgeMasked/', True)

fits_hdu = fits.open(sofia)
f_var = fits_hdu[1].data
f_exposure = fits_hdu[2].data
# t_max = 793
copy = fits_hdu[0].data.copy()
for why, y in enumerate(copy):
    for ex,x in enumerate(y):
        t_ex = f_exposure[why][ex]
        t_max = np.max(y)
        if t_ex < 0.3*t_max:
            x = np.nan


filename = new_path + 'tmp_sofia.fits'
fits.writeto(filename, copy, fits_hdu[0].header, overwrite=True)
print(f'File written at {new_path}')

# print(np.max(f_exposure[4716]))