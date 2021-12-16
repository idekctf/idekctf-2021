#include <fcntl.h>
#include <sys/mman.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <linux/seccomp.h>
#include <sys/prctl.h>
#include "seccomp-bpf.h"

void install_syscall_filter()
{
        struct sock_filter filter[] = {
                VALIDATE_ARCHITECTURE,
                EXAMINE_SYSCALL,
                ALLOW_SYSCALL(rt_sigreturn),
#ifdef __NR_sigreturn
                ALLOW_SYSCALL(sigreturn),
#endif
                ALLOW_SYSCALL(openat),
                ALLOW_SYSCALL(write),
                ALLOW_SYSCALL(sendfile),
                ALLOW_SYSCALL(read),
                ALLOW_SYSCALL(exit),
                ALLOW_SYSCALL(fcntl),
                KILL_PROCESS,
        };
        struct sock_fprog prog = {
                .len = (unsigned short)(sizeof(filter)/sizeof(filter[0])),
                .filter = filter,
        };

        assert(prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) == 0);

        assert(prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &prog) == 0);
}

int main(int argc, char **argv)
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    int fd = open("/tmp", O_RDONLY);
    char path[] = "/tmp/XXXXXX";
    mkdtemp(path);
    chroot(path);
    printf("Creating a jail at `%s`.\n", path);


    for ( int x = 0 ; x < 100; x ++ ){
        char path[] = "/tmp/XXXXXX";
        mkdtemp(path);
        int fd = open(path, O_RDONLY);
        int r = rand() % 1000 + 3; 
        dup2(fd, r);
        close(fd);
    }

    srand(time(NULL)); 
    int r = rand() % 1000 + 3; 
    dup2(fd, r);
    close(fd);
    char * shellcode[0x100];
    printf("Here is a gift for your journey:%p\n" , shellcode);
    gets(shellcode);

    install_syscall_filter();
}
