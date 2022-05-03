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

from reproject import reproject_interp
from matplotlib.colors import LogNorm
array, footprint = reproject_interp(Spitzer24_IsoFields, Forcast25_1.header)

combined = array + Forcast25_1.data

plt.rcParams.update({'font.size': 27})
# forcast isofield 1
ax2 = plt.subplot(1,2,1, xlabel='Galactic Longitude', ylabel='Galactic Latitude')
ax2.imshow(spits_iso_hdu.data, origin='lower', norm=LogNorm())
# ax2.coords['deg'].set_axislabel('Longitude')
# ax2.coords['deg'].set_axislabel('Latitude')
ax2.set_title('Spitzer')

# the reprojected isofield 1
ax3 = plt.subplot(1,2,2, projection=WCS(Forcast25_1.header))
ax3.imshow(array, origin='lower', norm=LogNorm())
ax3.coords['ra'].set_axislabel('Right Ascension')
ax3.coords['dec'].set_axislabel('Declination')
ax3.set_title('Reprojected Spitzer24_IsoFields @ Forcast25_1')
            
# # the combined final
# ax4 = plt.subplot(2,2,3, projection=WCS(Forcast25_1.header))
# ax4.imshow(combined, origin='lower', norm=LogNorm())
# ax4.coords['ra'].set_axislabel('Right Ascension')
# ax4.coords['dec'].set_axislabel('Declination')
# ax4.set_title('Reprojected Spitzer24_IsoFields + Forcast25_1')

# # replacing supersaturated data with nan's or 0's
# # # mask nan's
# bad = array < 0
# # withnans = np.copy(array)
# # withnans[bad] = np.nan

# # combined_nans = withnans + Forcast25_1.data

# # # the combined final, but bad data covered with nans
# # ax4 = plt.subplot(2,2,3, projection=WCS(Forcast25_1.header))
# # ax4.imshow(combined_nans, origin='lower', norm=LogNorm())
# # ax4.coords['ra'].set_axislabel('Right Ascension')
# # ax4.coords['dec'].set_axislabel('Declination')
# # ax4.set_title('Masked_nans_Spitzer24_IsoFields + Forcast25_1')

# withzeros = np.copy(array)
# withzeros[bad] = 0

# combined_zeros = withzeros + Forcast25_1.data
# # this is the plot of the reprojected spitzer data after sending it through a data mask, turning all <0 => np.nan's
# ax5 = plt.subplot(2,2,4, projection=WCS(Forcast25_1.header))
# ax5.imshow(combined_zeros, origin='lower', norm=LogNorm())
# ax5.coords['ra'].set_axislabel('Right Ascension')
# ax5.coords['dec'].set_axislabel('Declination')
# ax5.set_title('Masked_zeros_Spitzer24_IsoFields + Forcast25_1')


plt.subplots_adjust(hspace=0.7)
plt.show()
bad = Forcast25_1.data == np.nan
# print(bad)

# fits.writeto("fits/Masked_zeros_Spitzer24_IsoFields + Forcast25_1.fits", combined_zeros, Forcast25_1.header, overwrite=True)