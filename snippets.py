# Print list:
a = int(input())
b = int(input())
for i in range(a,b+1):
    print(i)

#Print list: increase or decrease
a = int(input())
b = int(input())
if a >= b:
    for i in range(a,b-1,-1):
        print(i)
else:
    for i in range(a,b+1):
        print(i)

#Sum up list:
nums = []
for i in range(10):
    nums.append(int(input()))
print(nums.sum)

#or
res = 0
for i in range(10):
    res += int(input())
print(res)

#or with N numbers:
res = 0
for i in range(int(input())):
    res += int(input())
print(res)

#cubic meters:
res = 0
for i in range(1, int(input()) + 1):
    res += i ** 3
print(res)

#recursive factorial:
n = int(input())
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
print(factorial_recursive(n))

#or:
res = 1
n = int(input())
for i in range(1, n + 1):
    res *= i
print(res)

#count specific number:
num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)

# 1! + 2! + ... + n!
res = 1
sum = 0
n = int(input())
for i in range(1, n + 1):
    res *= i
    sum += res
print(sum)

#ladder
for i in range(1, int(input()) + 1):
    for j in range(1,i+1):
        print(j,sep='',end='')
    print()

#find missing
c = []
sc = []
res = []
n = int(input())
for i in range(1,n):
    c.append(int(input()))
for j in range(1,n+1):
    sc.append(j)
res = list(set(sc) - set(c))
print(res[0])

#or:
n = int(input())
sum_cards = 0
for i in range(1, n + 1):
    sum_cards += i
# One can prove the following:
# sum_cards == n * (n + 1) // 2
# However, we'll calculate that using the loop.
for i in range(n - 1):
    sum_cards -= int(input())
print(sum_cards)

#or calculating max sum
cardsum = 0
n = int(input())
sum = n * (n + 1) // 2
for i in range(1,n):
    cardsum += int(input())
print(sum - cardsum)

#string Theory
s = input()
print(s[2],s[2],s[1:],s[:4],s[:-2],s[2::2],s[1::2],s[::-1],len(s), sep='\n')

#count words
s = input()
print(s.count(' ')+1)

#interchange or swap strings and rounding:
s = input()
a = float(len(s))
b = int(--0-- a//2)
sone = s[:b]
stwo = s[b:]
sone, stwo = stwo, sone
print(sone,stwo,sep='')

#or shorter:
s = input()
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

#swap strings:
s = input()
print(s[s.find(' '):], s[:s.find(' ')], sep=' ')

#postions of char in string: if find:
s = input()
a = s.find('f')
b = s.rfind('f')
if a != -1:
    print(a)
    if b > a:
        print(b)    
else:
    print()

#or if count:
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))

#positions of 2nd char index:
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') == 0:
    print(-2)
else:
    a = s.find('f')
    b = s.find('f',a+1)
    print(b)

#extract fragment from string
s = input()
a = s.find('h')
b = s.rfind('h')
print(s[:a],s[b+1:],sep='')

#reverse extracted fragment
s = input()
a = s[:s.find('h')] 
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)

#replace string
s = input()
print(s.replace('1','one'))

#remove string
s = input()
print(s.replace('@',''))

#remove occurences but....
s = input()
a = s[:s.find('h') + 1] 
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)

#remove nth character from string
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t += s[i]
print(t)

#SquareList
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1

#SquareList no while
n = int(input())
nsqlist = []
i = 0
nsq = 0
for i in range(1,n+1):
    nsq = i ** 2
    nsqlist.append(nsq)
for j in nsqlist:    
    if j <= n:
        print(j)

#least divisor kleinster Teiler
n = int(input())
i = 2
while n%i != 0:
  i += 1
print(i)

#greatest power (höchste Potenz)
n = int(input())
i = 1
while 2 ** i <= n:
    i += 1
print(i-1, 2 ** (i-1))

#greatest power (höchste Potenz)(no operator **)
n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)

#training day +10%
x = int(input())
y = int(input())
days = 1
while x < y:
    x = x + (x*10/100) # x *= 1.1
    days += 1
print(days)

#input separated by lines new line input length of sequence
n = int(input())
c = 0
while n != 0:
    c += 1
    if c == 0:
        break
    n = int(input())
