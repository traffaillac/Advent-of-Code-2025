from sys import stdin

t, b = stdin.read().split("\n\n")
R = [[*map(int, r.split('-'))] for r in t.split()]
IDs = [*map(int, b.split())]
print(sum(any(a<=i<=b for a, b in R) for i in IDs))

R.sort()
A, B = 1, 0
s = 0
for a, b in R:
	if a <= B: # interval intersection
		B = max(b, B)
	else:
		s += B - A + 1
		A, B = a, b
print(s + B - A + 1)