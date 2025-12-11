from sys import stdin

F = {}
for l in stdin:
	u, *V = l.split()
	u = u[:-1]
	F[u] = V
N = len(F)
B = {}
for u, V in F.items():
	for v in V:
		B.setdefault(v, []).append(u)
P = {u: 0 for u in F}
P["you"] = 1
for i in range(N-1):
	for v, U in B.items():
		if v != "you":
			P[v] = sum(P[u] for u in U)
print(P["out"])