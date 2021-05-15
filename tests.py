s = dict()
n = int(input())
for i in range(n):
    key, val = input().split()
    s.update({key: val})
c = input()
for key, val in s.items():
    if c in s:
        print(s[val])
        break
    elif s[val] == c:
        print(s[key])
        break