#include <stdio.h>

int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        int n; 
        int max; 
        scanf("%d %d",&n,&max);
        
        unsigned int bigger = 0;
        for(int j = 0; j <= n; j++) {
            for(int k = j+1; k <= n; k++) {
                unsigned int bitwise = j & k;
                if(bitwise > bigger && bitwise < max) {
                    bigger = bitwise;
                }
            }
        }
        printf("%d\n", bigger);
    }
    return 0;
}