print(c)

#or
len = 0
while int(input()) != 0:
    len += 1
print(len)

#avarage of sequence
n = int(input())
s = 0
c = 0
while n != 0:
    c += 1
    s += n
    n = int(input())
print(s / c)

#max of sequence
max = 0
element = -1
while element != 0:
    element = int(input())
    if element > max:
        max = element
print(max)

#or with list
n = int(input())
c = []
while n != 0:
    c.append(n)
    n = int(input())
print(max(c))

#index of max in sequence no list
max = 0
pos = 0
top = 1
element = -1
while element != 0:
    element = int(input())
    pos += 1
    if element > max:
        max = element
        top = pos
print(top)

#or
max = 0
index_of_max = -1
element = -1
len = 1
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index_of_max = len
    len += 1
print(index_of_max)

#count even in sequence (because 0 counts...so -1 becomes 0)
num_even = -1
element = -1
while element != 0:
    element = int(input())
    if element % 2 == 0:
        num_even += 1
print(num_even)

#or 
c = 0
element = int(input())
while element != 0:
    if element % 2 == 0:
        c += 1
    element = int(input())
print(c)

#count greater than prev in sequence
ge = 0
n = int(input())
k = 0
while n != 0:
    k = n
    n = int(input())
    if n > k:
        ge += 1
print(ge)

#or where prev becomes next
prev = int(input())
answer = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        answer += 1
    prev = next
print(answer)

#find second max with list
n = int(input())
c = []
while n != 0:
    c.append(n)
    n = int(input())
c.sort(reverse=True)
print(c)
print(c[1])

#or without list
first_max = int(input())
second_max = int(input())
if first_max < second_max:
    first_max, second_max = second_max, first_max
element = int(input())
while element != 0:
    if element > first_max:
        second_max, first_max = first_max, element
    elif element > second_max:
        second_max = element
    element = int(input())
print(second_max)

#count max numbers with list
n = -1
m = 0
l = []
c = 0
while n != 0:
    n = int(input())
    l.append(n)
m = max(l)
for i in l:
    if i == m:
        c += 1
print(c)

#or no list
maximum = 0
num_maximal = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
    elif element == maximum:
        num_maximal += 1        
print(num_maximal)

#Fibunacci sequence with list:
def fibs(n):                                                                                                 
    fibs = [0, 1, 1]                                                                                           
    for f in range(2, n):                                                                                      
        fibs.append(fibs[-1] + fibs[-2])                                                                         
    return fibs[n]

#or for loop:
n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)

# is input Fibunacci-Number? without list
if n == 0:
    print(0)
else:
    a, b = 0, 1
    q = 1
    while b <= n:
        if b == n:
            print(q)
            break
        a, b = b, a + b
        q += 1
    else:
        print(-1)

#or with list        
q = int(input())
n = 45
l = [0, 1]
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
        l.append(b)
if q in l:
    print(l.index(q))
else:
    print(-1)

#recursion fibunacci:
a = int(input())

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

print(fib(a))

# or shorter recursion fibunacci:
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
        
print(fib(int(input())))

#find max of consecutive equal elements
prev = -1
curr_rep_len = 0
max_rep_len = 0
element = int(input())
while element != 0:
    if prev == element:
        curr_rep_len += 1
    else:
        prev = element
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    element = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)

#or more readable:
k = 0
q = 1
r = 1
t = 1
n = int(input())
while n != 0:
    k = n
    n = int(input())
    if k == n:
        q += 1
    elif k != n:
        q = 1    
    t = q
    if t > r:
        r = t
print(r)

# print every 2nd index from list:
a = [int(s) for s in input().split()]
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i])

#or:
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])

#print even element of list:
a = [int(i) for i in input().split()]
for j in a:
    if j % 2 == 0:
        print(j)

# greater than previous in list:
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

# same sign of neighbour
a = [int(i) for i in input().split()]
for i in range(len(a) - 1):
    if a[i] > 0 and a[i + 1] > 0:
        print(a[i],' ',a[i + 1])
        break
    elif a[i] < 0 and a[i + 1] < 0:
        print(a[i],' ',a[i + 1])
        break
    else:
        pass

