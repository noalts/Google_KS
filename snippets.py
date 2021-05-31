# Tries

# Implementing TrieNode class
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}

# initialising empty TrieNode
class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

# perform insertion into Trie

def insert(self, word):
    node = self.root
    for char in word:
        if char in node.children:
            node = node.children[char]
        else:
            new_node = TrieNode(char)
            node.children[char] = new_node
            node = new_node
    node.is_end = True



# For loops with range

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

# 1! + 2! + ... + n! sum of factorials
#-----------------------------------------------------------in
# 4
#-----------------------------------------------------------out
# 33

res = 1
sum = 0
n = int(input())
for i in range(1, n + 1):
    res *= i
    sum += res
print(sum)

#ladder
#-----------------------------------------------------------in
# 3
#-----------------------------------------------------------out
# 1
# 12
# 123

for i in range(1, int(input()) + 1):
    for j in range(1,i+1):
        print(j,sep='',end='')
    print()

#find missing element
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

# Strings

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
print(sone, stwo, sep='')

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

#While Loops--------------------------------------------------------------------------------

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

#Lists-------------------------------------------------------------------------------------------

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
    if i == m:
        m = i
print(m, a.index(m))

# or
a = [int(i) for i in input().split()]
c = 0
m = max(a)
print(m , a.index(m))

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
#-------------------------------------------in
# 1 1 1 1 1	
#-------------------------------------------out
# 10

a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)

#number of equal pairs all combinations counted
#-------------------------------------------in
# 1 1 1 1 1	
#-------------------------------------------out
# 10

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
#-------------------------------------------in
# 4 3 5 2 5 1 3 5
#-------------------------------------------out
# 4 2 1

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

# Lists
# chess place 8 queens
#-------------------------------------------in
# 1 7
# 2 4
# 3 2
# 4 8
# 5 6
# 6 1
# 7 3
# 8 5
#-------------------------------------------out
# NO

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

# Lists
# bowling pins standing .I:
#-------------------------------------------in
# 10 3
# 8 10
# 2 5
# 3 6
#-------------------------------------------out
# I.....I...

N, K = [int(i) for i in input().split()]
kegels = ['I'] * N
for j in range(K):
    l, r = [int(i) for i in input().split()]
    kegels[l-1:r] = ['.'] * (r-l+1)
print(''.join([str(i) for i in kegels]))

#function distance(): Pythagoras
#-------------------------------------------in
# 0
# 0
# 1
# 0
#-------------------------------------------out
# 1

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

# Functions and recursion-------------------------------------------------------------------------------------------------------
# uppercase letter, lowercase-
#-------------------------------------------in
# harry potter
#-------------------------------------------out
# Harry Potter

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

# Functions and recursion
# power of with recursion, exponentiation: a power of n
#-------------------------------------------in
# 2
# 4
#-------------------------------------------out
# 16

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
# -------------------------------------------in
# 1
# 2
# 3
# 0
# -------------------------------------------out
# 0
# 3
# 2
# 1

def reverse():
    a = int(input())
    if a != 0:
        reverse()
    print(a)

reverse()

#Collatz function recursion remember the callstacks!
# count steps to reach 1
#-------------------------------------------in
# 27
# #-------------------------------------------out
# 111

def coll(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + coll(n / 2)        
    else:        
        return 1 + coll(n*3 + 1)

print(coll(int(input())))

# Functions and recursions:
#recursion fibunacci:	
#-------------------------------------------in
# 6
#-------------------------------------------out
# 8

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

# array
#find index of max of array of lists or list in list short
#-------------------------------------------in
# 3 4
# 0 3 2 4
# 2 3 5 5
# 5 1 2 3
#-------------------------------------------out
# 1 2

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

# array
# print a snowflake with if:
#-------------------------------------------in
# 5
#-------------------------------------------out
# * . * . *
# . * * * .
# * * * * *
# . * * * .
# * . * . *

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

# or without if:
n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))

# array
# print chessboard:
#-------------------------------------------in
# 3 4
#-------------------------------------------out
# . * . *
# * . * .
# . * . *

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

# array
# parallel diagonals readable:
#-------------------------------------------in
# 5
#-------------------------------------------out
# 0 1 2 3 4
# 1 0 1 2 3
# 2 1 0 1 2
# 3 2 1 0 1
# 4 3 2 1 0

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

# array
#minor diagonal:
#-------------------------------------------in
# 4	
# -------------------------------------------out
# 0 0 0 1
# 0 0 1 2
# 0 1 2 2
# 1 2 2 2

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

# array
# swap columns in array function:
#-------------------------------------------in
# 3 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 0 1
#-------------------------------------------out
# 12 11 13 14
# 22 21 23 24
# 32 31 33 34

