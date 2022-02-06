import numpy as np
import matplotlib.pyplot as plt

from astropy.io import fits
from astropy.convolution import Gaussian2DKernel, convolve, interpolate_replace_nans
from scipy.signal import convolve as scipy_convolve

from matplotlib.colors import LogNorm

# size the convolved data with the original, so the holes match the missing data in the original
def TransformHole(input_data, xrangevalues, yrangevalues):
    data = input_data
    xmin = xrangevalues[0]
    xmax = xrangevalues[1]
    ymin = yrangevalues[0]
    ymax = yrangevalues[1]

    # # scale the file and crop
    # scaledimg = data[xmin:xmax, ymin:ymax] * .9e3

    # # set brightest pixel to NaN to simulate saturated data set
    # scaledimg[scaledimg > 2e1] = np.nan

    resizedarray = np.full((xmax,ymax), np.nan)
    for x in range(xmin,xmax):
        for y in range(0,ymax - ymin): # size of region
            resizedarray[x, y + ymin] = data[x - xmin,y]
    return resizedarray

def ConvoleSciPyZero(filename, xrangevalues, yrangevalues):
    hdu = fits.open(filename)[0]

    # scale the file and crop
    img = hdu.data[xrangevalues[0]:xrangevalues[1], yrangevalues[0]:yrangevalues[1]] * .9e3

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

    return combined

