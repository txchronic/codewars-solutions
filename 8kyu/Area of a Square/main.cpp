#include <math.h>
#include <cmath>

double square_area(double A)
{
    double r = A / (M_PI / 2);
    double area = pow(r, 2);
    return round(area * 100) / 100;
}