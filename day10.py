from heapq import heappush, heappop
from sys import stdin
from ortools.linear_solver import pywraplp

s = 0
for l in stdin:
	L, *B, J = l.split()
	N = len(L) - 2
	L = sum((L[i+1]=='#') << i for i in range(N))
	B = [tuple(map(int, b[1:-1].split(','))) for b in B]
	X = [sum(1 << i for i in b) for b in B]
	J = tuple(map(int, J[1:-1].split(',')))
	# day 1
	D = [11] * (1 << N)
	H = [(0, 0)]
	while H and H[0][1] != L:
		d, i = heappop(H)
		if d < D[i]:
			D[i] = d
			for b in X:
				heappush(H, (d+1, i^b))
	s += H[0][0]
	# day 2
	solver = pywraplp.Solver.CreateSolver("SAT")
	V = [solver.IntVar(0.0, solver.infinity(), f"v{i}") for i in range(len(B))]
	obj = solver.Objective()
	obj.SetMinimization()
	for v in V:
		obj.SetCoefficient(v, 1)
	for i, j in enumerate(J):
		constr = solver.Contraint(0, j)
		for k, b in enumerate(B):
			if i in b:
				constr.SetCoefficient(V[k], 1)
	solver.Solve()
	print(obj.Value())
print(s)