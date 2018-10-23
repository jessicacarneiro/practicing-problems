#include <stdio.h>

int main(int argc, const char *argv[])
{
  int diam;
  int alt, larg, prof;

  scanf("%d", &diam);
  scanf("%d %d %d", &alt, &larg, &prof);

  if(alt < diam || larg < diam || prof < diam) {
    printf("N\n");
  }
  else {
    printf("S\n");
  }

  return 0;
}
