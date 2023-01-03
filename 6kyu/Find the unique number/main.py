def find_uniq(arr: list) -> int:
    return [j for j in set(arr) if arr.count(j) == 1][0]