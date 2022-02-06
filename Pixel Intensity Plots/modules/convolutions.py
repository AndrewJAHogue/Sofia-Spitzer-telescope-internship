from math import floor
from random import gauss
import numpy as np

from astropy.io import fits
from astropy.convolution import Gaussian2DKernel, convolve, interpolate_replace_nans, convolve_fft


import stars as st
import filetree as ft
fitsfolder = ft.FitsFolder() 
def ConvolveShift(path, x, y, sigmashift, shift, collims=[None, None, None, None], rowlims=[None, None, None, None], **keywargs):
    increment = keywargs.get('increment', 0.0)
    x2 = keywargs.get('x2', None)
    y2 = keywargs.get('y2', None)
    
    sofia = fitsfolder + "/Forcast25_isoField1.fits"
    spit = fitsfolder + "/Reprojected Spitzer24 IsoFields @ Forcast25 isoField1.fits"
    print(f'x: {x} \ny: {y}')
    hdu = fits.open(sofia)[0]


    # scale the file and crop
    # img = hdu.data[x1:x2, y1:y2]
    img = hdu.data
    img[img > 1] = np.nan
    img[img < 0] = np.nan

    files = np.array([])
    files = [sofia, spit]

    # from astropy import units as u
    # a = 2.4 * u.arcsec
    # print(a.to(pix))

    from lineplots import MultiLinePlot, SingleLinePlot

    from astropy.stats import gaussian_fwhm_to_sigma
    from math import sqrt
    fwhm = sqrt((5.9**2)-(2.2**2))
    sigma = fwhm * 1.302 * gaussian_fwhm_to_sigma ## converts from arcseconds to pixels
    sigma += sigmashift
    print(f'sigma => {sigma}')
    sigmas = [sigma]

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
        p = f"{path}/convolved/{floor(s * 1000)}.fits"
        path_shifted = f"{path}/shifted/{shift * 1000}_{floor(s * 1000)}.fits"
        
        kernel = Gaussian2DKernel(s)
        astropy_conv = convolve_fft(img, kernel)

        fits.writeto(p, astropy_conv, hdu.header, overwrite=True)
        astropy_conv += shift
        fits.writeto(path_shifted, astropy_conv, hdu.header, overwrite=True)

        files = np.append(files, p)
        files = np.append(files, path_shifted)
    MultiLinePlot(x, y, files, collims, rowlims, legend=True)


    


