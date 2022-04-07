import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import lineplots as plt
import filetree as ft
import stars as st

import time
start = time.perf_counter()

def EdgeMask(fraction, data, exposure):
    copy = data.copy()
    for why, y in enumerate(copy):
        no_zeros = exposure[exposure != 0].copy()
        t_max = np.nanmedian(no_zeros[why])
        for ex,x in enumerate(copy[why]):
            t_ex = exposure[why][ex]
            if t_ex < fraction*t_max and np.isnan(t_max) == False or t_ex == 0.0:
                copy[why][ex] = np.nan
    return copy



def SmallExposureMap(data, full_exposure):
    new_ex = np.full_like(data, np.nan)
    why = full_exposure.shape[0] - data.shape[0] - 1
    for j, y in enumerate(full_exposure):
        if j < data.shape[0] - 1:
            for i, x in enumerate(y):
                if i < data.shape[1] - 1:
                    new_ex[j][i] = full_exposure[why][i]
            why += 1
    return new_ex
        
parent = ft.FitsFolder()

s = 'Forcast25_SgrB.fits'

outpath = f'EdgeMasked/{s}'
ft.FolderCheck(outpath, True)
outpath = parent + outpath
sofia = parent + s

exposure = parent + 'Full Maps/F0217_FO_IMA_70030015_FORF253_MOS_0001-0348_final_MATT_Corrected.fits'
small_exposure = parent + 'EdgeMasked/sgrb_exposure.fits'

ex_hdu = fits.open(exposure)[2]
f_exposure = ex_hdu.data
fits_hdu = fits.open(sofia)
f_copy = fits_hdu[0].data.copy()
small_exposure_data = fits.open(small_exposure)[0].data

fraction = 0.5

filename = parent + 'EdgeMasked/' + str(fraction) + '_' + s
masked = EdgeMask(fraction, f_copy, small_exposure_data)

fits.writeto(filename, masked, fits_hdu[0].header, overwrite=True)

print(f'File written at {filename}')








end = time.perf_counter()
time = end - start
# if time / 1e6 < 1000:
#     time /= 1e6
#     time = str(time) + ' ms'
# elif time / 1e9 < 360:
#     time /= 1e9
#     time = str(time) + ' s'
print(f'Function processed in {time}')