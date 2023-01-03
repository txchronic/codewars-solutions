def first_non_repeating_letter(string: str) -> str:
	lst = [j for j in string if string.lower().count(j.lower()) == 1]

	if string == "" or (len(string) > 1 and not [j for j in lst if j != 1]):
		return ""
	else:
		return lst[0]
