def alphabet_position(text: str) -> str:
    string = "abcdefghijklmnopqrstuvwxyz"
    
    return " ".join([str(string.index(j.lower()) + 1) for j in text
                    if j.isalpha()])