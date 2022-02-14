from sgrb import sofia, spit, path, x1, y1, column_limits, row_limits, sigma_offset, shift

import sys
sys.path.append('./Pixel Intensity Plots/modules/')

from convolutions import ConvolveShift


ConvolveShift(sofia, spit, path, x1, y1, sigma_offset, shift, column_limits, row_limits)

