#include <string>
#include <vector>

std::string range_extraction(std::vector<int> args) {
    std::string result;
    int i = 0;
    while (i < args.size()) {
        int j = i;

        while (j + 1 < args.size() && args[j + 1] == args[j] + 1)
            j++;
    
        if (j == i) {
            result += std::to_string(args[i]);

            if (i != args.size() - 1)
                result += ",";
        } else if (j == i + 1) {
            result += std::to_string(args[i]) + "," + std::to_string(args[j]);

            if (j != args.size() - 1)
                result += ",";
        } else {
            result += std::to_string(args[i]) + "-" + std::to_string(args[j]);

            if (j != args.size() - 1)
                result += ",";
        }

        i = j + 1;
    }

    return result;
}
