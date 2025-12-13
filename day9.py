from matplotlib import pyplot, patches
from sys import stdin

def rip(P, L, R, B, T):
	x, y = L+.5, B+.5
	cross = 0
	for (x0, y0), (x1, y1) in zip(P, P[1:]+[P[0]]):
		l, r, b, t = min(x0, x1), max(x0, x1), min(y0, y1), max(y0, y1)
		if (B < b == t < T and L < r and l < R) or (L < l == r < R and B < t and b < T):
			return False
		cross += b < y < t and l == r < x
	return cross % 2 == 1

P = [tuple(map(int, l.split(','))) for l in stdin]
fig, ax = pyplot.subplots()
ax.plot([x for x, y in P], [y for x, y in P])
A, B = 0, None
for i, (x0, y0) in enumerate(P):
	print(i)
	for x1, y1 in P[:i]:
		l, r, b, t = min(x0, x1), max(x0, x1), min(y0, y1), max(y0, y1)
		a = (r-l+1) * (t-b+1)
		if a > A and rip(P, l, r, b, t):
			A, B = a, (l, r, b, t)
print(A)
l, r, b, t = B
ax.add_patch(patches.Rectangle((l, b), r-l, t-b))
pyplot.show()