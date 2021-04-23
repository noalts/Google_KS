
def multi(a, b, c, d, m, n, r):
        
    for i in range(m):
        q = 0
        for j in range(n):
            q += a[i][j] * c[i][j]
        d.append(q)


       
    

m, n, r = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]
b = [[int(k) for k in input().split()] for l in range(n)]
d = []

c = [[b[j][i] for j in range(len(b))] for i in range(len(b[0]))]

# for i in range(len(b)):
#     for j in range(len(b[0])):
#         c[i][j] = b[j][i]


multi(a, b, c, d, m, n, r)

for row in c:
    print(' '.join([str(elem) for elem in row]))

