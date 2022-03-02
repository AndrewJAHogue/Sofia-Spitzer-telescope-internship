import sys
sys.path.append('./Pixel Intensity Plots/modules/')
sys.path.append('./modules/')

from lineplots import MultiLinePlot
import stars as st
from filetree import FitsFolder

x = st.isoOne.A.x1
y = st.isoOne.A.y1
parent = FitsFolder()
combined = parent + 'Combined Maps/1.fits'
comparison = '/media/al-chromebook/USB20FD/Python/Research/ToGiveHankings/one/8.5_3036.fits'
files = [comparison, combined]

# x = st.isoTwo.A.x1
# y = st.isoTwo.A.y1
# files = [FitsFolder() + 'Combined Maps/Two.fits']

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