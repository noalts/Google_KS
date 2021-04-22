
def scale(a, n, m, c):    
    for i in range(n):
        for j in range(m):
            a[i][j] *= c
    

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
c = int(input())

scale(a, n, m, c)

for row in a:
    print(' '.join([str(elem) for elem in row]))

