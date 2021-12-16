#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct lolol {
  char buf[32];
  char *sp;
};

struct lolol lol;

int main() {
  lol.sp = lol.buf;
  setvbuf(stdout, NULL, 2, 0);
  setvbuf(stdin, NULL, 2, 0);
  puts("Welcome to Vanity Check II. (AKA mirror as a service!)");
  while (1) {
    read(0, lol.sp, 33);
    puts(lol.sp);
  }
}
