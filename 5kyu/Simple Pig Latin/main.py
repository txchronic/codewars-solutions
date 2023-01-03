def pig_it(text: str) -> str:
	return " ".join([j[1:] + j[0] + "ay"
                     if j.isalpha() else j for j in text.split()])