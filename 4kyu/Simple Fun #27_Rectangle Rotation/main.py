def rectangle_rotation(a: int, b: int) -> int:
    a, b = int(a / (2 ** 0.5)), int(b / (2 ** 0.5))

    if (a % 2 == 0 and b % 2 == 0) or (a % 2 == 1 and b % 2 == 1):
        return a * b + (a + 1) * (b + 1)
    
    return a * (b + 1) + (a + 1) * b