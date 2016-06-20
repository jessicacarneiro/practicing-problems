#include <stdio.h>
#define MAX_CASOS 1000

int main(int argc, const char *argv[])
{
  int resultados[MAX_CASOS];
  int i, j, n, op;

  j = 0;
  scanf("%d", &n);
  while(n != 0) {
    resultados[j] = 0;

    for (i = 0; i < n; i++) {
      scanf("%d", &op);
      resultados[j] += op;
    }
    j++;
    scanf("%d", &n);
  }

  for (i = 0; i < j; i++) {
    printf("Teste %d\n%d\n\n", i+1, resultados[i]);
  }

  return 0;
}
