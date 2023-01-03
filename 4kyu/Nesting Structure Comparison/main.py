def same_structure_as(original: list, other: list) -> bool:
    if (
        isinstance(original, list)
        and isinstance(other, list)
        and len(original) == len(other)
    ):
        for i, j in zip(original, other):
            if not same_structure_as(i, j):
                return False
        return True
    return not isinstance(original, list) and not isinstance(other, list)
