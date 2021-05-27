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