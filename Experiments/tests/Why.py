x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x = x2 - x1
y = y2 - y1

if (1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8 and -1 <= x <= 1 and -1 <= y <= 1):
    print('YES')
else:
    print('NO')
