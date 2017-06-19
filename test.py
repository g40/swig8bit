#
# numpy 8 bit types refuse to inter-op via SWIG
# after cookbook recipe here:
# http://scipy-cookbook.readthedocs.io/items/SWIG_NumPy_examples.html

import numpy as np
import example
import sys, traceback

# 
np_i = np.array([0, 2, 4, 6], dtype=np.int)
try:
	avg = example.average_i(np_i)
except Exception:
	traceback.print_exc(file=sys.stdout)
try:
	avg = example.average_i(np_i.data,np_i.size)
except Exception:
	traceback.print_exc(file=sys.stdout)


# fails
np_i8 = np.array([0, 2, 4, 6], dtype=np.int8)
try:
	avg = example.average_s8(np_i8)
except Exception:
	traceback.print_exc(file=sys.stdout)
try:
	avg = example.average_s8(np_i8.data,np_i8.size)
except Exception:
	traceback.print_exc(file=sys.stdout)

# fails.
np_u8 = np.array([0, 2, 4, 6], dtype=np.uint8)
avg = example.average_u8(np_u8.data,np_u8.size)
print "int8 %d" % avg


