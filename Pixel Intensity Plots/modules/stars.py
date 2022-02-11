

import filetree as ft
path = ft.FitsFolder()
class isoOne:
    masked = path + "/Masked_zeros_Spitzer24_IsoFields + Forcast25_1.fits"
    sofia = path + "/Forcast25_isoField1.fits"
    spitzer = path + "/Reprojected Spitzer24 IsoFields @ Forcast25 isoField1.fits"
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
    sofia = path + "/Forcast25_isoField2.fits"
    spitzer = path + "/Reprojected Spitzer24 IsoFields @ Forcast25 isoField2.fits"
    # file = path + "/Masked_zeros_Spitzer24_IsoFields + Forcast25_2.fits"
    class A:
        x1 = 330
        x2 = 390
        y1 = 412
        y2 = 450

    class B:
        x1 = 295
        x2 = 326
        y1 = 312
        y2 = 340
    class C:
        x1 = 277
        x2 = 305
        y1 = 233
        y2 = 255
    class D:
        x1 = 301
        x2 = 336
        y1 = 200
        y2 = 224
    stars = [A, B, C, D]

class sgrb:
    sofia = path + "/Forcast25_SgrB.fits"
    spitzer = path + "/Reprojected Spitzer24_SgrB @ Forcast25_SgrB.fits"
    # file = path + "/datamasked Spitzer24_SgrB @ Forcast25_SgrB.fits"
    class A:
        x1 = 241
        x2 = 272
        y1 = 1043
        y2 = 1066
    class B:
        x1 = 340
        x2 = 375
        y1 = 965
        y2 = 1007
    class C:
        x1 = 343
        x2 = 360
        y1 = 911
        y2 = 930
    class D:
        x1 = 460
        x2 = 485
        y1 = 836
        y2 = 860
    class E:
        x1 = 228
        x2 = 290
        y1 = 735
        y2 = 808
    class F:
        x1 = 100
        x2 = 122
        y1 = 666
        y2 = 685
    class G:
        x1 = 440
        x2 = 485
        y1 = 673
        y2 = 700
    class H:
        x1 = 450
        x2 = 490
        y1 = 382
        y2 = 450
    class I:
        x1 = 430
        x2 = 545
        y1 = 260
        y2 = 370
    class J:
        x1 = 550
        x2 = 836
        y1 = 114
        y2 = 395

