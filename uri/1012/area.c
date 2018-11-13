#include <stdio.h>

int main()
{
    double pi = 3.14159;
    double a, b, c;
    scanf("%lf %lf %lf", &a, &b, &c);
    double tri = (a*c)/2.0;
    double cir = pi * c * c;
    double tra = (a + b)*c/2.0;
    double qua = b * b;
    double ret = a * b;
    printf("TRIANGULO: %.3lf\nCIRCULO: %.3lf\nTRAPEZIO: %.3lf\nQUADRADO: %.3lf\nRETANGULO: %.3lf\n",
          tri, cir, tra, qua, ret);
    return 0;
}
