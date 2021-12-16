#!/usr/bin/env python3
# ^^^ This is important ^^^

import socket

HOST = 'localhost'
PORT = 1337

def recv_until_input(s, txt):
    buf = s.recv(1024)
    while txt not in buf:
        buf = s.recv(1024)

def solve_level(script):
    recv_until_input(s, b'Command >')
    s.send(b'play\n')
    recv_until_input(s, b'script:') 
    s.send(script)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.settimeout(100)
    solve_level(b'TICK, LOAD, 4, SUB, IF, SKP, 1, SKP, 2, RIGHT, RIGHT\n')
    solve_level(b'LOAD, 10, TICK, MOD, IF, LEFT\n')
    solve_level(b'LOAD, 20, TICK, MOD, COPY, -1, LOAD, 19, SUB, IF, RIGHT, IF, LEFT\n')
    solve_level(b'TICK, IF, SKP, 1, SKP, 6,  LOAD, 1, LOAD, 1, LOAD, 1, COPY, -1, TICK, SUB, IF, SKP, 1, SKP, 15,  RIGHT, DEL, -1, COPY, -2, COPY, -2, ADD, COPY, -2, TICK, ADD, DEL, 0\n')
    recv_until_input(s, b'Command >')
    s.send(b'play\n')
    flag = s.recv(1024).split(b': ')[-1].strip()

print(flag)
if b'idek{' in flag:
   exit(0)
else:
   exit(1)
