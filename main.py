
import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')
sys.path.append('./Combining Maps/')

import numpy as np
from astropy.io import fits

import lineplots as plt
import filetree as ft
import stars as st


import filetree as ft
file1 = st.isoOne
parent = ft.FitsFolder()
sofia = parent + 'Full Maps/'
sofia += 'F0217_FO_IMA_70030015_FORF253_MOS_0001-0348_final_MATT_Corrected.fits'
spit = parent + 'Full Maps/'
spit += 'Spitzer_GCmosaic_24um_onFORCASTheader_JyPix.fits'


from convolutions import ConvolveShift


path = parent + 'Full Maps/'
sigma_offset = 0.105
shift = 0.0085
# -------------------------------Convolve the SOFIA data------------------------------
# the x and y coordinates don't really matter here
convolved_files = ConvolveShift(sofia, spit, path, 1530, 3430, sigma_offset, shift) # tuple of convolved and convolved+shifted filepaths (strings)

#--------------------------------Combine it with the Spitzer data-------------------------
# CALCULATED NOISE LEVEL  noise_level = 0.0147
noise_level = 0.016

parent = ft.FitsFolder()
# sofia = parent + 'Combined Maps/Full Maps/convolved/'
# # sofia += 'F0217_FO_IMA_70030015_FORF253_MOS_0001-0348_final_MATT_Corrected.fits'
# f = '2026'
# sofia += f
sofia = convolved_files[1]

from NoiseMask import NoiseAndCombine
spit = parent + 'Full Maps/'
spit += 'Spitzer_GCmosaic_24um_onFORCASTheader_JyPix.fits'
filename = f'Full Maps/noiselvl-{noise_level}_{shift}_{(3.026 + sigma_offset)*1000}'
combined_output = NoiseAndCombine(noise_level, sofia, spit, filename)

