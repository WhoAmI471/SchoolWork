x = int(input())
y = int(input())
k = str(input())

if k == '*':
    print(x * y)
elif k == '/' and y != 0:
    print(x / y)
elif k == '/' and y == 0:
    print('На ноль делить нельзя!')
elif k == '+':
    print(x + y)
elif k == '-':
    print(x - y)
elif k != '*' or k != '/' or k != '+' or k != '-':
    print('Неверная операция')
