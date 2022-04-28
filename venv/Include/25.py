import math


count = 0
for i in range(700001, 800000):
    
    b = 0

    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            b = round(i / j)
            break

    
    if b == 0:
        M = 0
    else:
        M = j + b

    if M != 0 and M % 10 == 8:
        count += 1
        print(i, M)


    if count == 5:
        break





