def descending_order(num: int) -> int:
    return int("".join(sorted([j for j in str(num)], reverse=True)))