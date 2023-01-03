def friend(x: list) -> list:
    return list(filter(lambda y: len(y) == 4, x))