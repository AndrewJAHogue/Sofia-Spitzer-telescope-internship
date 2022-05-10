import sys
sys.path.append('./modules/')

import numpy as np
from astropy.io import fits

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
    new_path = path + 'Combined Maps/' + filename + '.fits'
    fits.writeto(new_path, new, for_header, overwrite=True)
    print(f'File written at {new_path}')
    return new_path
 