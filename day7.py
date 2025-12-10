from sys import stdin

G = list(stdin)
R, C = len(G), len(G[0])
T = [1 if c=='S' else 0 for c in G[0]]
s = 0
for r in range(1, R):
	T = [0 if G[r][c]=='^' else T[c]+(T[c-1] if c>0 and G[r][c-1]=='^' else 0)+(T[c+1] if c<C-1 and G[r][c+1]=='^' else 0) for c in range(C)]
print(sum(T))