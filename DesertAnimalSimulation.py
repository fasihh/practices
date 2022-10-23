import random as r
import time
import os

animal = "A"
food = "F"
gridSize = 20
animalCount = 5
foodCount = 1

class Desert:
    grid = []
    animalList = []
    numberOfAnimals = 0

    def __init__(self):
        self.grid = [["." for i in range(gridSize)] for j in range(gridSize)]

        for i in range(animalCount):
            AnimalObj = Animal()
            self.animalList.append(AnimalObj)
            self.IncrementNumberCounter()

        for j in range(foodCount):
            self.GenerateFood()

        self.stepCounter = 0

    def IncrementNumberCounter(self):
        self.numberOfAnimals += 1

    def GenerateFood(self):
        placed = False
        while not placed:
            X = r.randint(0, gridSize - 1)
            Y = r.randint(0, gridSize - 1)

            if self.grid[Y][X] != food and self.grid[Y][X] != animal:
                self.grid[Y][X] = food
                placed = True

    def DisplayGrid(self):

        for x in range(len(self.animalList)):
            Xpos = self.animalList[x].across
            Ypos = self.animalList[x].down
            self.grid[Ypos][Xpos] = animal

        for i in range(gridSize):
            display = ""
            for j in range(gridSize):
                display = display + "  " + self.grid[j][i]
            print(display)
        print("total animals: " + str(self.numberOfAnimals) + "\n ")



class Animal:
    across = 0
    down = 0

    def __init__(self):
        placeX = r.randint(0, gridSize - 1)
        placeY = r.randint(0, gridSize - 1)
        self.across = placeX
        self.down = placeY
        self.score = 0

    def SetDown(self, val):
        self.down = val

    def SetAcross(self, val):
        self.across = val

    def Move(self):
        desert.grid[self.down][self.across] = "."

        self.SetAcross(GenerateChangeInCoordinate(self.across))
        self.SetDown(GenerateChangeInCoordinate(self.down))

        if desert.grid[self.down][self.across] == food:
            self.EatFood()
            desert.grid[self.down][self.across] = animal
        elif desert.grid[self.down][self.across] == animal:
            placed = False
            while not placed:
                self.SetAcross(GenerateChangeInCoordinate(self.across))
                self.SetDown(GenerateChangeInCoordinate(self.down))
                if desert.grid[self.down][self.across] != animal:
                    placed = True
        else:
            desert.grid[self.down][self.across] = animal

    def EatFood(self):
        self.score += 1
        desert.GenerateFood()
        desert.IncrementNumberCounter()
        desert.animalList.append(Animal())


def GenerateChangeInCoordinate(val):
    if val == gridSize - 1:
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


def Start(val):
    count = 0
    while count != val:
        time.sleep(3)
        count += 1
        os.system('cls')
        Wave()
    print("All animal scores: ")
    for i in range(len(desert.animalList)):
        print(desert.animalList[i].score)


loopCount = int(input("how many times do you want to loop?: "))
gridSize = int(input("how much grid space? (square space, one dimension only): "))
animalCount = int(input("how many animals at the start?: "))
foodCount = int(input("how much food throughout the simulation?: "))
desert = Desert()
Start(loopCount)





