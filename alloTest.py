# %%
import random

T = random.randint(1,100)
y = 0
Ai = []
k = 1
for i in range(T):
    i +=1
    N = random.randint(1,100)
    B = random.randint(1,1000000)
    for j in range(N):
        Ai.append(random.randint(1,1000))
        Ai.sort()
    for k in range(N):
        Bleft = B-Ai[k]
        
        if Ai[k]<Bleft:
            y += 1
            B = Bleft
        else:
            break
    print("Case #", i, ": ", y, sep='')
    N = 0
    B = 0
    Ai = []
    y = 0
