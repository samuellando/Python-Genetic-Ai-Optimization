"""
IMPORTS
"""
import random #For the selection of the random loactions of food and player
import numpy as np #For arrays and array operations
import pygame #For the graphical display of frames
import time #For pause between frames

"""
PARAMETERS
"""
numFrames = 10000 #Number of frames to compute
frameRate = 1 #Number of frames per secound
gene = "111110011111110010110001000111101011111111001111011111111100001101111100011011110001100111110111111111101111111000111000110001110111111101111100101010000101000100111111100110000010101110011110101011000110011110110110010100111100111111111001100111110010100001011000111101110111011101110011001101010100011000101001000010111111110101101110111001011110100000011110"
#Binary reprisentation of AI

"""
FRAME COMPUTATION FUNCTIONS
"""
def framesCalc(wo,wt,numFrames):
    """
    function that retunrs table of position player, food and the score for each frame calculated
    """
    score = 0 #initializ number of time food is atained
    posX = random.randint(0,100) #random selection of x position of player (position)
    posY = random.randint(0,100) #random selection of y position of player (position)
    destX = random.randint(0,100) #random selection of x position of food (destination)
    destY = random.randint(0,100) #random selection of y position of food (destination)
    frames = [] #initalize returned table
    c = 0 #current frame being calculated
    while (c < numFrames):
        c+=1 #keep curent frame number up to date
        horDiff = (posX-destX) #calculate difference in horizontal postion of player and food
        verDiff = (posY-destY) #calculate difference in vertical postion of player and food
        I = np.array([[horDiff,verDiff]]) #Create input array for AI
        H = I.dot(wo) #Calculate hidden array of AI
        O = H.dot(wt) #Calculate output array of ai
        move = O[0].tolist() #tunr numpy array into python list
        moveIndex = move.index(max(move)) #Take the index of the hihest value in output list
        if moveIndex == 0: #if index is zero move up
            posY+=1 #increse vertical position of player
        if moveIndex == 1: #if index is one move down
            posY-=1 #decrease vertical position of player
        if moveIndex ==2: #if index is two move right
            posX+=1 #increase horizontal position of player
        if moveIndex == 3: #if index is three left
            posX-=1 #decrease horizontal position of player
        if posX == 101: #if the horizontal position of player is too high
            posX = 100 #go to max horizontal value
        if posX == -1: #if the horizontal positon of player is too low
            posX = 0 #go to min horizontal value
        if posY == 101: #if the vertical position of player is too high
            posY = 100 #go to max vertical value
        if posY == -1: #if the vertical position of play is too low
            posY = 0 #go to min vertical value
        if posX == destX and posY == destY: #if the play is in the same position as food
            score+=1 #increase thge score
            destX = random.randint(0,100) #set a new horizontal position for the food
            destY = random.randint(0,100) #set a new vertical position for the food
        frames.append([score,posX,posY,destX,destY]) #append data to table
    return(frames)#return table
"""
COMPUTATION
"""
"""
convert binary reprisentation of AI to arrays of weights
"""
print("Calculateing...") #Make user aware that the computation has begun
wList = [] #initalize weights list
c = 0 #index binary vaule being converted
while c < 360:
    Neg = -1 if gene[c] == 0 else 1 #negative cary ofver to wieghts
    wList.append(float(Neg*int(gene[c+1:c+14],2))/10000) #convert next 14 bits to float and multiply by neg, then devide to normalize
    c+=15 #keep index up to date
WO = np.array([[wList[0],wList[1],wList[2],wList[3]],[wList[4],wList[5],wList[6],wList[7]]]) #create first weight array
WT = np.array([[wList[8],wList[9],wList[10],wList[11]],[wList[12],wList[13],wList[14],wList[15]]
,[wList[16],wList[17],wList[18],wList[19]],[wList[20],wList[21],wList[22],wList[23]]]) #create last weight array
"""
compute frames
"""
frames = framesCalc(WO,WT,numFrames)

"""
GRAPHICAL PRESENTATION
"""
input("Press enter to begin viewing") #wait for user to be ready to view
class Player: #class for the player
    x = 0 #initalize x position
    y = 0 #initialize y position
    def setLoc(self,x,y): #allow position to be updated
        self.x = x*5 #update x location and multiply by five for grid match
        self.y = y*5 #update y location and multiply by five for grid match
class Food: #class for food
    x = 0 #initialize x position
    y = 0 #initialize y position
    def setLoc(self,x,y): #allow for position to be updates
        self.x = x*5 #update x locagtion and multiply by 5 for grid match
        self.y = y*5 #update y postion and multiply by 5 for grid match
class App: #class for display window
    windowWidth = 505
    windowHeight = 505
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = Player()
        self.food = Food()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Score: 0')
        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        pygame.draw.rect(self._display_surf,(0,255,0),(self.player.x,self.player.y,5,5),0)
        pygame.draw.rect(self._display_surf,(255,0,0),(self.food.x,self.food.y,5,5),0)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        i = 0
        while( self._running ):
            frame = frames[i]

            time.sleep(1/frameRate)
            score, posX, posY, destX, destY = frame[0], frame[1], frame[2], frame[3], frame[4]
            pygame.display.set_caption('Score: '+str(score))
            self.player.setLoc(posX,posY)
            self.food.setLoc(destX,destY)
            self.on_loop()
            self.on_render()
            i += 1
            if (i+1) == len(frames):
                break
        self.on_cleanup()

theApp = App()
theApp.on_execute()
