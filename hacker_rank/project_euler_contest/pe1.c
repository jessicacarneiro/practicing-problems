#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n;
    int * array;
    
    scanf("%d", &n);
    array = malloc(sizeof(int) * n);
    
    int previous = 0;
    int greater = 0;
    int greater_n = 0;
    for(int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
        int sum = 0;
        int k = 1;
        
        if(i > 0) {
            if(array[i-1] <= array[i]) {
                sum = previous;
                k = array[i-1];
            }
        }

        if(greater_n <= array[i]) {
            k = greater_n;
            sum = greater;
        }
        
        for(int j = k; j < array[i]; j++) {
            if(j % 3 == 0 || j % 5 == 0) {
                sum += j;
            }
        }
        previous = sum;
        if(sum > greater) {
            greater_n = array[i];
            greater = sum;
        }
        printf("%d\n", sum);
    }
    
    return 0;
}
