piles = [3,7,2,3]
scoreA = 0
scoreL = 0
numpiles = len(piles)
A = 1
L = 0
while numpiles != 1:
    if A > L:
        if piles[0]-piles[1] >= piles[-1]-piles[-2]:
            scoreA += piles[0]
            piles.remove(piles[0])
            A -= 1
            L += 1
        else:    
            scoreA += piles[len(piles)-1]
            piles.remove(piles[len(piles)-1])
            A -= 1
            L += 1
    else:
        if piles[0] >= piles[len(piles)-1]:
            scoreL += piles[0]
            piles.remove(piles[0])
            A += 1
            L -= 1
        else:    
            scoreL += piles[len(piles)-1]
            piles.remove(piles[len(piles)-1])
            A += 1
            L -= 1
    numpiles = len(piles)           
if A > L:
    scoreA += piles[0]
else:
    scoreL += piles[0]

if scoreA > scoreL:
    print('True')
else:
    print('False')