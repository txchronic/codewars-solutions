#include <string>

using std::string;

string repeat_str(size_t repeat, const string& str) {
  string s;
  
  while (repeat--) {
    s += str;
  }
  
  return s;
}