#include <stdlib.h>
#include <stdio.h>

#define MAX 40

void fib(int *values, int *calls) {
    // initial values
    values[0] = 0;
    values[1] = 1;

    // initial # of calls
    calls[0] = 0;
    calls[1] = 0;
    calls[2] = 2;

    for(int i = 2; i < MAX; i++) {
        values[i] = values[i-1] + values[i-2];
        calls[i] = calls[i-2] + calls[i-1] + 2;
    }
}

void main() {
    int n_tests;
    scanf("%d", &n_tests);
    
    int cases[MAX];
    int calls[MAX];
    int values[MAX];

    for(int i = 0; i < n_tests; i++) {
        scanf("%d", &cases[i]);
    }

    fib(values, calls);

    for(int i = 0; i < n_tests; i++) {
        printf("fib(%d) = %d calls = %d\n", cases[i], calls[cases[i]], values[cases[i]]);
    }
}