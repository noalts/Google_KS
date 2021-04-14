n, m = [int(i) for i in input().split()]

a = [[int(j) for j in input().split()] for i in range(n)]

maxi = int()

for i in range(n):
    for j in range(m):
        if a[i][j] >= maxi and a[i][j] >= 0:
            maxi = a[i][j]
        elif a[i][j] <= 0:
            maxi = a[i][j]
            if a[i][j] <= maxi:
                maxi = a[i][j]
            

for i in range(n):
    for j in range(m):
        if a[i][j] == maxi:
            print(i, j)
            break
    else:
        continue
    break