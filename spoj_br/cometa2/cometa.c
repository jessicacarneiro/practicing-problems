#include <stdio.h>

int main(int argc, const char *argv[])
{
  int ano, proximo;

  scanf("%d", &ano);

  proximo = 1986;
  while(proximo <= ano) {
    proximo += 76;
  }

  printf("%d\n", proximo);
  return 0;
}
