def find_missing_letter(chars):
    lst = [ord(j) for j in chars]
    symb = "".join([chr(x) for x in range(lst[0], lst[-1] + 1)
                        if x not in lst])

    if all([j.isupper() for j in chars]):
        return symb.upper()
    return symb