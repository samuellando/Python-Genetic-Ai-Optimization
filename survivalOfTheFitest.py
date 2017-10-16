import random
import os

import Testbeds.snake_testBed as tb
numOfGeneomes = 100
numberOfGenerations = 1000
numberOfMutations = 25
numberOfFrames = 10000
survivalCutOff = 0.1

class genome():
    def __init__(self, sb):
        self.SB = sb
        self.C = 0
        self.ANFV = 2
    def rCreate(self):
        while len(self.SB) < tb.SBLength:
            self.SB += str(random.randint(0,1))
    def mate(self, so):
        crossoverPoints = random.randint(1,5)
        crossoverPoints = 2*crossoverPoints+1
        crossoverLocations = int(round(tb.SBLength/crossoverPoints))
        childSB = ""
        i = 1
        while i <= crossoverPoints:
            if round(i/2) == i/2:
                childSB += self.SB[(i-1)*crossoverLocations:i*crossoverLocations]
            else:
                childSB += so.SB[(i-1)*crossoverLocations:i*crossoverLocations]
            i += 1
        while len(childSB) < tb.SBLength:
            childSB += str(random.randint(0,1))
        return(childSB)

def getKey(Item):
    return Item.C

def survivalOfTheFittest(size, itterations, mutations, testFrames, cutOff):
    try:
        generation = []
        i = 0
        while i < itterations:
            if i == 0 and len(generation) < size:
                gene = genome("")
                gene.rCreate()
                generation.append(gene)
            elif len(generation) < size-mutations:
                gene = genome(generation[random.randint(0,len(generation)-1)].mate(generation[random.randint(0,len(generation)-1)]))
                generation.append(gene)
            elif len(generation) < size:
                gene = genome("")
                gene.rCreate()
                generation.append(gene)
            else:
                i += 1
                sumC = 0.00
                for gene in generation:
                    gene.C = tb.test(gene.SB,testFrames)
                generation = sorted(generation, key=getKey)
                for gene in generation:
                    sumC += gene.C
                avC = sumC/size
                for gene in generation:
                    gene.C = gene.C/sumC
                sumC = 0.00
                c = 1
                while c < len(generation):
                    gene = generation[c-1]
                    sumC += gene.C
                    gene.ANFV = sumC/1
                    if gene.ANFV >= cutOff:
                        del generation[c]
                    else:
                        c = c+1
                os.system("clear")
                print("on Generation "+str(i)+" of "+str(itterations))
        print(generation[0].SB)
        print(generation[0].C)
    except:
        print(generation[0].SB)
        print(generation[0].C)

if __name__ == "__main__":
    survivalOfTheFittest(numOfGeneomes, numberOfGenerations, numberOfMutations, numberOfFrames, survivalCutOff)
