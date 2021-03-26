# %%
import random, sys

T = int(input())
y = 0

for i in range(T):
    i +=1
    N, B = map(int,input().split())
    Ai = list(map(int,input().split()))
    Ai.sort()
    for k in Ai:        
        if k<=B:
            Bleft = B-k
            y += 1
            B = Bleft
        else:
            break
    print("Case #", i, ": ", y, sep='')
    N = 0
    B = 0
    Ai = []
    y = 0
