## this file is meant as a quick way to run python commands, for whatever project I'm doing. Anything I want to keep needs to be saved in its own file

# import numpy as np
# import matplotlib.pyplot as plt
from astropy.io import fits
# from astropy.wcs import WCS
# from astropy.coordinates import Galactic


Forcast25_isoField1 = fits.open("fits/Forcast25_isoField1.fits")[0]
Forcast25_isoField2 = fits.open("fits/Forcast25_isoField2.fits")[0]
Spitzer24_IsoFields = fits.open("fits/Spitzer24_IsoFields.fits")[0]
re_Spitzer24_IsoFields1 = fits.open("fits/Reprojected Spitzer24 IsoFields @ Forcast25 isoField1.fits")[0]
re_Spitzer24_IsoFields2 = fits.open("fits/Reprojected Spitzer24 IsoFields @ Forcast25 isoField2.fits")[0]

# forcast_rgb = fits.open("Forcast25_SgrB.fits")
# spitzer_rgb = fits.open("Spitzer24_SgrB.fits")

# print((forcast_rgb[0].shape))
# print((spitzer_rgb[0].shape))

# print(len(Forcast25_isoField1.data))
print(1 / .768)