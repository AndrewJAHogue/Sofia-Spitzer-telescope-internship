import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import lineplots as plt
import filetree as ft
import stars as st
def NoiseAndCombine(noise_level, sofia, spitzer, filename):
    # ---------SOFIA------------------------------------------------------------------------------------------------
    hdu = fits.open(sofia)[0]
    f_data = hdu.data
    for_header = hdu.header

    sofia_copy = f_data.copy()
    # ---------Mask using noise level--------------------------
    bad = f_data < noise_level
    sofia_copy[bad] = np.nan 
    # -----------------------------------

    # -------create mask from spitzer data---------
    # hdu = fits.open(spitzer)[0]
    # spit_data = hdu.data

    # spit_mask = spit_data > noise_level
    # sofia_copy[~spit_mask] = np.nan 
    # ---------------------------------------------

    # ---------------SPITZER-----------------------------------------------------------------

    hdu = fits.open(spitzer)[0]
    spit_data = hdu.data

    spit_copy = spit_data.copy()
    # ---mask from spit data-------
    # bad = spit_data > noise_level
    # spit_copy[bad] = np.nan
    # ------------------------------

    # -----------MASK from sofia data---------------------------
    hdu = fits.open(sofia)[0]
    sofia_data = hdu.data
    sofia_mask = sofia_data < noise_level
    spit_copy[~sofia_mask] = np.nan
    # --------------------------------------

    # data below 0 is bad
    bad = spit_data < 0
    spit_copy[bad] = np.nan
    
    path = ft.FitsFolder()
    new = np.nanmean([spit_copy, sofia_copy], axis=0) 
    new_path = path + 'Combined Maps/' + filename
    fits.writeto(new_path, new, for_header, overwrite=True)
    print(f'File written at {new_path}')
    

# ----------Files from sofia I want to noise-mask----------
hankinsfolder = '/media/al-chromebook/USB20FD/Python/Research/ToGiveHankings/'
f = {
    'One': '8.5_3036.fits',
    'sgrb': '15.0_3036.fits', 
    'Two': '12.0_3031.fits'
}
sofias = np.array([])
for key in f:
    chosen = f[key]
    p = hankinsfolder + key + '/'  + chosen
    sofias = np.append(sofias, p)
sofias = np.sort(sofias)


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
parent = ft.FitsFolder()
sofia = parent + 'Combined Maps/Full Maps/EdgeMasked/convolveda/1.3_FullSofia/'
f = '3026.fits'
sofia += f

spit = parent + 'Full Maps/'
spit += 'Spitzer_GCmosaic_24um_onFORCASTheader_JyPix.fits'
filename = f'Full Maps/EdgeMasked/full_{str(noise_level)}_{f}'
# filename = 'full' + '_' + str(noise_level) + '_' + f 
NoiseAndCombine(noise_level, sofia, spit, filename)
