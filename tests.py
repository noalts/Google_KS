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
# print(s)
# print(s)
# res =   
# print(res)


# for i in words:
    
    # key, val = input().split()
    # # votes += int(val)
    # s.update({key: val})
    # s[key] = int(s[key]) + int(s[key])
    # votes = 0
    # vote += int(val)
    # val = int(val) + vote
    # s[key] += val
    
    # s[key] = key
    # s[val] = int(val) + int(val)

# c = input()
# if c in s:
#     print(s[c])   
# elif c in b:
#     print(b[c])