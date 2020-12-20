import pygame, sys, random

pygame.init()
def quitGame():
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
quitGame()
displayWidth = 897
displayHeight = 531

screen = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Pygame Algorithm")

red = (128,0,0)
blue = (0,0,255)
green = (0,255,0)
purple = (128,0,128)
screen.fill(red)
beforelistOfGridCoordinates = []
listOfGridCoordinates = []
listOfPathForX = []
listOfPathForY = []

class PygameObject(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width,height))
        self.image.fill((color))
        self.rect = self.image.get_rect()

    @staticmethod
    def quitGame():
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def algorithm(self,this,listOfBlock,otherRandomSprite,algorithm,randomBlock,running):
        coordinates = [(originalCoordinateX,originalCoordinateY)]
        beforeCoordinates = []
        pygame.display.update()
        while this:
            self.quitGame()
            for i in range(1):    
                self.quitGame()
                pygame.time.wait(800)
            for thing in coordinates:
                self.quitGame()
                beforeCoordinates.append((thing[0],thing[1]-89.75))
                beforeCoordinates.append((thing[0],thing[1]+89.75))
                beforeCoordinates.append((thing[0]+89.75,thing[1]))
                beforeCoordinates.append((thing[0]-89.75,thing[1]))
                pygame.display.update()
            newList = list(set(coordinates)^set(beforeCoordinates))
            for thing in coordinates:
                self.quitGame()
                del thing
            for thing in newList:
                self.quitGame()
                if (thing[0] <= 897 and thing[0] >= 0) and (thing[1] <= 531 and thing[1] >= 0):
                    if thing[0]==listOfBlock[0] and thing[1]==listOfBlock[1]:
                        self.quitGame()
                        screen.blit(otherRandomSprite,(thing[0],thing[1]))
                        if listOfBlock[0]==originalCoordinates[0]:
                            if listOfBlock[1]>originalCoordinates[1]:
                                difference=listOfBlock[1]
                                for block in range(int((listOfBlock[1]/89.75)-(originalCoordinates[1]/89.75))):
                                    difference-=89.75
                                    screen.blit(otherRandomSprite,(listOfBlock[0],difference))
                            elif listOfBlock[1]<originalCoordinates[1]:
                                difference=listOfBlock[1]
                                for block in range(int((originalCoordinates[1]/89.75)-(listOfBlock[1]/89.75))):
                                    difference+=89.75
                                    screen.blit(otherRandomSprite,(listOfBlock[0],difference))
                        if listOfBlock[0]>originalCoordinates[0]:
                            difference = listOfBlock[0]
                            for block in range(int(((listOfBlock[0]/89.75)-(originalCoordinates[0]/89.75)))):
                                self.quitGame()
                                difference-=89.75
                                screen.blit(otherRandomSprite,(difference,thing[1]))
                                listOfPathForX.append((difference,thing[1]))
                        elif listOfBlock[0]<originalCoordinates[0]:
                            difference = listOfBlock[0]
                            for block in range(int((((originalCoordinates[0])//89.75)-(listOfBlock[0]//89.75)))):
                                self.quitGame()
                                difference+=89.75
                                screen.blit(otherRandomSprite,(difference,thing[1]))
                                listOfPathForX.append((difference,thing[1]))
                        if listOfBlock[1]>originalCoordinates[1] and not listOfBlock[0]==originalCoordinates[0]:
                            difference = listOfBlock[1]
                            for block in range(int(((listOfBlock[1]//89.75)-(originalCoordinates[1]//89.75)))):
                                self.quitGame()
                                difference-=89.75
                                screen.blit(otherRandomSprite,(listOfPathForX[(len(listOfPathForX)-1)][0],difference))
                        elif listOfBlock[1]<originalCoordinates[1] and not listOfBlock[0]==originalCoordinates[0]:
                            difference = listOfBlock[1]
                            for block in range(int(((originalCoordinates[1]//89.75)-(listOfBlock[1]//89.75)))):
                                self.quitGame()
                                difference+=89.75
                                screen.blit(otherRandomSprite,(listOfPathForX[(len(listOfPathForX)-1)][0],difference))
                        pygame.display.update()
                        running = False
                    else:
                        if thing[0]==originalCoordinateX and thing[1]==originalCoordinateY:
                            continue
                        else:
                            screen.blit(self.image,(thing[0],thing[1]))
                else:
                    continue
            pygame.display.update()
            for thing in newList:
                self.quitGame()
                coordinates.append((thing[0],thing[1]))

    def randomPlace(self,listOfBlock):
        screen.blit(self.image,(listOfBlock[0],listOfBlock[1]))

class Map:
    def __init__(self,width,length): 
        self.width = width
        self.length = length

    @staticmethod
    def quitGame():
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def lineOfBlocks(self,yChange=0,color=(255,255,255)):
        xChange = 0
        for block in range(self.width):
            self.quitGame()
            pygame.draw.rect(screen,color,((0 + xChange),(0 + yChange),89.75,89.75),5)
            listOfGridCoordinates.append((xChange,0))
            xChange += 89.75

    def lineMultipliedDownward(self,yChange=0):
        for i in range(self.length):
            self.quitGame()
            yChange += 89.75
            self.lineOfBlocks(yChange)

    def addToCoordinatesList(self):
        yChange = 0
        for i in range(self.length-1):
            self.quitGame()
            yChange += 89.75
            for thing in listOfGridCoordinates:
                beforelistOfGridCoordinates.append((thing[0],yChange))
        for thing in beforelistOfGridCoordinates:
            self.quitGame()
            listOfGridCoordinates.append(thing)

theMap = Map(10,5)
theMap.lineOfBlocks()
theMap.lineMultipliedDownward()
theMap.addToCoordinatesList()
originalCoordinates = listOfGridCoordinates[random.randint(0,len(listOfGridCoordinates)-1)]
originalCoordinateX = originalCoordinates[0]
originalCoordinateY = originalCoordinates[1]
startOfAlgorithmX = originalCoordinates[0]
startOfAlgorithmY = originalCoordinates[1]
firstBlock = PygameObject(purple,89.75,89.75)
algorithm = PygameObject(green,89.75,89.75)
algorithm.rect.x = startOfAlgorithmX
algorithm.rect.y = startOfAlgorithmY
originalCoordinates = (originalCoordinateX,originalCoordinateY)
print(listOfGridCoordinates)
listOfGridCoordinates.remove((startOfAlgorithmX,startOfAlgorithmY))
randomBlock = listOfGridCoordinates[random.randint(0,len(listOfGridCoordinates)-1)]
print(randomBlock)

randomThing = PygameObject(blue,89.75,89.75)
randomThing.rect.x = randomBlock[0]
randomThing.rect.y = randomBlock[1]

running = True
while running:
    algorithm.quitGame()
    pygame.display.update()
    screen.blit(firstBlock.image,algorithm.rect)
    randomThing.randomPlace(randomBlock)
    algorithm.algorithm(running,randomBlock,randomThing.image,algorithm,randomBlock,running)
    pygame.display.update()

algorithm.quitGame()
