from math import prod


def part(n: int) -> str:
    def next_part(n: int, c = 1) -> int:
        yield [n]

        for i in range(c, n // 2 + 1):
            for j in next_part(n - i, i):
                yield [i] + j
    

    lst = sorted(set([prod(j) for j in next_part(n)]))
    rn, av = max(lst) - min(lst), sum(lst) / len(lst)

    if len(lst) % 2 != 0:
        med = lst[len(lst) // 2]
    else:
        med = (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
    
    return f"Range: {rn} Average: {'%.2f' % av} Median: {'%.2f' % med}"