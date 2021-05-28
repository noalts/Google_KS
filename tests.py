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