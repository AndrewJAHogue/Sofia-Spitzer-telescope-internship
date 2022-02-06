import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import Galactic

forcast_rgb = fits.open("../fits/Forcast25_SgrB.fits")
spitzer_rgb = fits.open("../fits/Spitzer24_SgrB.fits")

masked_hdu = fits.open("../fits/datamasked Spitzer24_SgrB @ Forcast25_SgrB.fits")[0]

forc_hdu =forcast_rgb[0]
spit_hdu = spitzer_rgb[0]

from reproject import reproject_interp, reproject_adaptive, reproject_exact
from matplotlib.colors import LogNorm
array, footprint = reproject_adaptive(spit_hdu, forc_hdu.header)

# forcast isofield 2
ax2 = plt.subplot(2,2,1, projection=WCS(forc_hdu.header))
ax2.imshow(forc_hdu.data, origin='lower', norm=LogNorm())
ax2.coords['ra'].set_axislabel('Right Ascension')
ax2.coords['dec'].set_axislabel('Declination')
ax2.set_title('Forcast25_SgrB')

# # # forcast 2 scaled down by a factor of 7
# ax3 = plt.subplot(2,2,2, projection=WCS(forc_hdu.header))
# ax3.imshow(forc_hdu.data / 7, origin='lower', norm=LogNorm())
# ax3.coords['ra'].set_axislabel('Right Ascension')
# ax3.coords['dec'].set_axislabel('Declination')
# ax3.set_title('Forcast25_isoField2 // 7')

# # the reprojected spitzer at isofield 2
ax3 = plt.subplot(2,2,2, projection=WCS(forc_hdu.header))
ax3.imshow(array, origin='lower', norm=LogNorm())
ax3.coords['ra'].set_axislabel('Right Ascension')
ax3.coords['dec'].set_axislabel('Declination')
ax3.set_title('Reprojected Spitzer24_RBG @ forcast_rgb')


# COMBINING THE TWO MAPS
combined = array + forc_hdu.data
# masked spitzer
ax4 = plt.subplot(2,2,3, projection=WCS(forc_hdu.header))
ax4.imshow(combined, origin='lower', norm=LogNorm())
ax4.coords['ra'].set_axislabel('Right Ascension')
ax4.coords['dec'].set_axislabel('Declination')
ax4.set_title('Spitzer24_RGB + Forcast25_SgrB')

bad = array < 0
array[bad] = 0
# array = array / 10
forc_hdu.data = forc_hdu.data / 2.355

better_combined = array + forc_hdu.data
# this is the plot of the reprojected spitzer data after sending it through a data mask, turning all < 0 => np.nan's
ax5 = plt.subplot(2,2,4, projection=WCS(forc_hdu.header))
ax5.imshow(better_combined, origin='lower', norm=LogNorm())
ax5.coords['ra'].set_axislabel('Right Ascension')
ax5.coords['dec'].set_axislabel('Declination')
ax5.set_title('Masked_Spitzer24_RGB + Forcast25_SgrB')


# fits.writeto("fits/Reprojected Spitzer24_SgrB @ Forcast25_SgrB.fits", array, forc_hdu.header, overwrite=True)
# fits.writeto("fits/masked_spitzer_rgb + Forcast25_SgrB_scaled_down_2.355.fits", better_combined, forc_hdu.header, overwrite=True)


plt.subplots_adjust(hspace=0.7)
plt.show()
