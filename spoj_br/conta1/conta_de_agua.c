#include <stdio.h>

int main(int argc, const char *argv[])
{
  int consumo;
  int total;
  int faixa[3];

  scanf("%d", &consumo);
  if(consumo <= 10) {
    total = 7;
  }
  else if(consumo > 10 && consumo <= 30) {
    faixa[0] = 7;
    faixa[1] = consumo - 10;
    total = faixa[0] + faixa[1];
  }
  else if(consumo > 30 && consumo <= 100) {
    faixa[0] = 7;
    faixa[1] = 20;
    faixa[2] = (consumo - 30)*2;
    total = faixa[0] + faixa[1] + faixa[2];
  }
  else if(consumo > 100) {
    faixa[0] = 7;
    faixa[1] = 20;
    faixa[2] = 140;
    total = faixa[0] + faixa[1] + faixa[2] + (consumo - 100)*5;
  }

  printf("%d\n", total);
}
