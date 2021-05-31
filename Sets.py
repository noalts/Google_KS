#print number of distinct elements in set:

#-----------------------------------------in
# 1 2 3 2 1
#-----------------------------------------out
# 3

a = {str(s) for s in input().split()}
print(len(a))

#print distinct elements of set:
a = {int(s) for s in input().split()}
b = set()
b.update(a)
print(*b)

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

#distinct words in given text:

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