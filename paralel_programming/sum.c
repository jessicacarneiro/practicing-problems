#include <pthread.h>
#include <stdio.h>

int sum1; /* this data is shared by the thread(s) */
int sum2; /* this data is shared by the thread(s) */
void *runner1(void *param); /* the thread */
void *runner2(void *param);

int main(int argc, char const *argv[]) {
  pthread_t tid1; /* the thread identifier */
  pthread_attr_t attr1; /* set of thread attributes */
  pthread_t tid2; /* the thread identifier */
  pthread_attr_t attr2; /* set of thread attributes */

  if (argc != 2) {
    fprintf(stderr, "usage: a.out <integer value>\n");
  }
  if (atoi(argv[1]) < 0) {
    fprintf(stderr, "%d must be >= 0\n", atoi(argv[1]));
  }

  /* get the default attributes */
  pthread_attr_init(&attr1);
  pthread_attr_init(&attr2);
  /* create the thread */
  pthread_create(&tid1,&attr1,runner1,argv[1]);
  pthread_create(&tid2,&attr2,runner2,argv[1]);
  /* wait for the thread to exit */
  pthread_join(tid1,NULL);
  pthread_join(tid2,NULL);

  printf("sum = %d\n", sum1+sum2);

  return 0;
}

/* The thread will begin control in this function */
void *runner1(void *param) {
  int i, upper = atoi(param)/2;
  sum1 = 0;

  for (int i = 1; i < upper; i++) {
    sum1 += i;
  }

  pthread_exit(0);
}

/* The thread will begin control in this function */
void *runner2(void *param) {
  int i, upper = atoi(param);
  sum2 = 0;

  for (int i = atoi(param)/2; i <= upper; i++) {
    sum2 += i;
  }

  pthread_exit(0);
}
