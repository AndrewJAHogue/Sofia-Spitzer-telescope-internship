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



fits_hdu = fits.open(sofia)
f_var = fits_hdu[1].data
f_exposure = fits_hdu[2].data
# t_max = 793
threshold = 85
fraction = 0.55
copy = fits_hdu[0].data.copy()
# odd_stamps = [
#     copy[2798:3070][0:271].copy(),
#     copy[3656:3719][0:63].copy(),
#     copy[3510:3570][:60].copy()
# ]
for why, y in enumerate(copy):
    no_zeros = f_exposure[f_exposure != 0].copy()
    t_max = np.nanmedian(no_zeros[why])
    for ex,x in enumerate(copy[why]):
        t_ex = f_exposure[why][ex]
        # print(f'The exposure for x:{ex} and y:{why} is {t_ex} and the max for this row is {t_max}')
        # if why < 3634 and x < 1841 or why > 3814 and x > 1807:
        if t_ex < fraction*t_max and np.isnan(t_max) == False or t_ex == 0.0:
            copy[why][ex] = np.nan
#             if why < 2803:
#                 if ex < 2053:
#                     copy[why][ex] = np.nan
#             if why > 3060 and why < 3200:
#                 if ex < 2053:
#                     copy[why][ex] = np.nan
#             if why > 3200 and why < 3725:
#                 if ex > 2260:
#                     copy[why][ex] = np.nan
# copy[2798:3070][0:271] = odd_stamps[0]
# copy[3656:3719][0:63] = odd_stamps[1]
# copy[3510:3570][:60] = odd_stamps[2]

new_path = parent + 'EdgeMasked/'
ft.FolderCheck('EdgeMasked/', True)
filename = new_path + 'tmp_sofia.fits'

fits.writeto(filename, copy, fits_hdu[0].header, overwrite=True)

print(f'File written at {filename}')
end = time.perf_counter_ns()




time = end - start
if time / 1e6 < 1000:
    time /= 1e6
    time = str(time) + ' ms'
elif time / 1e9 < 360:
    time /= 1e9
    time = str(time) + ' s'
print(f'Function processed in {time}')