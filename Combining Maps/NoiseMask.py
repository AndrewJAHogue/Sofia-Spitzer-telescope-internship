import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import lineplots as plt
import filetree as ft
import stars as st
 
def NoiseMask(sofia_noise_level, spit_noise_level, input_files, stars):
    path = ft.FitsFolder()
    for s, f in enumerate(input_files):
        star = stars[s]
        # if isinstance(f, (1, 2)):

        hdu = fits.open(f)[0]
        f_data = hdu.data

        bad = f_data < sofia_noise_level

        copy = f_data.copy()

        copy[bad] = 0
        # copy[bad] = np.nan 
        
        new = path + 'Forcast' + star + '/noise_masked_' + str(sofia_noise_level) + '.fits'
        fits.writeto(new, copy, hdu.header, overwrite=True)
        
    # Spitzer
    spits = [ st.isoOne.spitzer, st.isoTwo.spitzer, st.sgrb.spitzer ]
    for i, spit in enumerate(spits):
        i += 1
        hdu = fits.open(spit)[0]
        spit_data = hdu.data

        bad = spit_data > spit_noise_level
        copy = spit_data.copy()
        copy[bad] = np.nan

        bad = spit_data < 0
        copy[bad] = np.nan

        if i == 3:
            i = 'SGRB'
        new = path + '/masked spitzers/noise_masked_' + 'spitzer' + str(i) + '.fits'
        fits.writeto(new, spit_data, hdu.header, overwrite=True)



# Files from sofia I want to noise-mask
hankinsfolder = '/media/al-chromebook/USB20FD/Python/Research/ToGiveHankings/'
f = {'One': '8.5_3036.fits', 'sgrb': '15.0_3036.fits', 'Two': '12.0_3031.fits'}
files = np.array([])
stars_folders = np.array([])
for key in f:
    chosen = f[key]
    p = hankinsfolder + key + '/'  + chosen
    files = np.append(files, p)
    stars_folders = np.append(stars_folders, key)
# under = files[0][:files[0].find('_')]
# print(under)
# hash = under[under.find('/')]
# print(hash)
# found = files[0][under:hash]
# print(found)

# ------------CALCULATED NOISE LEVEL----------------------------------

noise_level = 0.0147

# -----------------------------------------------------------------

# NoiseMask(0.0, noise_level, files, stars_folders)


sys.path
import glob
def Combine(inputs_sofia, inputs_spit):
    path = ft.FitsFolder()
    # spits = path + '/masked spitzers/*.fits'
    spits = inputs_spit.copy()
    for i,S in enumerate(spits):
        print(inputs_sofia[i])
        for_hdu = fits.open(inputs_sofia[i])[0]
        for_data = for_hdu.data

        spit_hdu = fits.open(S)[0]
        spit_data = spit_hdu.data

        new = for_data + spit_data 
        new = np.nanmean([for_data, spit_data], axis=0) #doesn't do what I expected
        i += 1
        if i == 3:
            i = 'sgrb'
        new_path = path + 'Combined Maps/' + str(i) + '.fits'
        fits.writeto(new_path, new, for_hdu.header, overwrite=True)
    
path = ft.FitsFolder()
output_masked = np.array([])
for star in stars_folders:
    o = path + 'Forcast' + star + '/noise_masked_' + str(noise_level) + '.fits'
    output_masked = np.append(output_masked, o)
print(output_masked)


spit = path + 'masked spitzers/noise_masked_spitzer'
spits_masked = [ spit + '1.fits', spit + 'SGRB.fits', spit + '2.fits']

Combine(output_masked, spits_masked)