#include <stdio.h>
#define MAX_QTD 1000

int main(int argc, const char *argv[])
{
  int i, j, n;
  int acumulado, total[MAX_QTD];
  int quantidade, tamanho;

  j = 0;
  scanf("%d", &n);
  while(n != 0) {

    total[j] = 0;
    acumulado = 0;

    for (i = 0; i < n; i++) {
      scanf("%d %d", &tamanho, &quantidade);
      if(quantidade/4 >= 1) {
        total[j] += quantidade/4;
        quantidade = quantidade % 4;
      }
      if(quantidade == 2 || quantidade == 3){
        if(acumulado == 0) {
          acumulado += 2;
        }
        else {
          acumulado -= 2;
          total[j]++;
        }
      }
    }

    scanf("%d", &n);
    j++;
  }

  for (i = 0; i < j; i++) {
    printf("%d\n", total[i]);
  }

  return 0;
}
