
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import Galactic

Forcast25_isoField1 = fits.open("../fits/Forcast25_isoField1.fits")
Spitzer24_IsoFields = fits.open("../fits/Spitzer24_IsoFields.fits")

# masked_hdu1 = fits.open("fits/datamasked Spitzer24_isofields @ Forcast25_isofields1.fits")[0]
# masked_hdu2 = fits.open("fits/datamasked Spitzer24_isofields @ Forcast25_isofields1.fits")[0]

spits_iso_hdu = Spitzer24_IsoFields[0]
Forcast25_1=Forcast25_isoField1[0]

print(spits_iso_hdu.header)