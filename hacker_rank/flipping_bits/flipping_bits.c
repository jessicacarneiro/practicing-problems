#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n;
    unsigned int *arr;
    
    scanf("%d", &n);
    arr = malloc(sizeof(unsigned int) * n);
    
    for(int i = 0; i < n; i++) {
        scanf("%u", &arr[i]);
    }
    
    unsigned int mask = 4294967295; // 2^32 - 1
    for(int i = 0; i < n; i++) {
        unsigned int flipped = arr[i] ^ mask;
        printf("%u\n", flipped);
    }
    
    return 0;
}
