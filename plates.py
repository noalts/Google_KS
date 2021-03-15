T = int(input())
y = 0
Ptrack = 0
Vcount = 0
for i in range(T):
    N, K, P = map(int,input().split()) # N = stacks; K = plates; P = needed plates
    for stacks in range(N):
        Beau = list(map(int,input().split())) #Beau = value of plate
        Bmax = max(Beau)
        for x in Beau:            
            if x != Bmax and Ptrack <= P:
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