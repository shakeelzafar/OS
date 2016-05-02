#include <stdio.h>
int main()
{
 FILE *f2, *fopen();
 f2 = fopen("file.txt","w");
 /*Create a file and add text*/
 fprintf(f2,"%s","This is just an example :)"); /*writes data to the file*/
 fclose(f2); /*done!*/
 return 0;
}
