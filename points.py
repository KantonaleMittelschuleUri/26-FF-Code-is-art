
class Point:
    def __init__(self, x, y, typ="klein"):
        self.x = x
        self.y = y
        self.typ = typ  # "klein", "gross", "kirsche"


# Rastergröße
width = 23
height = 23

# Erstelle eine Liste mit Punkten für jedes Feld im Raster
punkte = {}
for x in range(width):
    for y in range(height):
        punkte[(x,y)] = Point(x, y, "klein")

# Beispiel-Ausgabe
print(punkte)

