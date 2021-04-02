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


