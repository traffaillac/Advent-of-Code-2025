from pprint import pprint
from sys import stdin

A = [0]*6
for i in range(6):
	input()
	A[i] = ''.join(input() for _ in range(3)).count('#')
	input()
s = 0
for l in stdin:
	S, *Q = l.split()
	Q = tuple(map(int, Q))
	C, R = map(int, S[:-1].split('x'))
	s += R*C >= sum(Q[i]*A[i] for i in range(6))
print(s)