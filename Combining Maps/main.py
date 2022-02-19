import sys
sys.path.append('./Pixel Intensity Plots/modules/')
sys.path.append('./modules/')

from lineplots import MultiLinePlot
import stars as st
from filetree import FitsFolder

x = st.isoOne.A.x1
y = st.isoOne.A.y1
files = [FitsFolder() + 'Combined Maps/One.fits']

MultiLinePlot(x, y, files)

