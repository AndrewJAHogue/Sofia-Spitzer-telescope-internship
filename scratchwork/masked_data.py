from astropy.table import Table, Column, MaskedColumn
import numpy as np

# MaskedColumn object
# a = MaskedColumn([1, 2], name='a', mask=[False, True], dtype='i4')
# b = Column([3, 4], name='b', dtype='i8')
# print(Table([a, b]))

# numpy maskedarray; remember, the arrays are COLUMNS of data
a = np.ma.array([1, 2])
b = [3, 4]
t = Table([a, b], names=('a', 'b'), masked=True)
print(f"\nthe numpy maskedarray \n{t}\n")

# t = Table([(1, 2), (3, 4)], names=('a', 'b'), masked=True)
t['a'].mask = [False, True]  # Modify column mask (boolean array)
t['b'].mask = [True, False]  # Modify column mask (boolean array)
print(t)
t['a'].fill_value = 0
t['b'].fill_value = 0
print(f"\nthe numpy maskedarray \n{t.filled()}\n")

# directly using np.ma.masked elements; embedded is slower
# a = [1.0, np.ma.masked]
# b = [np.ma.masked, 'val']
# print(Table([a, b], names=('a', 'b')))
