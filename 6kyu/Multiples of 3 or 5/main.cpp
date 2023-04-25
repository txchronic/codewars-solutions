int solution(int number) 
{
    number--;

    int num3 = number / 3;
    int num5 = number / 5;
    int num15 = number / 15;

    int sum3 = (num3 * (num3 + 1) / 2) * 3;
    int sum5 = (num5 * (num5 + 1) / 2) * 5;
    int sum15 = (num15 * (num15 + 1) / 2) * 15;

    return sum3 + sum5 - sum15;
}