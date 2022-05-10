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

   

# # ----------Files from sofia I want to noise-mask----------
# hankinsfolder = '/media/al-chromebook/USB20FD/Python/Research/ToGiveHankings/'
# f = {
#     'One': '8.5_3036.fits',
#     'sgrb': '15.0_3036.fits', 
#     'Two': '12.0_3031.fits'
# }
# sofias = np.array([])
# for key in f:
#     chosen = f[key]
#     p = hankinsfolder + key + '/'  + chosen
#     sofias = np.append(sofias, p)
# sofias = np.sort(sofias)


# ------------CALCULATED NOISE LEVEL----------------------------------
noise_level = 0.016
# noise_level = 0.0147
# --------------------------------------------------------------------

# sofia = sofias[0]
# spitzer = st.isoOne.spitzer
# filename = 'isoOne'
# NoiseAndCombine(noise_level, sofia, spitzer, filename)

# sofia = sofias[1]
# spitzer = st.isoTwo.spitzer
# filename = 'isoTwo'
# NoiseAndCombine(noise_level, sofia, spitzer, filename)

# sofia = sofias[2]
# spitzer = st.sgrb.spitzer
# filename = 'sgrb_tmp'
# NoiseAndCombine(n_level, sofia, spitzer, filename)

# final, full map
# parent = ft.FitsFolder()
# sofia = parent + 'Combined Maps/Full Maps/convolved/'
# # sofia += 'F0217_FO_IMA_70030015_FORF253_MOS_0001-0348_final_MATT_Corrected.fits'
# f = '2026'
# sofia += f

# spit = parent + 'Full Maps/'
# spit += 'Spitzer_GCmosaic_24um_onFORCASTheader_JyPix.fits'
# filename = 'full' + '_' + str(noise_level) + '_' + f 
# NoiseAndCombine(noise_level, sofia, spit, filename)
