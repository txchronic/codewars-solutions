def solution(number: int) -> int:
    return sum([j for j in range(number) if j % 3 == 0 or j % 5 == 0])