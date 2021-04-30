n = int(input())
ans = ''
t = ''
a = {int(s) for s in range(1,n+1)}
b = set()

while ans != 'HELP':
    q = input().split()
    ans = input()
    if ans == 'YES':
        pass
    elif ans == 'NO':
        [a.discard(int(i)) for i in q]
    else:
        break
else:
    print (*a)



