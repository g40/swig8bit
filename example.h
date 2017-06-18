/* File : example.h */

#include <stdint.h>
#include <vector>
#include <algorithm>
#include <functional>
#include <numeric>

typedef char int8;

double average_u8(std::vector<unsigned char> v) {
  return std::accumulate(v.begin(), v.end(), 0.0)/v.size();
}

double average_i8(std::vector<char> v) {
  return std::accumulate(v.begin(), v.end(), 0.0)/v.size();
}

double average_i(std::vector<int> v) {
  return std::accumulate(v.begin(), v.end(), 0.0)/v.size();
}

std::vector<double> half(const std::vector<double>& v) {
  std::vector<double> w(v);
  for (unsigned int i=0; i<w.size(); i++)
    w[i] /= 2.0;
  return w;
}

void halve_in_place(std::vector<double>& v) {
  std::transform(v.begin(), v.end(), v.begin(),
                 std::bind2nd(std::divides<double>(), 2.0));
}
