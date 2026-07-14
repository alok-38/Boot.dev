#include <stdio.h>

char *does_not_exist(char expression[]);

int main() {
    printf("starting sneklang tools\n");

    printf("%s\n", does_not_exist("uh oh"));

    printf("finished sneklang tools\n");
    return 0;
}

char *does_not_exist(char expression[]) {
    return expression;
}