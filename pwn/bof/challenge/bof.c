#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

void call_me(){
    puts("!!!!!!!!!!YOU WIN!!!!!!!!!");
    char * flag = malloc ( 100 );
    int fp = open("/flag.txt", 0);
    read(fp, flag, 100);
    write( 1, flag, 100 );
    exit(1337);
}

int main(void){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    puts("Welcome to a basic buffer overflow challenge!!!");
    puts("Try to complie this binary with gcc and see what warning message you get");
    puts("Try looking into why this functions is so bad and how you can exploit this");
    puts("In this challenge their is another function that seems very helpful :)");
    char foo[69];
    gets(foo);
    return 0;
}
