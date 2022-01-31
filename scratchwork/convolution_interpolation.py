import numpy as np
import matplotlib.pyplot as plt

from astropy.io import fits
from astropy.convolution import Gaussian2DKernel, convolve, interpolate_replace_nans
from scipy.signal import convolve as scipy_convolve

from matplotlib.colors import LogNorm

xholes = [[400,430],[300,400],[260,290],[500,530],[570,600],[400,430]]
yholes = [[400,430],[350,400],[370,400],[200,230],[80,120],[500,530]]

hdu = fits.open("Forcast25_isoField1.fits")[0]

# scale the file and crop
img = hdu.data[xholes[1][0]:xholes[1][1], yholes[1][0]:yholes[1][1]] * 1e5

# set brightest pixel to NaN to simulate saturated data set
img[img > 2e1] = np.nan

# copy of data and set those NaNs to zero; use for scipy convolution
img_zerod = img.copy()
img_zerod[np.isnan(img)] = 0

# We smooth with a Gaussian kernel with x_stddev=1 (and y_stddev=1)
# It is a 9x9 array
kernel = Gaussian2DKernel(x_stddev=1,x_size=63,y_size=63)

# convolution: scipy's conv. spreads out NaNs
scipy_conv = scipy_convolve(img,kernel,mode='same',method='direct')

# scipy's direct conv. run on the zero'd img will not have NaNs but will have some very low value zones where they were
scipy_conv_zerod = scipy_convolve(img_zerod,kernel,mode='same',method='direct')

# astropy's conv. replaces NaNs with kernel-weighted interpolation from neighbors
astropy_conv = convolve(img, kernel)

combined = scipy_conv_zerod + img



from MiscFunctions import TransformHole
# from MiscFunctions import TransformHole
hole = TransformHole(combined, xholes[1],yholes[1])

# fits.writeto(f"interpolated hole 2 Spitzer24_isofields @ Forcast25_isofields1.fits", combined, hdu.header, overwrite=True)
