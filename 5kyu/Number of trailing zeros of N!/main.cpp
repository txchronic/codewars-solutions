long zeros(long n) {
    unsigned int count = 0;

    for (unsigned int i = 5; n / i >= 1; i *= 5) {
        count += n / i;
    }

    return count;
}
