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
# this [:605] limits it to essentially isofield1, for efficiency
copy = fits_hdu[0].data.copy()
# print(fits_hdu[0].data[:605,2800:].shape)
fraction = 1.3

for why, y in enumerate(copy):
    t_max = np.nanmedian(f_exposure[f_exposure != 0][why])
    for ex,x in enumerate(copy[why]):
        t_ex = f_exposure[why][ex]
        if t_ex < fraction*t_max and np.isnan(t_max) == False or t_ex == 0.0:
            copy[why][ex] = np.nan

s = 'FullSofia'
ft.FolderCheck(f'EdgeMasked/{s}/', True)
new_path += f'{s}/'
filename = f'{fraction}_{s}.fits'
print(filename)
outpath = new_path + filename
print(outpath)

fits.writeto(outpath, copy, fits_hdu[0].header, overwrite=True)

print(f'File written at {outpath}')






end = time.perf_counter_ns()
time = end - start
if time / 1e6 < 1000:
    time /= 1e6
    time = str(time) + ' ms'
elif time / 1e9 < 120:
    time /= 1e9
    time = str(time) + ' s'
elif ( time / 1e9 ) / 60 < 60:
    time /= 1e9
    time /= 60
    time = str(time) + ' min'
print(f'Function processed in {time}')