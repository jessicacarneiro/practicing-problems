#include <stdio.h>

int main(int argc, char const *argv[])
{
    float a;
    float b;
    scanf("%f", &a);
    scanf("%f", &b);

    float p_a = 3.5;
    float p_b = 7.5;

    double media = (a*p_a + b*p_b)/(p_a + p_b);
    printf("MEDIA = %.5lf\n", media);

    return 0;
}
