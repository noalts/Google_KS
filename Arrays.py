#find max of array of lists or list in list short
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
best_i, best_j = 0, 0
curr_max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            best_i, best_j = i, j
print(best_i, best_j)

#or longer but readable: break out of nested loop.
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

#print a snowflake with if:
n = int(input())

for i in range(n):
    for j in range(n):
        
        if i == round((n-1)/2):
            print('*',sep=' ', end=' ')
        elif j > round((n-1)/2) and j == n-i-1:
            print('*',sep=' ', end=' ')    

        elif j == round((n-1)/2):
            print('*',sep=' ', end=' ')
        elif i > round((n-1)/2) and j == n-i-1:
            print('*',sep=' ', end=' ') 
        
        elif i == j:
            print('*',sep=' ', end=' ')
        
            
        else:
            print(".",sep=' ', end=' ')
    print()   

#or without if:
n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))

#print chessboard:
n, m = [int(i) for i in input().split()]
a = [['.'] * m for i in range(n)]

for i in range(n):
    if i % 2 != 0:
        for j in range(0, m, 2):        
            a[i][j] = "*"
    else:
        for j in range(1, m, 2):
            a[i][j] = "*"

for row in a:
    print(' '.join(row))

# or:
n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))

#parallel diagonals readable:
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

#or pythonic
n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))

#minor diagonal:
n = int(input())
a = [['0'] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if j == n-1-i:
            a[i][j] = str(1)
        elif j > n-1-i:
           a[i][j] = str(2)

for row in a:
    print(' '.join(row))

#or without if:
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()

#swap columns in array function:
def swap_columns(a, i, j):    
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
    

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]

swap_columns(a,i,j)

for row in a:
    print(' '.join([str(elem) for elem in row]))
    
#scale matrix:
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

# or without function:
m, n = [int(k) for k in input().split()]
A = [[int(k) for k in input().split()] for i in range(m)]
c = int(input())

for i in range(m):
    for j in range(n):
        A[i][j] *= c

print('\n'.join([' '.join([str(k) for k in row]) for row in A]))

#multiply different arrays with oneanother

# 3 4 2
# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 2 3
# 0 4
# 5 -1
# 1 1

# 13 5
# 45 33
# 77 61

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

#or without function:
m, n, r = [int(k) for k in input().split()]
A = [[int(k) for k in input().split()] for i in range(m)]
B = [[int(k) for k in input().split()] for j in range(n)]
C = [[0]*r for i in range(m)]

for i in range(m):
    for k in range(r):
        for j in range(n):
            C[i][k] += A[i][j] * B[j][k]

print('\n'.join([' '.join([str(k) for k in row]) for row in C]))