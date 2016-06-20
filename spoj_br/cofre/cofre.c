#include <stdio.h>
#define MAX_CASOS 1000
#define MAX_DEP    100

int main(int argc, const char *argv[])
{
  int depositos[MAX_CASOS][MAX_DEP+1];
  int a, b;
  int i, j, k, m, n;
  int dif;

  j = 0;
  scanf("%d", &n);
  while(n != 0) {
    depositos[j][0] = n;

    k = 1;
    for (i = 0; i < n; i++) {
      scanf("%d %d", &a, &b);
      depositos[j][k] = a - b;
      k++;
    }
    scanf("%d", &n);
    j++;
  }

  for (i = 0; i < j; i++) {
    printf("Teste %d\n", i+1);

    dif = 0;
    for (k = 1; k <= depositos[i][0]; k++) {
      dif += depositos[i][k];
      printf("%d\n", dif);
    }
    printf("\n");
  }

  return 0;
}
