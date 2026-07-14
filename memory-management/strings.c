#include <stdio.h>
#include <string.h>

int main(void)
{
    char helloWorld[100] = "Hello World";
    printf("%s\n", helloWorld);
    char c[24] = "I love ";
    strcat(c, "systems!");
    printf("%s\n", c);
    return 0;
}