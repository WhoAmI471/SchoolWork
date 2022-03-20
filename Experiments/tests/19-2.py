def f(x, y, p):
    if x + y >= 69 or p > 5:
        return p == 3 or p == 5
    if p % 2 == 0:
        return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or  f(x * 2, y, p + 1) or f(x, y * 3, p + 1)
    else:
        return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and  f(x * 2, y, p + 1) and f(x, y * 3, p + 1)

for s in range(1,58+1):
    if f(10, s, 1):
        print(s)