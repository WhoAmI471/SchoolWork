n = int(input())

if 0 <= n <= 36 and (1 <= n <= 10 and n % 2 == 0 or 19 <= n <= 28 and n % 2 == 0):
    print('черный')
elif 0 <= n <= 36 and (1 <= n <= 10 and n % 2 != 0 or 19 <= n <= 28 and n % 2 != 0):
    print('красный')
elif 0 <= n <= 36 and (11 <= n <= 18 and n % 2 == 0 or 29 <= n <= 36 and n % 2 == 0):
    print('красный')
elif 0 <= n <= 36 and (11 <= n <= 18 and n % 2 != 0 or 29 <= n <= 36 and n % 2 != 0):
    print('черный')
elif n == 0:
    print('зеленый')
elif n < 0 or n > 36:
    print('ошибка ввода')


