import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import lineplots as plt
import filetree as ft
import stars as st
# 'stars' is essentially a list of strings to append to the filename (i.e. ['one', 'two', 'sgrb'])
def NoiseMask(noise_level, sofia, spitzer):
    masks = []
    # ---------SOFIA------------------------------------------------------------------------------------------------
    path = ft.FitsFolder()
    # -------create mask from spitzer data---------
    # spits = [ st.isoOne.spitzer, st.isoTwo.spitzer, st.sgrb.spitzer ]
    # hdu = fits.open(spits[s])[0]
    # spit_data = hdu.data

    # spit_mask = spit_data > 0.147
    # ---------------------------------------------
    hdu = fits.open(sofia)[0]
    f_data = hdu.data

    copy = f_data.copy()
    bad = f_data < noise_level
    # copy[~spit_mask] = np.nan 
    copy[bad] = np.nan 

    name_dot = sofia.find('.fits')
    name_slash = sofia.find('//')

    new = path + '/noise_masked_' + sofia[name_slash:name_dot] + '.fits'
    fits.writeto(new, copy, hdu.header, overwrite=True)

    # ---------------SPITZER-----------------------------------------------------------------
    # -----------MASKS from sofia data---------------------------
    hdu = fits.open(sofia)[0]
    sofia_data = hdu.data
    sofia_mask = sofia_data < 0.0147
    # --------------------------------------

    hdu = fits.open(spitzer)[0]
    spit_data = hdu.data

    copy = spit_data.copy()
    # ---mask from spit data-------
    # bad = spit_data > 0.0147
    # ------------------------------
    # copy[bad] = np.nan
    copy[~sofia_mask] = np.nan
    bad = spit_data < 0
    copy[bad] = np.nan
    

    name_dot = spitzer.find('.fits')
    name_slash = spitzer.find('//') + 2
    
    new = path + '/masked spitzers/noise_masked_' + spitzer[name_slash:name_dot] + '.fits'
    print(f'File written at {new}')
    fits.writeto(new, copy, hdu.header, overwrite=True)

    
   

# ------------CALCULATED NOISE LEVEL----------------------------------

noise_level = 0.0147

# -----------------------------------------------------------------



def Combine(sofia, spit, filename):
    path = ft.FitsFolder()
    for_hdu = fits.open(sofia)[0]
    for_data = for_hdu.data

    spit_hdu = fits.open(spit)[0]
    spit_data = spit_hdu.data

    new = np.nansum([for_data, spit_data], axis=0) 
    new_path = path + 'Combined Maps/' + filename + '.fits'
    fits.writeto(new_path, new, for_hdu.header, overwrite=True)
    
# --------------------------------------------------------------------------------------------------------
  

def NoiseAndCombine(noise_level, sofia, spitzer, filename):
    NoiseMask(noise_level, sofia, spitzer)
    Combine(sofia, spitzer, filename)

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


sofia = sofias[0]
spitzer = st.isoOne.spitzer
filename = 'isoOne'

NoiseAndCombine(noise_level, sofia, spitzer, filename)