#include <stdio.h>

int main()
{
    double pi = 3.14159;
    double r;
    scanf("%lf", &r);
    double v = pi * (r*r*r) * (4.0/3.0);
    printf("VOLUME = %.3lf\n", v);
    return 0;
}
