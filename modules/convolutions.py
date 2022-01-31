from math import floor
from random import gauss
import numpy as np

from astropy.io import fits
from astropy.convolution import Gaussian2DKernel, convolve, interpolate_replace_nans, convolve_fft


import stars as st

# file1 = st.isoOne
# x1 = file1.A.x1
# y1 = file1.A.y1
# print(f'x1: {x1} \ny1: {y1}')
# sofia = "../fits/Forcast25_isoField1.fits"
# spit = "../fits/Reprojected Spitzer24 IsoFields @ Forcast25 isoField1.fits"
# x2 = file1.A.x2
# y2 = file1.A.y2

# file1 = st.isoOne
# x1 = file1.C.x1
# y1 = file1.C.y1
# print(f'x1: {x1} \ny1: {y1}')
# sofia = "../fits/Forcast25_isoField1.fits"
# spit = "../fits/Reprojected Spitzer24 IsoFields @ Forcast25 isoField1.fits"
# x2 = file1.A.x2
# y2 = file1.A.y2



# scale the file and crop
# img = hdu.data[x1:x2, y1:y2]
# 1 pix = 0.768 ???

# bgn = 3100
# end = 6000
# for n in range(bgn,end, 10):
#     files = np.append(files, f"{path}/{n}.fits")
#     s = n / 1000
#     print(f'The program is proccessing {s} of {end / 1000}')
#     kernel = Gaussian2DKernel(x_stddev=s, y_stddev=s)
#     astropy_conv = convolve_fft(img, kernel)
#     fits.writeto(f'{path}/{n}.fits', astropy_conv, hdu.header, overwrite=True)
# fits.writeto(newpath, astropy_conv, hdu.header, overwrite=True)
# astropy_conv += shift
# fits.writeto(test, astropy_conv, hdu.header, overwrite=True)

# files = np.append(files, newpath)
# files = np.append(files, test)

# from astropy import units as u
# a = 2.4 * u.arcsec
# print(a.to(pix))

## quick test of some files
# files = np.append(files, '../fits/ForcastOne/B/Hankins Check/5.0_3290.fits' )
# files = np.append(files, '../fits/ForcastOne/B/Hankins Check/3290.fits' )
# oneAcollims = [390, 410, 0, 0.05] ## columnlimits = [xmin, xmax, ymin, ymax]
# oneArowlims = [240, 310, None, 0.05] ## rowlimits = [xmin, xmax, ymin, ymax]

# oneBcollims = [390, 420, 0, 0.04]
# oneBrowlims = [390, 440, 0, 0.04]
# MultiLinePlot(x1, y1, files, oneBcollims, oneBrowlims, legend=True)
# MultiLinePlot(x1, y1, files, collims, rowlims, colxmin=390, colxmax=410, colymin=0, colymax=0.05, rowxmin=240, rowxmax=310, rowymax=0.05, legend=True)


# noise floor 0.0235 jy/arcsec^2
#

def ConvolveShift(path, x, y, collims, rowlims, sigmashift, shift):
    sofia = "./fits/Forcast25_isoField1.fits"
    spit = "./fits/Reprojected Spitzer24 IsoFields @ Forcast25 isoField1.fits"

    hdu = fits.open(sofia)[0]


    # scale the file and crop
    # img = hdu.data[x1:x2, y1:y2]
    img = hdu.data
    # img = hdu.data[250:300, 360:410] * 3e5

    img[img > 1] = np.nan
    img[img < 0] = np.nan

    files = np.array([])
    files = [sofia, spit]

    # from astropy import units as u
    # a = 2.4 * u.arcsec
    # print(a.to(pix))

    ## quick test of some files
    # files = np.append(files, '../fits/ForcastOne/B/Hankins Check/5.0_3290.fits' )
    # files = np.append(files, '../fits/ForcastOne/B/Hankins Check/3290.fits' )
    from lineplots import MultiLinePlot, SingleLinePlot
    
    # MultiLinePlot(x1, y1, files, collims, rowlims, colxmin=390, colxmax=410, colymin=0, colymax=0.05, rowxmin=240, rowxmax=310, rowymax=0.05, legend=True)


    from astropy.stats import gaussian_fwhm_to_sigma
    from math import sqrt
    fwhm = sqrt((5.9**2)-(2.2**2))
    sigma = fwhm * 1.302 * gaussian_fwhm_to_sigma ## converts from arcseconds to pixels
    sigma += sigmashift
    print(f'sigma => {sigma}')

    # shift = 0.008 ## shift data up slightly

    kernel = Gaussian2DKernel(sigma)
    astropy_conv = convolve_fft(img, kernel)
    print(f'shift => {shift}')


    newpath = f"{path}/{floor(sigma * 1000)}.fits"
    test = f"{path}/shifted/{shift * 1000}_{floor(sigma * 1000)}.fits"


    fits.writeto(newpath, astropy_conv, hdu.header, overwrite=True)
    astropy_conv += shift
    fits.writeto(test, astropy_conv, hdu.header, overwrite=True)

    files = np.append(files, newpath)
    files = np.append(files, test)

    MultiLinePlot(x, y, files, collims, rowlims, legend=True)




