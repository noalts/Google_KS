s = dict()
b = dict()
n = int(input())
max = 0
nmax = 0
tfile = []
a = []
fn = str()
key = ''
val = ''

for i in range(n):
    tfile.append(input().split())

def ltod(x, dict):
    val = []
    for k in x:
        for j in range(len(k)):
            if j == 0:
                key = k[j]
                dict[key] = key
            else:
                val.append(k[j])
        dict[key] = ''.join(val)
        val =[]
    return dict

ltod(tfile, s)


l = int(input())
files = []
for i in range(l):
    r = input().split()
    r.reverse()
    files.append(r)


for i in files:
    for j in range(len(i)):
        if i[j] == 'write':
            i[j] = 'W'
        elif i[j] == 'execute':
            i[j] = 'X'
        elif i[j] == 'read':
            i[j] = 'R'

for i in range(len(files)):
    key, val = files[i][0], files[i][1]
    
    if key in s:
        
        if val in s.get(key):
            print('OK')
        else:
            print('Access denied')


            # print(i[j])
            # if i[j+1] in s[key]:

            
    



# class file:
#     def __init__(self, fi, read, write, ex):
#         self.fi = fi
#         self.read = read
#         self.write = write
#         self.ex = ex
#     def __repr__(self):
#         return repr((self.fi, self.read, self.write, self.ex))


#     for w in file:
#         if w not in s:
#             key, val = w, 1
#             s[key] = val
            
#         else:
#             key, val = w, s.get(key)
#             s[key] = s.get(key) + 1


# def filter(dictObj, callback):
#     nd = dict()
#     for (key, val) in dictObj.items():
#         if callback((key, val)):
#             nd[key] = val
#     return nd

# r = sorted(s.items(), key=lambda i: (i[1]), reverse=True)

# max = list(r)[0][1]
# nd = filter(s, lambda e: int(e[1])>=max)

# nd = sorted(nd, key=lambda i: i[0])
# print(nd[0])
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