from sys import stdin

s = 0
for B in stdin:
	l = len(B) - 1
	pos = 0
	J = ''
	for i in range(12):
		b, j = max((B[j], -j) for j in range(pos, l-11+i))
		J += b
		pos = -j + 1
	s += int(J)
print(s)
