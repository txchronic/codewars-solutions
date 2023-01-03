from itertools import chain


def list_squared(m: int, n: int) -> list:
    lst = []

    for i in range(m, n + 1):
        divs = list(set(
            chain(*((j, i // j)
            for j in range(1, int(i ** 0.5) + 1)
            if i % j == 0))
        ))

        sums = sum([j ** 2 for j in divs])

        if sums ** 0.5 % 1 == 0:
            lst.append([i, sums])

    return lst