from sys import stdin

d = 50
s = 0
for l in stdin:
	if l[0] == 'R':
		c = int(l[1:])
		s += (d + c) // 100
		d = (d + c) % 100
	else:
		c = int(l[1:])
		s += abs(((d - 1) % 100 - c) // 100)
		d = (d - c) % 100
print(s)
