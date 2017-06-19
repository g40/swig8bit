#
# numpy 8 bit types refuse to inter-op via SWIG
# after cookbook recipe here:
# http://scipy-cookbook.readthedocs.io/items/SWIG_NumPy_examples.html

import numpy as np
import example

# fails
np_i8 = np.array([0, 2, 4, 6], dtype=np.int8)
avg = example.average_s8(np_i8.data,np_i8.size)
print "int8 %d" % avg

# fails.
np_u8 = np.array([0, 2, 4, 6], dtype=np.uint8)
avg = example.average_u8(np_u8.data,np_u8.size)
print "int8 %d" % avg

# 
np_i = np.array([0, 2, 4, 6], dtype=np.int)
avg = example.average_i(np_i.data,np_i.size)
print "int %d" % avg

