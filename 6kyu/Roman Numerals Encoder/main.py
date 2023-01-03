def solution(n: int) -> str:
	x = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
		(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
	y = ""

	while n > 0:
		for i, j in x:
			while n >= i:
				y += j
				n -= i
	return y