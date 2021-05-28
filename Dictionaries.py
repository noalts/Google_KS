#Dictionaries
# Number of occurrences
# ---------------------------------------------in
# one two one tho three
# ---------------------------------------------out
# 0 0 1 0 0

a = input().split()
b = dict(zip(a, [-1 for i in range(len(a))]))
c = -1
for w in a:
    if w in b:
        b[w] += 1
        print(b[w], end = ' ')

#or with get()
counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')

#dictionary key and val interchange synonyms
# ---------------------------------------------in
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye
# ---------------------------------------------out
# Bye

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

#faster and shorter:
n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])

#election:
# ---------------------------------------------in
# 5
# McCain 10
# McCain 5
# Obama 9
# Obama 8
# McCain 1	
# ---------------------------------------------out
# McCain 16
# Obama 17

n = int(input())
d = {}
for i in range(n):
   key, val = input().split()
   if key in d:
       d[key] += int(val)
   else:
       d[key] = int(val)
for key, val in sorted(d.items()):
   print(key, val)


# or better
num_votes = {}
for _ in range(int(input())):
    candidate, votes = input().split()
    num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)

for candidate, votes in sorted(num_votes.items()):
    print(candidate, votes)

#most frequent word in dict low alphabet
# ---------------------------------------------in
# 1
# apple orange banana banana orange
# ---------------------------------------------out
# banana

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

# or shorter:
counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
        
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))

# Permissions
# ---------------------------------------------in
# 4
# helloworld.exe R X
# pinglog W R
# nya R
# goodluck X W R
# 5
# read nya
# write helloworld.exe
# execute nya
# read pinglog
# write pinglog
# ---------------------------------------------out
# OK
# Access denied
# Access denied
# OK
# OK

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

# or pythonic:

OPERATION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    operation, file = input().split()
    if OPERATION_PERMISSION[operation] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')

# list to dict function#
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

#cities in countries:
# ---------------------------------------------in
# 2
# USA Boston Pittsburgh Washington Seattle
# UK London Edinburgh Cardiff Belfast
# 3
# Cardiff
# Seattle
# London
# ---------------------------------------------out
# UK
# USA
# UK

cuntries = {}
for i in range(int(input())):
    cunt, *cit = input().split()
    cuntries[cunt] = set(cit)

for i in range(int(input())):
    city = input()
    for cunt, cit in cuntries.items():
        if city in cit:
            print(cunt)

#or a bit shorter:
motherland = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country
        
for i in range(int(input())):
    print(motherland[input()])

#sorting dict by first then second reversed
# ---------------------------------------------in
# 9
# hi
# hi
# what is your name
# my name is bond
# james bond
# my name is damme
# van damme
# claude van damme
# jean claude van damme
# ---------------------------------------------out
# damme
# is
# name
# van
# bond
# claude
# hi
# my
# james
# jean
# what
# your

counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
print(counter)

a = [(val, key) for key, val in counter.items()]

a.sort(key=lambda x: (-x[0], x[1]))
for i in range(len(a)):
    print(a[i][1])

#or a bit shorter:
n = int(input())
counts = {}
for _ in range(n):
    for word in input().split():
        counts[word] = counts.get(word, 0) + 1

freqs = [(-count, word) for (word, count) in counts.items()]

for c, word in sorted(freqs):
    print(word)

# or with counter:
from collections import Counter

words = []
for _ in range(int(input())):
    words.extend(input().split())

counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))

#English - Latin Dictionary:
# ---------------------------------------------in
# 3
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa
# ---------------------------------------------out
# 7
# baca - fruit
# bacca - fruit
# malum - apple, punishment
# multa - punishment
# pomum - apple
# popula - apple
# popum - fruit

englat = {}
lateng = {}
badies = [' -',',']
a = []
for i in range(int(input())):
    line = input()
    for i in badies:
        line = line.replace(i, '')
    eng, *lat = line.split()
    englat[eng] = set(lat)
    a.append(lat)

for key, val in englat.items():
    for elem in val:
        lateng.setdefault(elem,[])
        lateng[elem].append(key)
print(len(lateng))
for key, val in sorted(lateng.items()):   
    print(key, '- ', end='')
    print(*val, sep=', ')

#or shorter
from collections import defaultdict

latin_to_english = defaultdict(list)
for i in range(int(input())):
    english_word, latin_translations_chunk = input().split(' - ')
    latin_translations = latin_translations_chunk.split(', ')
    for latin_word in latin_translations:
        latin_to_english[latin_word].append(english_word)
    
print(len(latin_to_english))
for latin_word, english_translations in sorted(latin_to_english.items()):
    print(latin_word + ' - ' + ', '.join(english_translations))