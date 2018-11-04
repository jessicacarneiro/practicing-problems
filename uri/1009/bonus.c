#include <stdio.h>

int main(int argc, char const *argv[])
{
    char name[200];
    double salary, sales;
    scanf("%s", name);
    scanf("%lf %lf", &salary, &sales);

    printf("TOTAL = R$ %.2lf\n", salary + 0.15*sales);

    return 0;
}
