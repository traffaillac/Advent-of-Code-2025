from sys import stdin

# G = [l.split() for l in stdin]
# R, C = len(G), len(G[0])
# s = 0
# for c in range(C):
# 	s += eval(G[R-1][c].join(G[r][c] for r in range(R-1)))

G = list(stdin)
R, C = len(G), len(G[0]) - 1
op = None
st = ''
c = 0
s = 0
while c < C:
	for r in range(R-1):
		st += G[r][c]
	op = op if G[R-1][c]==' ' else G[R-1][c]
	c += 1
	if c == C or all(G[r][c]==' ' for r in range(R)):
		s += eval(st)
		st = ''
		c += 1
	else:
		st += op
print(s)