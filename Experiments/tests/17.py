from imp import NullImporter


with open ('17.txt') as f:
    data = [int(x) for x in f]
    k = 0
    m = -100

    for i in range(len(data)-1):
        if  data[i] % 3 == 0 or data[i+1] % 3 == 0:
            k += 1
            m = max(m, data[i] + data[i+1])

print(k,m)



