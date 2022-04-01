import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import filetree as ft
import stars as st
from convolutions import ConvolveShift

parent = ft.FitsFolder()
parent += 'Combined Maps/'
output = parent + 'convolved/'

from astropy.stats import gaussian_fwhm_to_sigma
from math import sqrt
fwhm = sqrt((5.9**2)-(2.2**2))

sigma = fwhm * 1.302 * gaussian_fwhm_to_sigma ## converts from arcseconds to pixels
kernel = 1.5 - sigma

sofia = parent + 'isoOne.fits'
ConvolveShift(sofia, sofia, output, st.isoOne.A.x1, st.isoOne.A.y1, 0, 0)

sofia = parent + 'isoTwo.fits'
ConvolveShift(sofia, sofia, output, st.isoTwo.A.x1, st.isoTwo.A.y1, 0, 0)

sofia = parent + 'sgrb.fits'
ConvolveShift(sofia, sofia, output, st.sgrb.A.x1, st.sgrb.A.y1, 0, 0)