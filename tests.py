a = [int(i) for i in input().split()]
x = a.index(max(a))
y = a.index(min(a))
q = 0
r = 0
a[x], a[y] = a[y], a[x]
print(*a)