
class isoOne:
    file = "../fits/Masked_zeros_Spitzer24_IsoFields + Forcast25_1.fits"
    # [starx, stary, xmax, ymax]
    # A = [270, 385, 290, 430]
    class A:
        x1 = 270
        x2 = 290
        y1 = 385
        y2 = 430
    # B = [335, 369]
    class B:
        x1 = 335
        x2 = 290
        y1 = 369
        y2 = 430
    # C = [414, 403]
    class C:
        x1 = 414
        y1 = 403
    stars = [A, B, C]

class isoTwo:
    file = "../fits/Masked_zeros_Spitzer24_IsoFields + Forcast25_2.fits"
    A = [330, 412]
    B = [295, 312]
    C = [277, 233]
    D = [301, 200]
    stars = [A, B, C, D]

class sgrb:
    file = "../fits/datamasked Spitzer24_SgrB @ Forcast25_SgrB.fits"
    A = [270, 385]
    B = [335, 369]
    C = [414, 403]
    D = [700, 300]

