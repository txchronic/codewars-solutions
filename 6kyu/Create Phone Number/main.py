def create_phone_number(n: list) -> str:
    n = list(map(lambda x: str(x), n))
    return f"({''.join(n[:3])}) {''.join(n[3:6])}-{''.join(n[6:])}"