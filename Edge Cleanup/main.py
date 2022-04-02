import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import lineplots as plt
import filetree as ft
import stars as st

import time
start = time.perf_counter_ns()

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
    t_max = np.nanmax(f_exposure[why])
    for ex,x in enumerate(copy[why]):
        t_ex = f_exposure[why][ex]
        # print(f'The exposure for x:{ex} and y:{why} is {t_ex} and the max for this row is {t_max}')
        if t_ex < 0.3*t_max and np.isnan(t_max) == False or t_ex == 0.0:
            copy[why][ex] = np.nan
# t_max = np.nanmax(f_exposure[180])
# for i, x in enumerate(copy[180]):
#     t = f_exposure[180][i]
#     if t < 0.3*t_max:
#         copy[180][i] = np.nan

filename = new_path + 'tmp_sofia.fits'
fits.writeto(filename, copy, fits_hdu[0].header, overwrite=True)
print(f'File written at {filename}')
end = time.perf_counter_ns()

# print((f_exposure[180][f_exposure[180] < 160]))





print(f'Function processed in {((end - start)*1e-6)} ms')