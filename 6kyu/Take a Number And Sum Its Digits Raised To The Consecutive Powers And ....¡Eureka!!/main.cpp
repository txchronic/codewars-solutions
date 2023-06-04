#include <vector>
#include <cmath>

std::vector<unsigned int> sumDigPow(unsigned int a, unsigned int b) {
    std::vector<unsigned int> result;

    for(unsigned int i = a; i <= b; i++){
        unsigned int sum = 0;
        unsigned int num_digits = floor(log10(i))+1;
        unsigned int temp = i;

        while (temp > 0) {
            unsigned int digit = temp % 10;

            sum += pow(digit,num_digits);
            num_digits--;
            temp /= 10;
        }

        if (sum == i) {
            result.push_back(i);
        }
    }

    return result;
}