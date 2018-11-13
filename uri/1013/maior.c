#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    int maiorAB = (a + b + abs(a-b))/2;
    int maiorAC = (a + c + abs(a-c))/2;
    if (maiorAB > maiorAC)
        printf("%d eh o maior\n", maiorAB);
    else
        printf("%d eh o maior\n", maiorAC);
    return 0;
}