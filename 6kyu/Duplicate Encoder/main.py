def duplicate_encode(word: str) -> str:
    return "".join(["(" if word.lower().count(j) == 1 else ")" for j in word.lower()])