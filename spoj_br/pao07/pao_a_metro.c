#include <stdio.h>
#define MAX 10000

int main(int argc, char const *argv[])
{
  int i;
  int fatias, max_fatia = 0;
  int paes, pessoas;
  int tamanhos[MAX];

  // recebe as entradas
  scanf("%d", &pessoas);
  scanf("%d", &paes);

  for (i = 0; i < paes; ++i)
  {
    scanf("%d", &tamanhos[i]);
    max_fatia += tamanhos[i];
  }

  // tamanho máximo da fatia
  max_fatia /= pessoas;

  // diminui o tamanho da fatia até
  // conseguir o número necessário
  fatias = 0;
  while(fatias < pessoas) {
    fatias = 0;

    for (i = 0; i < paes; ++i)
    {
      fatias += tamanhos[i]/max_fatia;
    }

    if (fatias < pessoas)
    {
      max_fatia--;
    }
  }

  printf("%d\n", max_fatia);

  return 0;
}
