from sage.modules.free_module_integer import IntegerLattice
from output import *

def Babai_CVP(mat, target):
	M = IntegerLattice(mat, lll_reduce=True).reduced_basis
	G = M.gram_schmidt()[0]
	diff = target
	for i in reversed(range(G.nrows())):
		diff -=  M[i] * ((diff * G[i]) / (G[i] * G[i])).round()
	return target - diff

c = 1000 ### Modify this

M = matrix(ZZ, L, L // 2 + L)

for i in range(L // 2):
	for j in range(L):
		M[j, i] = c * points[i]^j
M[:, L // 2:] = matrix.identity(L)

target = vector([c * evaluations[i] for i in range(L // 2)] + [0] * L)

v = Babai_CVP(M, target)

flag = ''.join(chr(v[i]) for i in range(L // 2, L // 2 + L))
print("idek{" + flag + "}")


