#include <stdio.h>

int main(int argc, const char *argv[])
{
  int n, valor;
  int soma = 0;

  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &valor);
    soma += valor;
  }

  printf("%d\n", soma);
  return 0;
}
