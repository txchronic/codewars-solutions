from functools import lru_cache


@lru_cache(maxsize=None)
def exp_sum(n: int) -> int:
    parts = 0

    if n in [0, 1]:
        return 1
    else:
        for i in range(1, n + 1):
            p1 = n - int((i * (3 * i - 1)) / 2)
            p2 = n - int((i * (3 * i + 1)) / 2)
            sign = pow(-1, i + 1)
            parts += sign * (exp_sum(p1) + exp_sum(p2))

        return parts