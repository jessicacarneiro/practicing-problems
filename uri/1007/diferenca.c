#include <stdio.h>

int main(int argc, char const *argv[])
{
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int diff = a * b - c * d;
    printf("DIFERENCA = %d\n", diff);
    return 0;
}
