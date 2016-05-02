#include <stdio.h>

#include <unistd.h>

#include <sys/types.h>

int main()
{
	int fd[5][2], nbytes;  
	int final=0;
        pid_t childpid[5]; 
     	int sum=0;
    	int arr[50];
	int i=0, j;
	for(int i=0;i<50;i++)
    		arr[i]=i;
	int k=0;
	i=0;
    for(k; k<5; k++)
       {
	pipe(fd[k]);
	childpid[k] = fork();	
	if(childpid[k] == 0)
        {     		
			for(j=0;j<10;j++)
				sum=sum+arr[(k*10)+j];	
			close(fd[k][0]);
 			write(fd[k][1], &sum, sizeof(sum));
			exit(0);
        }
     	else if(childpid[k] > 0)
        {		
		wait(NULL);
            	close(fd[k][1]);        
    		int value = 0;              
 		nbytes = read(fd[k][0], &value, sizeof(value)); 
          	final=final+value;
		printf ("\nSum after execution of %d process(es) is %d\n", k+1, final);
        }
       }
        return(0);
}
