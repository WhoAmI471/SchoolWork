def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    a = f(x + 1, end)
    b = f(x * 2 + 1, end)
    c = f(x * 2 + 1, end)
    d = f(x * 10, end)
    return a + b + c + d


print(f(10, 12))






