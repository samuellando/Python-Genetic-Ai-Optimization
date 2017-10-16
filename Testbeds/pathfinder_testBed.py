import random
import numpy as np

SBLength = 360

def test(SB,frames):
    c = 0
    intList = []
    while c < SBLength:
        Neg = -1 if SB[c] == 0 else 1
        intList.append(float(Neg*int(SB[c+1:c+14],2))/10000)
        c+=15
    wo = np.array([[intList[0],intList[1],intList[2],intList[3]],[intList[4],intList[5],intList[6],intList[7]]])
    wt = np.array([[intList[8],intList[9],intList[10],intList[11]],[intList[12],intList[13],intList[14],intList[15]],[intList[16],intList[17],intList[18],intList[19]],[intList[20],intList[21],intList[22],intList[23]]])
    score = 1
    posX = random.randint(0,100)
    posY = random.randint(0,100)
    destX = random.randint(0,100)
    destY = random.randint(0,100)
    c = 0
    while (c <= frames):
        c+=1
        hor = (posX-destX)
        ver = (posY-destY)
        I = np.array([[hor,ver]])
        H = I.dot(wo)
        O = H.dot(wt)[0]
	dir = O.tolist()
	dir = dir.index(max(dir))
	if dir == 0:
		posY+=1
	if dir == 1:
		posY-=1
	if dir ==2:
		posX+=1
	if dir == 3:
		posX-=1
	if posX == 101:
		posX = 100
	if posX == -1:
		posX = 1
	if posY == 101:
		posY = 100
	if posY == -1:
		posY = 0
	if posX == destX and posY == destY:
		score+=1
		destX = random.randint(0,100)
		destY = random.randint(0,100)
    return(1.00/float(score))
