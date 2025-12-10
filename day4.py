from sys import stdin
G = [list(l[:-1]) for l in stdin]
R, C = len(G), len(G[0])
adj = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
s = 0
while True:
	rem = [(r, c) for r in range(R) for c in range(C) if G[r][c]=='@' and 4 > sum(G[r+dr][c+dc]=='@' for dr, dc in adj if 0<=r+dr<R and 0<=c+dc<C)]
	if len(rem) == 0:
		break
	s += len(rem)
	for r, c in rem:
		G[r][c] = '.'
print(s)
