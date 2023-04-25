from math import prod
from typing import List

def part(n: int) -> str:
    def next_partition(n: int, start = 1) -> List[List[int]]:
        yield [n]

        for i in range(start, n // 2 + 1):
            for j in next_partition(n - i, i):
                yield [i] + j

    partitions = sorted(set([prod(j) for j in next_partition(n)]))
    range_num = max(partitions) - min(partitions)
    average = sum(partitions) / len(partitions)

    if len(partitions) % 2 != 0:
        median = partitions[len(partitions) // 2]
    else:
        median = (partitions[len(partitions) // 2] + partitions[len(partitions) // 2 - 1]) / 2

    return f"Range: {range_num} Average: {'%.2f' % average} Median: {'%.2f' % median}"
