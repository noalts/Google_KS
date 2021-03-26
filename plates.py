T = int(input())
y = 0
Ptrack = 0
Vcount = 0

def knapsack(K,P):
    n=len(K)
    

for i in range(T):
    N, K, P = map(int,input().split()) # N = stacks; K = plates; P = needed plates
    for stacks in range(1,N):
        Beau = list(map(int,input().split())) #Beau = list of values of plate
        Bmax = max(Beau)
        Bsort = sorted(Beau)
        Bmaxindex = Beau.index(Bmax)
        Pindex = 0
        for x in Beau:

            if Ptrack <= P:
                
                if Pindex <= Bmaxindex:
                    Pindex += 1
                    Ptrack += 1 
                    Vcount += x
            else:
                Vcount += Bmax
                Ptrack += 1
                break
    print("Case #", i, ": ", Vcount, sep='')    
        
        #         
        #
        #         break