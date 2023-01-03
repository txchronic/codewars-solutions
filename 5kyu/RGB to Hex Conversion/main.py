def rgb(r: int, g: int, b: int) -> str:
    return "".join([
        hex(min(j, 255))[2:]
        if len(hex(max(min(j, 255), 0))[2:]) == 2
        else f"0{hex(max(min(j, 255), 0))[2:]}"
        for j in [r, g, b]
    ]).upper()