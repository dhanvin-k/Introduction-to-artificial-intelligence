#include <stdio.h>
#include <string.h>
#include "student_code.c"

#define RED     "\x1b[31m"
#define GREEN   "\x1b[32m"
#define NORMAL  "\x1b[0m"

int main(int n, char **args)
{
	char msg[100]="good bye world!";
	get_msg(msg);
    printf("Message received: %s",msg);
    if (strcmp(msg,"hello world!"))
    {
        printf("(%sFail%s)\n",RED,NORMAL);
    }
    else
    {
        printf("(%sSuccess%s)\n",GREEN,NORMAL);
    }
        
	return strcmp(msg,"hello world!");
}
