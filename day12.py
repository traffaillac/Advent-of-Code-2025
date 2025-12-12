from pprint import pprint
from sys import stdin

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
pprint(S)