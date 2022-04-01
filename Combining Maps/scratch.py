import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import filetree as ft
import stars as st

parent = '/media/al-chromebook/USB20FD/Python/Research/fits/'
full = parent + 'Combined Maps/full_0.016_2026.fits.fits'
spit = parent + 'noise_masked_Spitzer_GCmosaic_24um_onFORCASTheader_JyPix.fits'
sofia = parent + 'noise_masked_2026.fits'
data = fits.open(sofia)[0].data
print(data[2550][2050])