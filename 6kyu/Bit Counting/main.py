def count_bits(n: int) -> int:
    return len([j for j in f"{n:b}" if j == "1"])
