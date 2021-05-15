a = input().split()
b = dict(zip(a, [-1 for i in range(len(a))]))
c = -1
for w in a:
    if w in b:
        b[w] += 1
        print(b[w], end = ' ')





