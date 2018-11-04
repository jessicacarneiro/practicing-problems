#include <stdio.h>

int main(int argc, char const *argv[])
{
    double a;
    double b;
    double c;
    scanf("%lf", &a);
    scanf("%lf", &b);
    scanf("%lf", &c);

    float p_a = 2.0;
    float p_b = 3.0;
    float p_c = 5.0;

    double media = (a*p_a + b*p_b + c*p_c)/(p_a + p_b + p_c);
    printf("MEDIA = %.1lf\n", media);

    return 0;
}
