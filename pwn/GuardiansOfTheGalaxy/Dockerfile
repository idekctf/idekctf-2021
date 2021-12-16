FROM ubuntu:21.04
# FROM archlinux

WORKDIR /app
# RUN apt-get update -y && apt-get install -y && apt install apt-utils python3 gdb socat -y
RUN apt-get update -y && apt-get install -y && apt install socat -y

# RUN apt-get install gcc socat
# RUN pacman -Syyu && pacman -S gcc socat gdb python3

COPY rocket.c ./
COPY flag.txt /flag.txt
COPY seccomp-bpf.h ./ 
COPY rocket /app/rocket


RUN chmod 777 /flag.txt
# RUN gcc /app/rocket.c -fno-stack-protector -execstack -W -no-pie -z execstack -o /app/rocket


EXPOSE 1337

# RUN useradd -M -s /usr/bin/nologin ctf
# USER ctf
CMD socat \
        TCP-LISTEN:1337,reuseaddr,fork \
        EXEC:"/app/rocket"
