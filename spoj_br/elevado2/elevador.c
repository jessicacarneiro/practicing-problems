#include <stdio.h>

int main(int argc, const char *argv[]) {
  int i;
  int capacidade, leituras;
  int entrada, saida;
  int total = 0;
  int excedeu = 0;

  scanf("%d %d", &leituras, &capacidade);

  for (i = 0; i < leituras; i++) {
    scanf("%d %d", &saida, &entrada);
    total += (-saida + entrada);
    if(total > capacidade) {
      excedeu = 1;
    }
  }

  if(!excedeu) {
    printf("N\n");
  }
  else {
    printf("S\n");
  }
  return 0;
}
