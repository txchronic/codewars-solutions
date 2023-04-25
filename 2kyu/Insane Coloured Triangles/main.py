def triangle(row: str) -> str:
    color_map = {
        "RR": "R", "GG": "G", "BB": "B",
        "BG": "R", "RB": "G", "RG": "B",
        "GB": "R", "BR": "G", "GR": "B"
    }

    length = len(row)

    if length == 1:
        return row
    else:
        third = 1
        while third <= length - 1:
            third *= 3
        third //= 3
        d = length - third

        return color_map[triangle(row[:d]) + triangle(row[-d:])]
