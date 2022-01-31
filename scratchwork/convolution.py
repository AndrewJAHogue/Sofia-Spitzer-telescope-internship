import numpy as np
import matplotlib.pyplot as plt

from astropy.io import fits
from astropy.convolution import Gaussian2DKernel, convolve, interpolate_replace_nans, convolve_fft
from scipy.signal import convolve as scipy_convolve

from matplotlib.colors import LogNorm

hdu = fits.open("fits/Forcast25_isoField1.fits")[0]

# import lineplots as ln

# scale the file and crop
img = hdu.data * 2.4
# print(hdu.data[250:300, 360:410])
# img = hdu.data[250:300, 360:410] * 3e5

# set brightest pixel to NaN to simulate saturated data set
img[img > 1] = np.nan
img[img < 0] = np.nan

# copy of data and set those NaNs to zero; use for scipy convolution
img_zerod = img.copy()
img_zerod[np.isnan(img)] = 0

# We smooth with a Gaussian kernel with x_stddev=1 (and y_stddev=1)
# It is a 9x9 array
# kernel = Gaussian2DKernel(x_stddev=10.67, y_stddev=10.67)
kernel = Gaussian2DKernel(x_stddev=2.4, y_stddev=2.4)
astropy_conv = convolve_fft(img, kernel)

# convolution: scipy's conv. spreads out NaNs
# scipy_conv = scipy_convolve(img,kernel,mode='same',method='direct')

# scipy's direct conv. run on the zero'd img will not have NaNs but will have some very low value zones where they were
# scipy_conv_zerod = scipy_convolve(img_zerod,kernel,mode='same',method='direct')

# astropy's conv. replaces NaNs with kernel-weighted interpolation from neighbors
# astropy_conv = convolve(img, kernel)

# Now we do a bunch of plots.  In the first two plots, the originally masked
# values are marked with red X's
# plt.figure(1, figsize=(12, 12)).clf()
# ax1 = plt.subplot(2, 2, 1)
# im = ax1.imshow(img, vmin=-2., vmax=2.e1, origin='lower',interpolation='nearest', cmap='viridis')
# y, x = np.where(np.isnan(img))
# ax1.set_autoscale_on(False)
# ax1.plot(x, y, 'rx', markersize=4)
# ax1.set_title("Original")
# ax1.set_xticklabels([])
# ax1.set_yticklabels([])

# ax2 = plt.subplot(2, 2, 2)
# im = ax2.imshow(scipy_conv, vmin=-2., vmax=2.e1, origin='lower',interpolation='nearest', cmap='viridis')
# ax2.set_autoscale_on(False)
# ax2.plot(x, y, 'rx', markersize=4)
# ax2.set_title("Scipy")
# ax2.set_xticklabels([])
# ax2.set_yticklabels([])

# ax3 = plt.subplot(2, 2, 3)
# im = ax3.imshow(scipy_conv_zerod, vmin=-2., vmax=2.e1, origin='lower',interpolation='nearest', cmap='viridis')
# ax3.set_title("Scipy nan->zero")
# ax3.set_xticklabels([])
# ax3.set_yticklabels([])

# ax4 = plt.subplot(2, 2, 4)
# im = ax4.imshow(astropy_conv, vmin=-2., vmax=2.e1, origin='lower',interpolation='nearest', cmap='viridis')
# ax4.set_title("Default astropy")
# ax4.set_xticklabels([])
# ax4.set_yticklabels([])

# # we make a second plot of the amplitudes vs offset position to more
# # clearly illustrate the value differences
# plt.figure(2).clf()
# plt.plot(img[:, 25], label='input', drawstyle='steps-mid', linewidth=2,alpha=0.5)
# plt.plot(scipy_conv[:, 25], label='scipy', drawstyle='steps-mid',linewidth=2, alpha=0.5, marker='s')
# plt.plot(scipy_conv_zerod[:, 25], label='scipy nan->zero',drawstyle='steps-mid', linewidth=2, alpha=0.5, marker='s')
# plt.plot(astropy_conv[:, 25], label='astropy', drawstyle='steps-mid',linewidth=2, alpha=0.5)
# plt.ylabel("Amplitude")
# plt.ylabel("Position Offset")
# plt.legend(loc='best')
# plt.show()


# hdu.data[250:300, 360:410] = astropy_conv
# hdu.data = astropy_conv
# print(hdu.data[250:300, 360:410])



fits.writeto("fits/convolved-test-Forcast25_isofields1.fits", astropy_conv, hdu.header, overwrite=True)
