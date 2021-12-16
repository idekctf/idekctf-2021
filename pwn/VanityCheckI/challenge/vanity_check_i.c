#include <stdio.h>
#include <stdlib.h>

int main() {
  char buf[256];
  setvbuf(stdout, NULL, 2, 0);
  setvbuf(stdin, NULL, 2, 0);
  puts("Welcome to Vanity Check. (AKA mirror as a service!)");
  while (1) {
    scanf("%255[^\n]%*c", buf);
    printf(buf);
    putchar(10);
  }
}
