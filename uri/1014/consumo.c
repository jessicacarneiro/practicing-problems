#include <stdio.h>

int main()
{
    int km;
    double price;
    scanf("%d", &km);
    scanf("%lf", &price);
    printf("%.3lf km/l\n", ((double)km)/price);
    return 0;
}
