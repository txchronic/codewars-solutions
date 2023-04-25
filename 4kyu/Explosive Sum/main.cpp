using ull = unsigned long long;

ull exp_sum(unsigned int n) {
    ull dp[n+1];
    dp[0] = 1;

    for (unsigned int i = 1; i <= n; i++) {
        dp[i] = 0;
    }

    for (unsigned int k = 1; k <= n; k++) {
        for (unsigned int i = k; i <= n; i++) {
        dp[i] += dp[i-k];
        }
    }

    return dp[n];
}