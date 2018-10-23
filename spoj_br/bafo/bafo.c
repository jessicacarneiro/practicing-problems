#include <stdio.h>
#define MAX_CASOS 100000

int main(int argc, const char *argv[])
{
  int i, j, n;
  int a, b;
  int totalA, totalB;
  int saida[MAX_CASOS];

  j = 0;
  scanf("%d", &n);
  while(n != 0) {
    totalA = 0;
    totalB = 0;
    for (i = 0; i < n; i++) {
      scanf("%d %d", &a, &b);
      totalA += a;
      totalB += b;
    }
    if(totalA > totalB) {
      saida[j] = 1;
    }
    else {
      saida[j] = 2;
    }
    j++;
    n--;
    scanf("%d", &n);
  }

  for (i = 0; i < j; i++) {
    printf("Teste %d\n", i+1);
    if(saida[i] == 1) {
      printf("Aldo\n\n");
    }
    else {
      printf("Beto\n\n");
    }
  }

  return 0;
}
