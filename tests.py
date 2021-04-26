def multi(a, b, d):
        
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                d[i][j] += a[i][k] * b[k][j]
               
       
    

m, n, r = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]
b = [[int(k) for k in input().split()] for l in range(n)]
d = [[int(0) for s in range(r)] for t in range(m)]

multi(a, b, d)

for row in d:
    print(' '.join([str(elem) for elem in row]))