def swap_columns(a, i, j):    
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
    

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]

swap_columns(a,i,j)

for row in a:
    print(' '.join([str(elem) for elem in row]))

# array   
#scale matrix:
#-------------------------------------------in
# 3 4
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34
# 2	
#-------------------------------------------out
# 22 24 26 28
# 42 44 46 48
# 62 64 66 68
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

# array
# multiply different arrays with oneonother
#-------------------------------------------in
# 3 4 2
# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 2 3
# 0 4
# 5 -1
# 1 1
#-------------------------------------------out
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

#set

#print number of distinct elements in set:
#-----------------------------------------in
# 1 2 3 2 1
#-----------------------------------------out
# 3

#print distinct elements of set:
a = {int(s) for s in input().split()}
b = set()
b.update(a)
print(*b)

#or
a = {str(s) for s in input().split()}
print(len(a))

#or short:
print(len(set(input().split())))

#number of unique numbers in 2 sets:

#-----------------------------------------in
# 1 3 2
# 4 3 2
#-----------------------------------------out
# 2 3

print(len(set(input().split()).intersection(set(input().split()))))

#or:
print(len(set(input().split()) & set(input().split())))

#sort list by last char using sorted with key and lambda function:
words = ['banana', 'pie', 'Washington', 'book']
sorted(words, key=lambda x: x[::-1])

#determine if number occured before without set:
#-----------------------------------------in
# 1 2 3 2 3 4
#-----------------------------------------out
# NO
# NO
# NO
# YES
# YES
# NO

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
# set
# distinct words in given text:
#-----------------------------------------in
# 4
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.
#-----------------------------------------out
# 19

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

#set
#languages spoken by one all or many students
#-----------------------------------------in
# 3
# 3
# Russian
# English
# Japanese
# 2
# Russian
# English
# 1
# English	
#-----------------------------------------out
# 1
# English
# 3
# English
# Japanese
# Russian

b = set()
a = set()
c = set()
d = set()
for i in range(int(input())):
    n = int(input())
    if i == 0:
        for j in range(n):
            a.update(input().split())
            d.update(a)
    else:
        for k in range(n):
            b.update(input().split())
            d.update(b)
        c = a.intersection(b)
        b = set()
print(len(c))
print(*sorted(c), sep = '\n')
print(len(d))
print(*sorted(d), sep = '\n')

#or shorter:
students = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')

# Dictionaries
# Number of occurrences
# ---------------------------------------------in
# one two one tho three
# ---------------------------------------------out
# 0 0 1 0 0
 
a = input().split()
b = dict(zip(a, [-1 for i in range(len(a))]))
c = -1
for w in a:
    if w in b:
        b[w] += 1
        print(b[w], end = ' ')

#or with get()
counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')

#dictionary key and val interchange
# ---------------------------------------------in
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye
# ---------------------------------------------out
# Bye

s = dict()
b = dict()
n = int(input())
for i in range(n):
    key, val = input().split()
    s.update({key: val})
    b.update({val: key})
c = input()
if c in s:
    print(s[c])   
elif c in b:
    print(b[c])

#faster and shorter:
n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])

# Dictionaries
# election:
# ---------------------------------------------in
# 5
# McCain 10
# McCain 5
# Obama 9
# Obama 8
# McCain 1	
# ---------------------------------------------out
# McCain 16
# Obama 17

n = int(input())
d = {}
for i in range(n):
   key, val = input().split()
   if key in d:
       d[key] += int(val)
   else:
       d[key] = int(val)
for key, val in sorted(d.items()):
   print(key, val)

# or better
num_votes = {}
for _ in range(int(input())):
    candidate, votes = input().split()
    num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)

for candidate, votes in sorted(num_votes.items()):
    print(candidate, votes)

# Dictionaries
#most frequent word in dict low alphabet
# ---------------------------------------------in
# 1
# apple orange banana banana orange
# ---------------------------------------------out
# banana

s = dict()
b = dict()
n = int(input())
max = 0
nmax = 0
a = []
for i in range(n):
    words = input().split()
    for w in words:
        if w not in s:
            key, val = w, 1
            s[key] = val
            
        else:
            key, val = w, s.get(key)
            s[key] = s.get(key) + 1


def filter(dictObj, callback):
    nd = dict()
    for (key, val) in dictObj.items():
        if callback((key, val)):
            nd[key] = val
    return nd

r = sorted(s.items(), key=lambda i: (i[1]), reverse=True)

max = list(r)[0][1]
nd = filter(s, lambda e: int(e[1])>=max)

nd = sorted(nd, key=lambda i: i[0])
print(nd[0])

