from astropy.table import Table, Column, MaskedColumn
import numpy as np
import matplotlib.pyplot as plt

from astropy.io import fits

hdu1 = fits.open("fits/Reprojected Spitzer24 IsoFields @ Forcast25 isoField1.fits")[0]
hdu2 = fits.open("fits/Reprojected Spitzer24 IsoFields @ Forcast25 isoField2.fits")[0]
hdu3 = fits.open("fits/Reprojected Spitzer24_SgrB @ Forcast25_SgrB.fits")[0]

## old method; slow!
# for x in range(0,len(hdu.data)):
#     for item in range(0, len(hdu.data[x])):
#         if hdu.data[x][item] < 0:
#             print(hdu.data[x][item])
#             hdu.data[x][item] = 0

# much faster method!
# bad1 = hdu1.data < 0
# hdu1.data[bad1] = np.nan

# bad2 = hdu2.data < 0
# hdu2.data[bad2] = np.nan

bad3 = hdu3.data < 0
hdu3.data[bad3] = np.nan

# fits.writeto(f"fits/datamasked Spitzer24 @ Forcast25_isofield1.fits", hdu1.data, hdu1.header, overwrite=True)
# fits.writeto(f"fits/datamasked Spitzer24 @ Forcast25_isofield2.fits", hdu2.data, hdu2.header, overwrite=True)
# fits.writeto(f"fits/datamasked Spitzer24_SgrB @ forcast_rgb.fits", hdu3.data, hdu3.header, overwrite=True)