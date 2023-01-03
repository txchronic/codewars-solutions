def generate_hashtag(s: str) -> str:
    if s == "" or len(s) > 140:
        return False
    else:
        return f"#{''.join([j.capitalize() for j in s.split(' ')])}"