# or shorter:
counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
        
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))

# Dictionaries
# Permissions
# ---------------------------------------------in
# 4
# helloworld.exe R X
# pinglog W R
# nya R
# goodluck X W R
# 5
# read nya
# write helloworld.exe
# execute nya
# read pinglog
# write pinglog
# ---------------------------------------------out
# OK
# Access denied
# Access denied
# OK
# OK

s = dict()
b = dict()
n = int(input())
max = 0
nmax = 0
tfile = []
a = []
fn = str()
key = ''
val = ''

for i in range(n):
    tfile.append(input().split())

def ltod(x, dict):
    val = []
    for k in x:
        for j in range(len(k)):
            if j == 0:
                key = k[j]
                dict[key] = key
            else:
                val.append(k[j])
        dict[key] = ''.join(val)
        val =[]
    return dict

ltod(tfile, s)


l = int(input())
files = []
for i in range(l):
    r = input().split()
    r.reverse()
    files.append(r)


for i in files:
    for j in range(len(i)):
        if i[j] == 'write':
            i[j] = 'W'
        elif i[j] == 'execute':
            i[j] = 'X'
        elif i[j] == 'read':
            i[j] = 'R'

for i in range(len(files)):
    key, val = files[i][0], files[i][1]
    
    if key in s:
        
        if val in s.get(key):
            print('OK')
        else:
            print('Access denied')

# or pythonic:

OPERATION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    operation, file = input().split()
    if OPERATION_PERMISSION[operation] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')

# list to dict function
def ltod(list):
    mydict = {}
    val = []
    for k in list:
        for j in range(len(k)):
            if j == 0:
                key = k[j]
                dict[key] = key
            else:
                val.append(k[j])
        dict[key] = ''.join(val)
        val =[]
    return mydict

# Dictionaries
# cities in countries:
# ---------------------------------------------in
# 2
# USA Boston Pittsburgh Washington Seattle
# UK London Edinburgh Cardiff Belfast
# 3
# Cardiff
# Seattle
# London
# ---------------------------------------------out
# UK
# USA
# UK

cuntries = {}
for i in range(int(input())):
    cunt, *cit = input().split()
    cuntries[cunt] = set(cit)

for i in range(int(input())):
    city = input()
    for cunt, cit in cuntries.items():
        if city in cit:
            print(cunt)

#or a bit shorter:
motherland = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country
        
for i in range(int(input())):
    print(motherland[input()])

# Dictionaries
#sorting dict by first then second reversed

# ---------------------------------------------in
# 9
# hi
# hi
# what is your name
# my name is bond
# james bond
# my name is damme
# van damme
# claude van damme
# jean claude van damme
# ---------------------------------------------out
# damme
# is
# name
# van
# bond
# claude
# hi
# my
# james
# jean
# what
# your

counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
print(counter)

a = [(val, key) for key, val in counter.items()]

a.sort(key=lambda x: (-x[0], x[1]))
for i in range(len(a)):
    print(a[i][1])

#or a bit shorter:
n = int(input())
counts = {}
for _ in range(n):
    for word in input().split():
        counts[word] = counts.get(word, 0) + 1

freqs = [(-count, word) for (word, count) in counts.items()]

for c, word in sorted(freqs):
    print(word)

# or with counter:
from collections import Counter

words = []
for _ in range(int(input())):
    words.extend(input().split())

counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))

# Dictionaries
#English - Latin Dictionary:
# ---------------------------------------------in
# 3
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa
# ---------------------------------------------out
# 7
# baca - fruit
# bacca - fruit
# malum - apple, punishment
# multa - punishment
# pomum - apple
# popula - apple
# popum - fruit

englat = {}
lateng = {}
badies = [' -',',']
a = []
for i in range(int(input())):
    line = input()
    for i in badies:
        line = line.replace(i, '')
    eng, *lat = line.split()
    englat[eng] = set(lat)
    a.append(lat)

for key, val in englat.items():
    for elem in val:
        lateng.setdefault(elem,[])
        lateng[elem].append(key)
print(len(lateng))
for key, val in sorted(lateng.items()):   
    print(key, '- ', end='')
    print(*val, sep=', ')

#or shorter
from collections import defaultdict
from builtins import len

latin_to_english = defaultdict(list)
for i in range(int(input())):
    english_word, latin_translations_chunk = input().split(' - ')
    latin_translations = latin_translations_chunk.split(', ')
    for latin_word in latin_translations:
        latin_to_english[latin_word].append(english_word)
    
print(len(latin_to_english))
for latin_word, english_translations in sorted(latin_to_english.items()):
    print(latin_word + ' - ' + ', '.join(english_translations))