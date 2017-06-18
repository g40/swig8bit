This repo demonstrates a regression or issue with SWIG where Numpy
arrays of dtype int8 and uint8 fail with `TypeError` when passed to a C++
function expecting input of type `std::vector`

```
#
# numpy 8 bit types refuse to inter-op via SWIG
import numpy as np
import example

# create a raw instance of a std::vector<unsigned char>
u8v = example.u8_vector(8)
print "u8 vector: uint8 %d" % example.average_u8(u8v)

# works for wrapper around std::vector<int>
np_i = np.array([0, 2, 4, 6], dtype=np.int)
print "int %d" % example.average_i(np_i)

# fails for wrapper around std::vector<char>
np_i8 = np.array([0, 2, 4, 6], dtype=np.int8)
print "int8 %d" % example.average_i8(np_i8)

# fails for wrapper around std::vector<unsigned char>
np_u8 = np.array([0, 2, 4, 6], dtype=np.uint8)
# this works
u8v = np_u8
# this prints as expected
print u8v
# now repeat as per line 8
print "uint8 %d" % example.average_u8(u8v)

```

`Linux ubuntu 4.4.0-78-generic #99-Ubuntu SMP Thu Apr 27 15:29:09 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux`
`gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4)`
`Python 2.7.12`
