
from random import randint
from Wall import Wall

class Point:
    def __init__(self, x, y, typ):
        self.x = x
        self.y = y
        r = randint(1, 50)
        if r in [48, 49]:
            self.typ = "gross"
        elif r == 50:
            self.typ = "kirsche"
        else:
            self.typ = "klein"

# Rastergröße
width = 23
height = 23

# Erstelle eine Liste mit Punkten für jedes Feld im Raster

punkte = {}
for x in range(width):
    for y in range(height):
        if not Wall.checkForWall(x,y):
            punkte[(x,y)] = Point(x, y, typ="self.typ")

punkte = {}
for x in range(width):
    for y in range(height):
        if not Wall.checkForWall(x,y):
            punkte[(x,y)] = Point(x, y, typ="self.typ")
    




