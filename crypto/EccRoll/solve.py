import ast
from Crypto.Util.number import *

with open('output.txt', "r") as f:
        lines = f.readlines()

bflag = ["0" for _ in range(639)]

for line in lines:
    if "p" in line:
        p = int(line.strip().split(" = ")[1])
    if "enc" in line:
        enc = ast.literal_eval(line.strip().split(" = ")[1])
        
        for i, n in enumerate(enc):
            if pow(n, (p-1) // 2, p) != 1:
                bflag[i] = "1"

res = ''.join(bflag)
flag = long_to_bytes(int(res, 2))
print(flag)
