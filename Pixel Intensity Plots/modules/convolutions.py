from math import floor
from random import gauss
import numpy as np

from astropy.io import fits
from astropy.convolution import Gaussian2DKernel, convolve, interpolate_replace_nans, convolve_fft


import stars as st
import filetree as ft
fitsfolder = ft.FitsFolder() 
def ConvolveShift(sofia, spit, path, x, y, sigmashift, shift, collims=[None, None, None, None], rowlims=[None, None, None, None], **keywargs):
    increment = keywargs.get('increment', 0.0)
    x2 = keywargs.get('x2', None)
    y2 = keywargs.get('y2', None)
    
    print(f'x: {x} \ny: {y}')
    hdu = fits.open(sofia)[0]

    img = hdu.data
    img[img > 1] = np.nan
    img[img < 0] = np.nan

    files = np.array([])
    files = [sofia, spit]

    from lineplots import MultiLinePlot, SingleLinePlot

    from astropy.stats import gaussian_fwhm_to_sigma
    from math import sqrt
    fwhm = sqrt((5.9**2)-(2.2**2))
    sigma = fwhm * 1.302 * gaussian_fwhm_to_sigma ## converts from arcseconds to pixels
    sigma += sigmashift
    print(f'sigma => {sigma}')
    sigmas = [sigma]
    name_dot = sofia.find('.fits')
    name_slash = sofia.rfind('/') - 1
    filename = sofia[name_slash:name_dot]
    ft.FolderCheck(path[path.find('fits/') + 5:] + 'convolved' + filename, True)
    ft.FolderCheck(path[path.find('fits/') + 5:] + 'shifted' + filename, True)

    # shift = 0.008 ## shift data up slightly

    print(f'shift => {shift}')
    if increment != 0:
        sigmadown = sigma - increment
        sigmaup = sigma + increment
        sigmas.append(sigmaup)
        sigmas.append(sigmadown)
        print(f'sigmaup => {sigmaup}')
        print(f'sigmadown => {sigmadown}')
    for s in sigmas:
        p = f"{path}/convolved{filename}/{floor(s * 1000)}.fits"
        path_shifted = f"{path}/shifted{filename}/{shift * 1000}_{floor(s * 1000)}.fits"
        
        kernel = Gaussian2DKernel(s)
        astropy_conv = convolve_fft(img, kernel)

        fits.writeto(p, astropy_conv, hdu.header, overwrite=True)
        astropy_conv += shift
        fits.writeto(path_shifted, astropy_conv, hdu.header, overwrite=True)

        files = np.append(files, p)
        files = np.append(files, path_shifted)
    MultiLinePlot(x, y, files, collims, rowlims, legend=True)


    


