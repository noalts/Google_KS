a = [int(s) for s in input().split()]
b = [*set(a)]
c = []
for i in range(len(b) - 1):
    if a.count(b[i]) == 1:
        print(b[i])