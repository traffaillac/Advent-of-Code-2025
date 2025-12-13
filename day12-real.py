from pprint import pprint
from sys import stdin
from pulp import *

def cw90(p):
	return tuple((c, 2-r) for r, c in p)
def flip(p):
	return tuple((2-r, 2-c) for r, c in p)

S = set()
for i in range(6):
	input()
	s = [input() for _ in range(3)]
	input()
	p = tuple((r, c) for r in range(3) for c in range(3) if s[r][c]=='#')
	pf = flip(p)
	for _ in range(4):
		S.add((p := cw90(p), i))
		S.add((pf := cw90(pf), i))
res = 0
for j, l in enumerate(stdin):
	A, *Q = l.split()
	Q = tuple(map(int, Q))
	C, R = map(int, A[:-1].split('x'))
	G = [[0] * C for _ in range(R)]
	I = [0] * 6
	prob = LpProblem("Problem", LpMaximize)
	for i, (p, idx) in enumerate(S):
		for r in range(R - 2):
			for c in range(C - 2):
				v = LpVariable(f"{i},{r},{c}", cat="Binary")
				I[idx] += v
				for dr, dc in p:
					G[r+dr][c+dc] += v
	for r in range(R):
		for c in range(C):
			prob += G[r][c] <= 1
	for i in range(6):
		prob += I[i] <= Q[i]
	prob += sum(I)
	prob.solve(PULP_CBC_CMD(msg=0))
	v, s = round(prob.objective.value()), sum(Q)
	print(f"{j} -> {v}/{s}")
	res += v == s
print(res)