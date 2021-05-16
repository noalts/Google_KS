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