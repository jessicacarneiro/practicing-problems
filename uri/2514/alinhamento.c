#include <stdlib.h>
#include <stdio.h>

int gcd(int a, int b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    if (b) while ((a %= b) && (b %= a));
    return (a + b);
}

int lcm(int a, int b, int c) {
    int r = (a*b) / gcd(a, b);
    return (c*r) / gcd(r, c);
}

int main() {
    char line[500];
    int a, b, c, m;
    int solutions[9999];
    int n = 0;
    
    while (fgets(line, sizeof(line), stdin) != NULL)
    {
        sscanf(line, "%d", &m);
        fgets(line, sizeof(line), stdin);
        sscanf(line, "%d %d %d", &a, &b, &c);
        solutions[n++] = abs(m - lcm(a, b, c));
    }

    for (int i = 0; i < n; i++)
        printf("%d\n", solutions[i]);

    return 0;
}