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