#include <vector>
#include <algorithm>

int maxSequence(const std::vector<int>& arr) {
    if (arr.empty() || std::all_of(arr.begin(), arr.end(), [](int x){ return x < 0; })) {
        return 0;
    }

    int max_sum = arr[0];
    int curr_sum = arr[0];

    for (size_t i = 1; i < arr.size(); ++i) {
        curr_sum = std::max(curr_sum + arr[i], arr[i]);
        max_sum = std::max(max_sum, curr_sum);
    }

    return max_sum;
}
