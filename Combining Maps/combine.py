import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import filetree as ft
import stars as st

path = ft.FitsFolder()
masked = path + 'masked spitzers/'
forcast = {'One': 'noise_masked_8.5_3036.fits', 'Two': 'noise_masked_12.0_3031.fits', 'sgrb': 'noise_masked_15.0_3036.fits'}
spit = {'One': 'noise_masked_spitzer1.fits', 'Two': 'noise_masked_spitzer2.fits', 'sgrb': 'noise_masked_spitzerSGRB.fits'}

for key in forcast:
    for_hdu = fits.open(path + 'Forcast' + key + '/' + forcast[key])[0]
    for_data = for_hdu.data

    spit_hdu = fits.open(masked + spit[key])[0]
    spit_data = spit_hdu.data

    new = for_data + spit_data 
    # new = np.nansum([for_data, spit_data]) #doesn't do what I expected
    new_path = path + 'Combined Maps/' + key + '.fits'
    fits.writeto(new_path, new, for_hdu.header, overwrite=True)



    

