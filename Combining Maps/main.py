import sys
sys.path.append('./Pixel Intensity Plots/modules/')
sys.path.append('./modules/')

from lineplots import MultiLinePlot
import stars as st
from filetree import FitsFolder
parent = FitsFolder()

x = st.sgrb.A.x1
y = st.sgrb.A.y1
# combined = parent + 'Combined Maps/sgrb.fits'
combined2 = parent + 'Combined Maps/sgrb_spitmask.fits'
combined3 = parent + 'Combined Maps/sgrb_sofiamask.fits'
comparison = '/media/al-chromebook/USB20FD/Python/Research/ToGiveHankings/sgrb/15.0_3036.fits'
files = [comparison, combined3, combined2] 


# x = st.isoTwo.A.x1
# y = st.isoOne.A.y1
# combined = parent + 'Combined Maps/isoTwo.fits'
# comparison = '/media/al-chromebook/USB20FD/Python/Research/ToGiveHankings/two/12.0_3031.fits'
# files = [comparison, combined]


# x = st.isoOne.A.x1
# y = st.isoOne.A.y1
# combined = parent + 'Combined Maps/isoOne.fits'
# comparison = '/media/al-chromebook/USB20FD/Python/Research/ToGiveHankings/one/8.5_3036.fits'
# files = [comparison, combined]


MultiLinePlot(x, y, files, legend=True)


# --------notes----------------
# mask = np.where(sptiz > x)
# spit_mask = spitz[mask]
# sofia_mask = forcast[mask]
# 
# then swap the logic if you want to test that
# mask = np.where(sofia > x)
# sofia_mask = sofia[mask]
# ...
# ...
# np.nanmean([spitzmask, sofiamask], axis=0)