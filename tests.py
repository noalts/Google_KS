a = [int(s) for s in input().split()]
b = []

for i in range(len(a)):
    if a[i] in b:
        print('YES')
        b.append(a[i])
    else:
        print('NO')
        b.append(a[i])