#or
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break

#bigger than both neighbours
a = [int(i) for i in input().split()]
c = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        c += 1
print(c)

#list max and index of max
a = [int(i) for i in input().split()]
c = 0
m = max(a)
for i in range(0, len(a)):
    if i == max:
        break
print(m,' ',a.index(m))

#count distinct numbers in list
a = [int(i) for i in input().split()]
c = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        c += 1
print(c)

#swap elements in list(print without brackets)
a = [int(i) for i in input().split()]
c = ''
for i in range(0, len(a) - 1, 2):
    c = a[i]
    a[i] = a[i + 1]
    a[i + 1] = c
    i += 2
print(*a)

#or
a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))

#swap elements(max, min) of list
a = [int(i) for i in input().split()]
x = a.index(max(a))
y = a.index(min(a))
a[x], a[y] = a[y], a[x]
print(*a)

#number of equal pairs counted once
a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)

#number of equal pairs all combinations counted
a = [int(i) for i in input().split()]
b = set(a)
c = []
d = []
for i in b:
	c.append(a.count(i))
for i in c:
	if i > 1:
		d.append(i * 2)
print(sum(d))

#print every unique element in order of appearance
a = [int(s) for s in input().split()]
b = []
for i in range(len(a)):
    if a.count(a[i]) == 1:
        b.append(a[i])
print(*b)

#or
a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')

#chess place 8 queens
N = 8
result = 'NO'
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = [int(j) for j in input().split()]
for i in range (N):
    for j in range(i+1,N):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            result = 'YES'
print(result)

#bowling pins standing .I:
N, K = [int(i) for i in input().split()]
kegels = ['I'] * N
for j in range(K):
    l, r = [int(i) for i in input().split()]
    kegels[l-1:r] = ['.'] * (r-l+1)
print(''.join([str(i) for i in kegels]))

#function distance(): Pythagoras
import math
def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance(x1, y1, x2, y2))

#function power of n: Quadratzahlen
r, t = [float(input()) for _ in range(2)]
def power(a, b):
    return a ** b
print(power(r, t))

#uppercase letter, lowercase-
def uppercase(s):
    q = []
    q[:0] = s
    if ord(q[0]) >= 97:
        q[0] = chr(ord(q[0]) - 32)
    s = ''.join(q)
    return s

a = input().split()
for i in a:
    print(uppercase(i),end=' ')

#or
def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))

#power of with recursion
a, n = [float(input()) for _ in range(2)]

def power(s, t):
    if t == 0:
        return 1
    s = s * power(s, t - 1)
    return s

print(power(a, n))

#or shorter
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

print(power(float(input()), int(input())))

#reverse order
def reverse():
    a = int(input())
    if a != 0:
        reverse()
    print(a)

reverse()

#Collatz function recursion remember the callstacks!
def coll(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + coll(n / 2)        
    else:        
        return 1 + coll(n*3 + 1)
print(coll(int(input())))

#recursion fibunacci:
a = int(input())

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

print(fib(a))

# or shorter:
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(int(input())))

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

#multiply different arrays with oneonother
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

#print distinct elements of set:
a = {int(s) for s in input().split()}
b = set()
b.update(a)
print(*b)

#print number of distinct elements in set:
a = {str(s) for s in input().split()}
print(len(a))

#or short:
print(len(set(input().split())))

#number of unique numbers in 2 sets:
print(len(set(input().split()).intersection(set(input().split()))))

#or:
print(len(set(input().split()) & set(input().split())))

#sort list by last char using sorted with key and lambda function:
words = ['banana', 'pie', 'Washington', 'book']
sorted(words, key=lambda x: x[::-1])

#determine if number occured before without set:
a = [int(s) for s in input().split()]
b = []

for i in range(len(a)):
    if a[i] in b:
        print('YES')
        b.append(a[i])
    else:
        print('NO')
        b.append(a[i])

#or with set
numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)

#distinct words in given text:
n = int(input())
b = set()
for i in range(n):
    a = input().split(' ')
    for e in a:
        b.add(e)
print(len(b))

#or shorter:
words = set()
for _ in range(int(input())):
    words.update(input().split())
print(len(words))