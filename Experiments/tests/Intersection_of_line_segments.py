a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if b1 == a2:
    print(b1)
elif a1 == b2:
    print(a1)
elif a1 <= a2 < b1 < b2:
    print(f'{a2} {b1}')
elif a2 <= a1 < b2 < b1:
    print(f'{a1} {b2}')
elif a1 < a2 < b2 <= b1:
    print(f'{a2} {b2}')
elif a2 < a1 < b1 <= b2:
    print(f'{a1} {b1}')
elif a1 == a2 and b1 == b2:
    print(f'{a1} {b1}')
else:
    print('пустое множество')

'''if a1 <= a2 and b1 >= b2: #1
    print( f'{a2} {b2}')
elif a1 >= a2 and b1 <= b2: #2
    print( f'{a1} {b2}')
elif a1 <= a2 and b1 <= b2: #3
    print(a2)
elif a1 >= a2 and b1 >= b2:
    print(a1)
elif b1 < a2 or b2 < a1:
    print('пустое множество')'''
