import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import Galactic

forcast_rgb = fits.open("fits/Forcast25_SgrB.fits")
spitzer_rgb = fits.open("fits/Spitzer24_SgrB.fits")

masked_hdu = fits.open("fits/Masked_zeros_Spitzer24_IsoFields + Forcast25_1.fits")[0]


# data[y][x] is the format; to get columns first, see below
# chosenrow = 712
# row = masked_hdu.data[chosenrow]
# column = np.array([])
# for x in row:
#     column = np.append(column, x)
# # fake data, just indeces, basically; example had 'r' but I don't know what that is in this context
# ydata = np.array(range(len(column)))

# plt.plot(ydata, column)
# plt.show()

# to get columns of 2d array: data[:,'column'] where 'column' is the column you want
#       |     |
#       |     |
#       |     |
#       |_____|______x
#       y    x=some number
# chosencolumn = 712
# column = masked_hdu.data[:,chosencolumn]
# rows = np.array([])
# for y in column:
#     rows = np.append(rows, y)
# # fake x data
# xdata = np.array(range(len(column)))

# print(column[column>0.04])
# plt.plot(xdata, rows)
# plt.show()

def GetNthColumn(column):
    chosencolumn = column
    yvalues = masked_hdu.data[:,chosencolumn]
    # fake x data
    xdata = np.array(range(len(yvalues)))
    plt.plot(xdata, yvalues)

def GetNthRow(row):
    chosenrow = row
    xvalues = masked_hdu.data[chosenrow]
    # fake data, just indeces, basically; example had 'r' but I don't know what that is in this context
    ydata = np.array(range(len(xvalues)))
    plt.plot(ydata, xvalues)

GetNthRow(384)
plt.show()

