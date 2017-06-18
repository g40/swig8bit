%module example

%{
#include "example.h"
%}

%include stdint.i
%include "std_vector.i"
// Instantiate templates used by example
// typedef char int8;
namespace std {
  %template(u8_vector) vector<unsigned char>;
  %template(c_vector) vector<char>;
  %template(i_vector) vector<int>;
  %template() vector<double>;
}

// Include the header file with above prototypes
%include "example.h"
