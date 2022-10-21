import random as r
import time


class Desert:
    grid = []
    animalList = []
    numberOfAnimals = 0

    def __init__(self):
        self.grid = [["." for i in range(40)] for j in range(40)]

        for i in range(5):
            AnimalObj = Animal()
            self.animalList.append(AnimalObj)

        for j in range(10):
            self.GenerateFood()

        self.stepCounter = 0

    def IncrementStepCounter(self):
        pass

    def GenerateFood(self):
        placed = False
        while not placed:
            X = r.randint(0, 39)
            Y = r.randint(0, 39)

            if self.grid[Y][X] != "F" and self.grid[Y][X] != "A":
                self.grid[Y][X] = "F"
                placed = True


    def DisplayGrid(self):

        for x in range(len(self.animalList)):
            Xpos = self.animalList[x].across
            Ypos = self.animalList[x].down
            self.grid[Ypos][Xpos] = "A"


        for i in range(40):
            display = ""
            for j in range(40):
                display = display + "  " + self.grid[j][i]
            print(display)

        print(" ")




class Animal:
    across = 0
    down = 0

    def __init__(self):
        placeX = r.randint(0, 39)
        placeY = r.randint(0, 39)
        self.across = placeX
        self.down = placeY
        self.score = 0

    def SetDown(self, val):
        self.down = val

    def GetDown(self):
        return self.down

    def SetAcross(self, val):
        self.across = val

    def GetAcross(self):
        return self.across

    def Move(self):
        desert.grid[self.down][self.across] = "."

        self.across = GenerateChangeInCoordinate(self.across)
        self.down = GenerateChangeInCoordinate(self.down)

        if desert.grid[self.down][self.across] == "F":
            self.EatFood()
            desert.grid[self.down][self.across] = "A"
        else:
            desert.grid[self.down][self.across] = "A"


    def EatFood(self):
        self.score += 1
        desert.GenerateFood()
        desert.animalList.append(Animal())


def GenerateChangeInCoordinate(val):
    if val == 39:
        val += r.randint(-1, 0)
    elif val == 0:
        val += r.randint(0, 1)
    else:
        val += r.randint(-1, 1)

    return val


def Wave():
    for i in range(len(Desert.animalList)):
        desert.animalList[i].Move()
    desert.DisplayGrid()


desert = Desert()

desert.DisplayGrid()


while True:
    time.sleep(0.5)
    Wave()
