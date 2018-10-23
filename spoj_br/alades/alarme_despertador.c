#include <stdio.h>
#define MAX_CASOS 1000

int main(int argc, const char *argv[]) {
  int i = 0, j;
  int h1, h2, m1, m2;
  int saida[MAX_CASOS];

  scanf("%d %d %d %d", &h1, &m1, &h2, &m2);
  while(h1 != 0 || m1 != 0 || h2 != 0 || m2 != 0) {
    if(h1 < h2) {
      if(m1 <= m2) {
        saida[i] = 60*(h2 - h1) + (m2 - m1);
      }
      else {
        saida[i] = 60*(h2 - h1 - 1) + (60 - m1 + m2);
      }
    }
    else if (h1 == h2) {
      if(m1 <= m2) {
        saida[i] = m2 - m1;
      }
      else {
        saida[i] = 60*(24 - h1 + h2 - 1) + (60 - m1 + m2);
      }
    }
    else {
      if(m1 <= m2) {
        saida[i] = 60*(24 - h1 + h2) + (m2 - m1);
      }
      else {
        saida[i] = 60*(24 - h1 + h2 - 1) + (60 - m1 + m2);
      }

    }
    scanf("%d %d %d %d", &h1, &m1, &h2, &m2);
    i++;
  }

  for (j = 0; j < i; j++) {
    printf("%d\n", saida[j]);
  }
  return 0;
}
