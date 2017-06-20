//
// http://scipy-cookbook.readthedocs.io/items/SWIG_NumPy_examples.html
//

%module example

%{
    #define SWIG_FILE_WITH_INIT
	#include "example.h"
%}

// https://raw.githubusercontent.com/numpy/numpy/master/tools/swig/numpy.i
%include "numpy.i"

%init %{
    import_array();
%}

//
%apply (char* INPLACE_ARRAY1, int DIM1) {(char* buffer, int bytes)}
%apply (unsigned char* INPLACE_ARRAY1, int DIM1) {(unsigned char* buffer, int bytes)}
%apply (int* INPLACE_ARRAY1, int DIM1) {(int* buffer, int bytes)}

// Include the header file with above prototypes
%include "example.h"
