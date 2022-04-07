import sys
sys.path.append('./modules/')
sys.path.append('./Pixel Intensity Plots/modules/')

import numpy as np
from astropy.io import fits

import lineplots as plt
import filetree as ft
import stars as st

def SmallExposureMap(data, full_exposure):
    new_ex = np.full_like(data, np.nan)
    why = full_exposure.shape[0] - data.shape[0] - 1
    for j, y in enumerate(full_exposure):
        if j < data.shape[0] - 1:
            for i, x in enumerate(y):
                if i < data.shape[1] - 1:
                    new_ex[j][i] = full_exposure[why][i]
            why += 1
    return new_ex

parent = ft.FitsFolder()