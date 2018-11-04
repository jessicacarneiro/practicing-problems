#include <stdio.h>

int main(int argc, char const *argv[])
{
    int n, hours;
    float value;
    scanf("%d %d %f", &n, &hours, &value);
    printf("NUMBER = %d\n", n);
    printf("SALARY = U$ %.2f\n", hours * value);

    return 0;
}
