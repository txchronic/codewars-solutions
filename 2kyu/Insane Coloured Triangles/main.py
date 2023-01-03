from math import log


dct = {
    "RR": "R", "GG": "G", "BB": "B",
    "BG": "R", "RB": "G", "RG": "B",
    "GB": "R", "BR": "G", "GR": "B"
}


def triangle(row: str) -> str:
    n = len(row)

    if n == 1:
        return row
    else:
        d = n - 3 ** int(log(n - 1, 3))

        return dct[triangle(row[:d]) + triangle(row[-d:])]