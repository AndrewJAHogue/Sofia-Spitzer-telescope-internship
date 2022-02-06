import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import Galactic

Forcast25_2 = fits.open("fits/Forcast25_isoField2.fits")[0]
Spitzer24_IsoFields = fits.open("fits/Spitzer24_IsoFields.fits")[0]

# masked_hdu2 = fits.open("fits/datamasked Spitzer24_isofields @ Forcast25_isofields1.fits")[0]


from reproject import reproject_interp
from matplotlib.colors import LogNorm
array2, footprint2 = reproject_interp(Spitzer24_IsoFields, Forcast25_2.header)

# forcast isofield 2
ax2 = plt.subplot(2,2,1, projection=WCS(Forcast25_2.header))
ax2.imshow(Forcast25_2.data, origin='lower', norm=LogNorm())
ax2.coords['ra'].set_axislabel('Right Ascension')
ax2.coords['dec'].set_axislabel('Declination')
ax2.set_title('Forcast25_isoField2')

# # the reprojected spitzer at isofield 2
ax3 = plt.subplot(2,2,2, projection=WCS(Forcast25_2.header))
ax3.imshow(array2, origin='lower', norm=LogNorm())
ax3.coords['ra'].set_axislabel('Right Ascension')
ax3.coords['dec'].set_axislabel('Declination')
ax3.set_title('Reprojected Spitzer24_IsoFields @ Forcast25_2')

# # mask nan's
bad = array2 < 0
withnans = np.copy(array2)
withnans[bad] = np.nan
combined_nans = withnans + Forcast25_2.data

# masked spitzer
ax4 = plt.subplot(2,2,3, projection=WCS(Forcast25_2.header))
ax4.imshow(combined_nans, origin='lower', norm=LogNorm())
ax4.coords['ra'].set_axislabel('Right Ascension')
ax4.coords['dec'].set_axislabel('Declination')
ax4.set_title('masked_nans_Spitzer24_IsoFields @ Forcast25_2')


withzeros = np.copy(array2)
withzeros[bad] = 0

combined_zeros = withzeros + Forcast25_2.data
# this is the plot of the reprojected spitzer data after sending it through a data mask, turning all <0 => 0's
ax5 = plt.subplot(2,2,4, projection=WCS(Forcast25_2.header))
ax5.imshow(combined_zeros, origin='lower', norm=LogNorm())
ax5.coords['ra'].set_axislabel('Right Ascension')
ax5.coords['dec'].set_axislabel('Declination')
ax5.set_title('Masked_zeros_Spitzer24_IsoFields + Forcast25_2')


fits.writeto("fits/Masked_zeros_Spitzer24_IsoFields + Forcast25_2.fits", combined_zeros, Forcast25_2.header, overwrite=True)


plt.subplots_adjust(hspace=0.7)
# plt.show()
