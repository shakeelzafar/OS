#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
void * MyThreadFunc(void * arg);
int main()
{
	int sum=0, i=0;	
	pthread_t t1, t2, t3, t4, t5;

	pthread_create(&t1, NULL, MyThreadFunc, 4);
	pthread_join(t1, &sum);
	i=i+sum;
	pthread_create(&t2, NULL, MyThreadFunc, 9);
	pthread_join(t2, &sum);
	i=i+sum;
	pthread_create(&t3, NULL, MyThreadFunc, 3);
	pthread_join(t3, &sum);
	i=i+sum;	
	pthread_create(&t4, NULL, MyThreadFunc, 2);
	pthread_join(t4, &sum);
	i=i+sum;
	pthread_create(&t5, NULL, MyThreadFunc, 5);
	pthread_join(t5, &sum);
	i=i+sum;

	printf("Final sum is %d\n",i);
	return 0;
}

void * MyThreadFunc(void * apg)
{
	int arg = (int *) apg;	
	int i=1;
	for(arg;arg>1;arg--)
		i=i*arg;
	pthread_exit(i);
}
