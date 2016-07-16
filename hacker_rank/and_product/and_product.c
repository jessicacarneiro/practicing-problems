#include <stdio.h>
#include <stdlib.h>

int main() {

    unsigned int n;
    unsigned int * numbers;
    
    scanf("%d", &n);
    numbers = malloc(sizeof(unsigned int) * n * 2);
    
    for(int i = 0; i < n; i++) {
        scanf("%u %u", &numbers[i], &numbers[i+1]);
        unsigned int bit_and = numbers[i];
        for(int j = numbers[i]+1; j <= numbers[i+1]; j++) {
            bit_and = bit_and & j;
        }
        printf("%u\n", bit_and);
    }
    
    return 0;
}
