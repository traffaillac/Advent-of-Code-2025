from math import hypot
from sys import stdin

class DisjointSet:
	def __init__(self):
		self.parent = {}
		self.cardinal = {}
	def find(self, a):
		if a in self.parent:
			t = self.find(self.parent[a])
			self.parent[a] = t[1]
		else:
			t = self.cardinal.get(a, 1), a
		return t
	def union(self, a, b):
		ca, a = self.find(a)
		cb, b = self.find(b)
		if a != b:
			if ca < cb:
				a, ca, b, cb = b, cb, a, ca
			self.parent[b] = a
			self.cardinal[a] = ca + cb

# Since len(J)=1000, Kruskal's MST with O(n^2) suffices here
J = [tuple(map(int, l.split(','))) for l in stdin]
D = sorted((hypot(x-X, y-Y, z-Z), i, j) for i, (x, y, z) in enumerate(J) for j, (X, Y, Z) in enumerate(J[:i]))
S = DisjointSet()
for _, (_, i, j) in zip(range(1000), D):
	S.union(i, j)
L = sorted({S.find(i) for i in range(len(J))}, reverse=True)
print(L[0][0] * L[1][0] * L[2][0])

S = DisjointSet()
for _, i, j in D:
	S.union(i, j)
	if S.find(i)[0] == len(J):
		print(J[i][0] * J[j][0])
		break