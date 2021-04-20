n = int(input())
a = [['0'] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = str(j-i)
        elif i == j:
            a[i][j] = str(0)
        else:
            a[i][j] = str(i-j)

for row in a:
    print(' '.join(row))

