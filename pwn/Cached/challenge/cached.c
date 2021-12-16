#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *ptr1;
char *ptr2;
char **a;
char **b;
char **c;
char **d;

int main() {
  setvbuf(stdin, NULL, 2, 0);
  setvbuf(stdout, NULL, 2, 0);
  puts("Welcome to cached, the place where we teach you how to do heap exploits!");
  puts("We're going to learn about tcache poisoning!");
  puts("But first, let's get some background on how the heap works.");
  puts("The heap is a place for dynamic memory allocation.");
  puts("In other words, it's a place where you can request arbitrarily sized blocks of memory, any time in your program.");
  puts("");
  puts("[Press enter to continue]");
  getchar();
  puts("We access heap memory through the malloc(), and free() functions, both provided when you `#include <stdlib.h>`.");
  puts("malloc(n) will return a pointer to a chunk of memory with size n, and free(ptr) will deallocate a chunk of memory returned by malloc().");
  puts("In recent versions of GLIBC (>=2.26), free()d chunks that are small enough are put into a linked list called the tcache, where they will be returned on the next call to malloc() of the same size.");
  puts("This means that if we malloc(64), then free() the pointer we get from that, the next malloc(64) will return the same chunk.");
  puts("Demonstration:");
  puts("```");
  puts("ptr1 = malloc(64);");
  puts("printf(\"ptr1: %p\\n\", ptr1);");
  puts("free(ptr1);");
  puts("ptr2 = malloc(64);");
  puts("printf(\"ptr2: %p\\n\", ptr2);");
  puts("```");
  ptr1 = malloc(64);
  printf("ptr1: %p\n", ptr1);
  free(ptr1);
  ptr2 = malloc(64);
  printf("ptr2: %p\n", ptr2);
  puts("");
  puts("[Press enter to continue]");
  getchar();
  puts("This is done to optimize memory usage, because we don't want to be allocating new memory when we have memory that is no longer being used lying around.");
  puts("However, this makes it very dangerous to use a chunk after we have free()d it. The data in the chunk may have been returned to a different call to malloc(), and may have been used for another purpose.");
  puts("We would be able to overwrite important information because the chunk is now being used in two places.");
  puts("In addition to this, free()d chunks are part of linked lists, so by editing the first 8 bytes of a free()d chunk we often can control where the next chunk in the linked list is.");
  puts("The result of this is a possible arbitrary memory write if we can control the next pointer that malloc() returns.");
  puts("");
  puts("[Press enter to continue]");
  getchar();
  puts("Let's see this in action!");
  puts("```");
  puts("a = malloc(128);");
  puts("b = malloc(128);");
  puts("free(a);");
  puts("free(b);");
  puts("```");
  a = malloc(128);
  b = malloc(128);
  free(a);
  free(b);
  puts("Right now I have allocated two chunks with size 128 using malloc, then freed them both.");
  puts("Note that I have not zeroed out the `a` and `b` pointers, as is best practice, but they are still pointing to the already freed chunks.");
  puts("At this point, because we have freed chunk `a`, then `b`, our tcache linked list (which is first in first out, meaning that new items are attached to the front of the list, and will be the first to be returned back) for size 128 looks like this: (note that by `head`, I mean the start of the linked list)");
  puts("----------------------------------------------------");
  printf("head => b (%p) => a (%p)\n", b, a);
  puts("----------------------------------------------------");
  puts("");
  puts("[Press enter to continue]");
  getchar();
  puts("Now, the first 8 bytes of the chunk stored at `b` (the part of the free chunk that points to the next free chunk) points to `a`.");
  puts("What if we rewrote this pointer by editing the memory at `b`?");
  puts("We could change the linked list and make a future malloc(128) return our rewritten pointer instead of `a`!");
  puts("One popular target, that will bypass full RELRO, is a function pointer in libc called `__free_hook`.");
  puts("This pointer, when not NULL, will be called whenever free() is called, and with the same arguments as well.");
  puts("Our goal here will be to write the address of system@libc to `__free_hook`.");
  puts("The result will be that every call to free() after this will be equivalent to a call to system().");
  puts("That means that if we free a chunk that has `/bin/sh` in it, we are essentially calling system(\"/bin/sh\")!");
  puts("Let's do this! You'll need this:");
  puts("----------------------------------------------------");
  printf("system @ %p\n", &system);
  puts("----------------------------------------------------");
  puts("With the provided libc you can also calculate the address of `__free_hook`.");
  puts("```");
  puts("fgets(b, 128, stdin);");
  puts("```");
  fgets(b, 128, stdin);
  puts("By writing to the already free()d chunk at `b`, we have now corrupted the tcache linked list. It now looks like:");
  puts("----------------------------------------------------");
  printf("head => b (%p) => (%p)\n", b, *b);
  puts("----------------------------------------------------");
  puts("Now, we will call malloc() two more times, to get the two chunks back out from the tcache linked list:");
  puts("```");
  puts("c = malloc(128);");
  puts("d = malloc(128);");
  puts("```");
  c = malloc(128);
  d = malloc(128);
  printf("We can now see that c points to %p (our chunk at `b` was returned back) and d points to %p (the pointer we overwrote).", c, d);
  puts("We have successfully controlled what malloc() returns!");
  puts("Let's say that we now wrote to the memory in the chunk returned by `d`.");
  puts("If all went well, we are now writing to the memory at `__free_hook`. Overwrite that with system now:");
  puts("```");
  puts("fgets(d, 128, stdin);");
  puts("```");
  fgets(d, 128, stdin);
  puts("OK. Now we will proceed to the last step. We will use chunk `c` as a scratchpad and write \"/bin/sh\" to it. Then we will free it, and hopefully call `system(\"/bin/sh\")` for a shell!");
  puts("```");
  puts("strcpy(c, \"/bin/sh\");");
  puts("free(c);");
  puts("```");
  strcpy(c, "/bin/sh");
  free(c);
  puts("If you got here, it seems that the exploit didn't work. Don't give up, you can do it!");

}
