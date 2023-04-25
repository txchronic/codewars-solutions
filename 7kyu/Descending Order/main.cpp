#include <algorithm>
#include <string>

uint64_t descendingOrder(uint64_t a) {
    std::string a_str = std::to_string(a);
    std::sort(a_str.begin(), a_str.end(), std::greater<char>());
    return std::stoull(a_str);
}