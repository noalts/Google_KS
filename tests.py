max = 0
sec = 0
element = -1
l = []
e = 0
while element != 0:
    element = int(input())
    #l.append(element)
    if element < max:
        max = element
    elif element > sec:
        sec = element
    elif max > sec:
        e = element
        
print(e)