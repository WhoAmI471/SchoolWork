n = int(input())
a = n // 1000
b = (n % 1000) // 100
c = (n % 100) // 10
d = n % 10

'''print(a)
print(b)
print(c)
print(d)'''

if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')
