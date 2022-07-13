import sys
sys.path.append('./Pixel Intensity Plots/modules/')
sys.path.append('./modules/')

import stars as st

import filetree as ft
from astropy.io import fits
file1 = st.isoOne
parent = ft.FitsFolder()
sofia = parent + 'Full Maps/'
sofia += 'F0217_FO_IMA_70030015_FORF253_MOS_0001-0348_final_MATT_Corrected.fits'
spit = parent + 'Full Maps/'
spit += 'Spitzer_GCmosaic_24um_onFORCASTheader_JyPix.fits'

path = parent + 'Full Maps/'
# import convolutions

# convolutions.ConvolveShiftPlot(sofia, spit, path, 1436, 3309, 1.15, 0)

coadd_path = path + 'shifteds/F0217_FO_IMA_70030015_FORF253_MOS_0001-0348_final_MATT_Corrected/0_1150.fits'

sofia_data = fits.open(sofia)[0].data
spitz_data = fits.open(spit)[0].data
coadd_data = fits.open(coadd_path)[0].data

import matplotlib.pyplot as plt
from lineplots import GetNthRow

yvalue = 4200
x, sofia_y = GetNthRow(sofia_data, yvalue)
x, spit_y = GetNthRow(spitz_data, yvalue)
x, coadd_y = GetNthRow(coadd_data, yvalue)

plt.plot(x, sofia_y, label='Sofia')
plt.plot(x, spit_y, label='Spitzer')
plt.plot(x, coadd_y, label='Coadd')
plt.legend()

plt.show()

