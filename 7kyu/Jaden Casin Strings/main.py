def to_jaden_case(string: str) -> str:
    return " ".join([j.capitalize() for j in string.split()])