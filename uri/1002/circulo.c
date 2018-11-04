#include <stdio.h>

int main(int argc, char const *argv[])
{
    double pi = 3.14159;
    double raio;
    scanf("%lf", &raio);
    printf("A=%.4lf\n", (raio*raio*pi));
    return 0;
}
