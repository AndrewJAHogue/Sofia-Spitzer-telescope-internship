import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import filetree as ft
import stars as st
# 'stars' here is just a list of the string keys for each file (i.e. ['one', 'two', 'sgrb'])
def SofiaMask(files, stars, noise_level):
    output = np.array([])
    for s, f in enumerate(files):
        star = stars[s]
        hdu = fits.open(f)[0]
        f_data = hdu.data

        bad = f_data < noise_level

        copy = f_data.copy()

        copy[bad] = np.nan 

        import lineplots as plt

        path = ft.FitsFolder()
        new = path + 'Forcast' + star + '/noise_masked_' + str(noise_level) + '.fits'
        print(f'File written at {new}')
        fits.writeto(new, copy, hdu.header, overwrite=True)
        output = np.append(output, new)
        return output
        # output = [f, new]
        # plt.MultiLinePlot(x, y, output, legend=True)

path = ft.FitsFolder()
# change file out for each spitzer24 file
spits_output = np.array([])
def SpitMask(noise_level):
    global spits_output
    spits = [ st.isoOne.spitzer, st.isoTwo.spitzer, st.sgrb.spitzer ]
    for i, spit in enumerate(spits):
        i += 1
        hdu = fits.open(spit)[0]
        spit_data = hdu.data

        bad = spit_data > noise_level

        copy = spit_data.copy()

        copy[bad] = np.nan
        bad = spit_data < 0
        copy[bad] = np.nan
        if i == 3:
            i = 'SGRB'
        new = path + '/masked spitzers/noise_masked_' + 'spitzer' + str(i) + '.fits'
        # print(f'File written at {new}')
        fits.writeto(new, copy, hdu.header, overwrite=True)
        spits_output = np.append(spits_output, new)
    return spits_output



def Combine(noise_level):
    spits = SpitMask(noise_level)
    # sort so list is ['...One...', '...Two...', '...sgrb...']
    spits = np.sort(spits)
    
    # --------The input files for SofiaMask----------------
    path = '/media/al-chromebook/USB20FD/Python/Research/ToGiveHankings/'
    # go through each chosen sofia file I made
    f = {'One': '8.5_3036.fits', 'Two': '12.0_3031.fits', 'sgrb': '15.0_3036.fits'}
    files = np.array([])
    stars_folders = np.array([])
    for key in f:
        chosen = f[key]
        p = path + key + '/' + chosen
        files = np.append(files, p)
        stars_folders = np.append(stars_folders, key)
    
    sofias = SofiaMask(files, stars_folders, noise_level)
    sofias = np.sort(sofias)
    print(f'the sorted sofias are {sofias}')

Combine(0.00147)
