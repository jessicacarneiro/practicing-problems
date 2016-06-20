#include <stdio.h>
#include <math.h>

int main(int argc, const char *argv[])
{
  int primo;

  scanf("%d", &primo);

  if(primo == 0 || primo == 1) {
    printf("nao\n");
    return 0;
  }

  for (int i = 2; i <= sqrt(primo); i++) {
    if(primo % i == 0) {
      printf("nao\n");
      return 0;
    }
  }

  printf("sim\n");
  return 0;
}
