def move_zeros(array: list) -> list:
    return [j for j in array if j != 0] + [0 for _ in range(array.count(0))]