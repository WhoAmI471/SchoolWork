x = int(input())
l = 0
m = 0

while x > 0:
	l = l + 1
	if (x % 2) != 0:
		m = m + x % 8
	x = x // 8
print(l)
print(m)








