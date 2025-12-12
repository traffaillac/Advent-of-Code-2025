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
# day 1
P = {u: 0 for u in F}
P["you"] = 1
for i in range(N-1):
	for v, U in B.items():
		if v != "you":
			P[v] = sum(P[u] for u in U)
print(P["out"])
# day 2
P = {u: (0,0,0,0) for u in F}
P["svr"] = (1,0,0,0)
for i in range(N-1):
	for v, U in B.items():
		if v == "dac":
			P[v] = (0, sum(P[u][0] for u in U), 0, sum(P[u][2] for u in U))
		elif v == "fft":
			P[v] = (0, 0, sum(P[u][0] for u in U), sum(P[u][1] for u in U))
		elif v != "svr":
			P[v] = tuple(sum(P[u][j] for u in U) for j in range(4))
print(P["out"][3])