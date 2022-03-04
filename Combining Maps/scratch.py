import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import filetree as ft
import stars as st

sofia1 = st.isoOne.sofia

name = sofia1.find('.fits')
slashes = sofia1.find('//') + 2
print(sofia1[slashes:name])