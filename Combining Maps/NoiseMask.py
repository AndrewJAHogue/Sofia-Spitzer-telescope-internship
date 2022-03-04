import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import lineplots as plt
import filetree as ft
import stars as st
def NoiseMask(noise_level, sofia, spitzer):
    # ---------SOFIA------------------------------------------------------------------------------------------------
    hdu = fits.open(sofia)[0]
    f_data = hdu.data

    copy = f_data.copy()
    # ---------Mask using noise level--------------------------
    bad = f_data < noise_level
    copy[bad] = np.nan 
    # -----------------------------------

    # -------create mask from spitzer data---------
    # hdu = fits.open(spitzer)[0]
    # spit_data = hdu.data

    # spit_mask = spit_data > noise_level
    # copy[~spit_mask] = np.nan 
    # ---------------------------------------------

    name_dot = sofia.find('.fits')
    name_slash = sofia.rfind('/') + 1
    
    path = ft.FitsFolder()
    new_sofia = path + '/noise_masked_' + sofia[name_slash:name_dot] + '.fits'
    fits.writeto(new_sofia, copy, hdu.header, overwrite=True)
    print(f'File written at {new_sofia}')

    # ---------------SPITZER-----------------------------------------------------------------

    hdu = fits.open(spitzer)[0]
    spit_data = hdu.data

    copy = spit_data.copy()
    # ---mask from spit data-------
    # bad = spit_data > noise_level
    # copy[bad] = np.nan
    # ------------------------------

    # -----------MASK from sofia data---------------------------
    hdu = fits.open(sofia)[0]
    sofia_data = hdu.data
    sofia_mask = sofia_data < noise_level
    copy[~sofia_mask] = np.nan
    # --------------------------------------

    # data below 0 is bad
    # bad = spit_data < 0
    # copy[bad] = np.nan
    

    name_dot = spitzer.find('.fits')
    name_slash = sofia.rfind('/') - 1

    new_spit = path + '/masked spitzers/noise_masked_' + spitzer[name_slash:name_dot] + '.fits'
    print(f'File written at {new_spit}')
    fits.writeto(new_spit, copy, hdu.header, overwrite=True)
    return new_spit, new_sofia

def Combine(sofia, spit, filename):
    path = ft.FitsFolder()
    for_hdu = fits.open(sofia)[0]
    for_data = for_hdu.data

    spit_hdu = fits.open(spit)[0]
    spit_data = spit_hdu.data
    
    new = np.nanmean([for_data, spit_data], axis=0) 
    new_path = path + 'Combined Maps/' + filename + '.fits'
    fits.writeto(new_path, new, for_hdu.header, overwrite=True)
    print(f'File written at {new_path}')
    
# --------------------------------------------------------------------------------------------------------
  

def NoiseAndCombine(noise_level, sofia, spitzer, filename):
    new_spit, new_sofia = NoiseMask(noise_level, sofia, spitzer)
    Combine(new_sofia, new_spit, filename)

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
n_level = 0.016
# noise_level = 0.0147
# --------------------------------------------------------------------

# sofia = sofias[0]
# spitzer = st.isoOne.spitzer
# filename = 'isoOne_tmp'
# NoiseAndCombine(noise_level, sofia, spitzer, filename)

# sofia = sofias[1]
# spitzer = st.isoTwo.spitzer
# filename = 'isoTwo'
# NoiseAndCombine(noise_level, sofia, spitzer, filename)

sofia = sofias[2]
spitzer = st.sgrb.spitzer
filename = 'sgrb_tmp'
NoiseAndCombine(n_level, sofia, spitzer, filename)
