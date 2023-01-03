def snail(snail_map: list) -> list:
    if not snail_map:
        return []
    else:
        return list(snail_map[0]) + snail(list(zip(*snail_map[1:]))[::-1])
