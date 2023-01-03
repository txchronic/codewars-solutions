def last_digit(lst: list) -> int:
    n = 1

    for i in reversed(lst):
        n = i ** (n if n < 4 else n % 4 + 4)

    return n % 10