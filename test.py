#
# numpy 8 bit types refuse to inter-op via SWIG
import numpy as np
import example

# works
u8v = example.u8_vector(8)
print "u8 vector: uint8 %d" % example.average_u8(u8v)

# works
np_i = np.array([0, 2, 4, 6], dtype=np.int)
print "int %d" % example.average_i(np_i)

# fails
np_i8 = np.array([0, 2, 4, 6], dtype=np.int8)
print "int8 %d" % example.average_i8(np_i8)

# fails.
np_u8 = np.array([0, 2, 4, 6], dtype=np.uint8)
# this works
u8v = np_u8
# this prints as expected
print u8v
# now repeat as per line 8
print "uint8 %d" % example.average_u8(u8v)

