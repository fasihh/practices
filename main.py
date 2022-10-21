import random


class IslandClass:
    found = "X"
    notfound = "O"
    treasure = "T"
    sand = "."
    status = False
    Grid = []


    def __init__(self):
        self.Grid = [[self.sand for i in range(10)] for i in range (30)]


    def HideTreasure(self):
        treasureX = random.randint(0, 29)
        treasureY = random.randint(0, 9)

        if self.Grid[treasureX][treasureY] != self.treasure:
            self.Grid[treasureX][treasureY] = self.treasure
        else:
            treasureX = random.randint(0, 29)
            treasureY = random.randint(0, 9)
            self.Grid[treasureX][treasureY] = self.treasure


    def DigHole(self, X, Y):
        if self.Grid[X][Y] == self.treasure:
            self.Grid[X][Y] = self.found
            self.status = True
        else:
            self.Grid[X][Y] = self.notfound


    def GetSquare(self, X, Y):
        return self.Grid[X][Y]


    def GetStatus(self):
        if self.status == True:
            print("you found the treasure! :)")
        else:
            print("you couldn't find the treasure. :(")


def DisplayGrid():
    for i in range(10):
        square = ""
        for col in range(30):
            square = square + " " + Island.GetSquare(col, i)
        print(square)
    print(" ")


def StartDig():
    x = int(input("input value for col: "))
    y = int(input("input value for row: "))

    Island.DigHole(x, y)


Island = IslandClass()

DisplayGrid()

for i in range(3):
    Island.HideTreasure()

StartDig()

DisplayGrid()

Island.GetStatus()
