#include <string>

std::string incrementString(const std::string& str) {
    int i = str.size() - 1;

    while (i >= 0 && std::isdigit(str[i])) {
        i--;
    }

    std::string suffix = str.substr(i + 1);

    int j = suffix.size() - 1;
    while (j >= 0 && suffix[j] == '9') {
        suffix[j] = '0';
        j--;
    }

    if (j < 0) {
        suffix.insert(0, "1");
    } else {
        suffix[j]++;
    }

    return str.substr(0, i + 1) + suffix;
}
