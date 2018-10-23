#include <stdio.h>

int main(int argc, const char *argv[])
{
  int dist, ped;
  int custoDist, custoPed, custoTotal;

  scanf("%d %d", &dist, &ped);
  scanf("%d %d", &custoDist, &custoPed);

  custoTotal = dist*custoDist + custoPed*(dist/ped);
  printf("%d\n", custoTotal);

  return 0;
}
