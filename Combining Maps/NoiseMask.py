import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import lineplots as plt
import filetree as ft
import stars as st
# 'stars' is essentially a list of strings to append to the filename (i.e. ['one', 'two', 'sgrb'])
def NoiseMask(sofia_noise_level, input_files):
    masks = []
    # ---------SOFIA------------------------------------------------------------------------------------------------
    path = ft.FitsFolder()
    stars = ['One', 'sgrb', 'Two']
    # sort so list is ['...One...', '...Two...', '...sgrb...']
    stars = np.sort(stars)
    input_files = np.sort(input_files)
    for s, f in enumerate(input_files):
        # hdu = fits.open(st.isoOne.spitzer)[0]
        # spit_data = hdu.data

        # spit_mask = spit_data > 0.147
        
        star = stars[s]
        hdu = fits.open(f)[0]
        f_data = hdu.data

        copy = f_data.copy()
        bad = f_data < sofia_noise_level
        # copy[bad] = 0
        # bad = copy[spit_mask]
        copy[bad] = np.nan 
        
        new = path + 'Forcast' + star + '/noise_masked_' + str(sofia_noise_level) + '.fits'
        fits.writeto(new, copy, hdu.header, overwrite=True)

     # ---------------SPITZER-----------------------------------------------------------------
    files_spit = np.array([])
    path = ft.FitsFolder()
    spits = [ st.isoOne.spitzer ]
    # spits = [ st.isoOne.spitzer, st.isoTwo.spitzer, st.sgrb.spitzer ]
    for i, spit in enumerate(spits):
        hdu = fits.open(input_files[0])[0]
        sofia_data = hdu.data

        sofia_mask = sofia_data < 0.0147
        hdu = fits.open(spit)[0]
        spit_data = hdu.data

        copy = spit_data.copy()
        
        # bad = spit_data > 0.0147
        # spit_noise_line = np.where(spit_data > 0.0147)
        # masks = np.append(masks, bad)
        copy[sofia_mask] = np.nan

        bad = spit_data < 0
        copy[bad] = np.nan
        i += 1
        if i == 3:
            i = 'SGRB'
        new = path + '/masked spitzers/noise_masked_' + 'spitzer' + str(i) + '.fits'
        # print(f'File written at {new}')
        fits.writeto(new, copy, hdu.header, overwrite=True)
        files_spit = np.append(files_spit, new)
    return 

    
   

# ----------Files from sofia I want to noise-mask----------
hankinsfolder = '/media/al-chromebook/USB20FD/Python/Research/ToGiveHankings/'
f = {
    'One': '8.5_3036.fits',
    'sgrb': '15.0_3036.fits', 
    'Two': '12.0_3031.fits'
}
files = np.array([])
stars_folders = np.array([])
for key in f:
    chosen = f[key]
    p = hankinsfolder + key + '/'  + chosen
    files = np.append(files, p)
    stars_folders = np.append(stars_folders, key)

# ------------CALCULATED NOISE LEVEL----------------------------------

noise_level = 0.0147

# -----------------------------------------------------------------

NoiseMask(noise_level, files)


sys.path
import glob
def Combine(inputs_sofia, inputs_spit):
    path = ft.FitsFolder()
    # spits = path + '/masked spitzers/*.fits'
    spits = inputs_spit.copy()
    for i,S in enumerate(spits):
        # print(inputs_sofia[i])
        for_hdu = fits.open(inputs_sofia[i])[0]
        for_data = for_hdu.data

        spit_hdu = fits.open(S)[0]
        spit_data = spit_hdu.data

        new = for_data + spit_data 
        new = np.nansum([for_data, spit_data], axis=0) 
        i += 1
        if i == 3:
            i = 'sgrb'
        new_path = path + 'Combined Maps/' + str(i) + '_sofia_mask' + '.fits'
        fits.writeto(new_path, new, for_hdu.header, overwrite=True)
    
# --------------------------------------------------------------------------------------------------------
  
path = ft.FitsFolder()
output_masked = np.array([])
for star in stars_folders:
    o = path + 'Forcast' + star + '/noise_masked_' + str(noise_level) + '.fits'
    output_masked = np.append(output_masked, o)
# print(output_masked)


spit = path + 'masked spitzers/noise_masked_spitzer'
spits_masked = [ spit + '1.fits', spit + 'SGRB.fits', spit + '2.fits']

Combine(output_masked, spits_masked)