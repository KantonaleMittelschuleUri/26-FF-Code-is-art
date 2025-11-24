from enum import Enum
import time
from PacMan import *
from Ghost import *
from Actor import *



class Mode(Enum):
    NORMAL = 0
    INVERTED = 1
    
mode = Mode.NORMAL

def fire_inverted():
    global mode
    print("Inverted Mode Activated")
    mode = Mode.INVERTED
    time.sleep(5)
    mode = Mode.NORMAL
    print("Normal Mode Activated")

def check_collision(actors):
    global mode
    pacman = None
    for actor in actors:
        if isinstance(actor,PacMan):
            pacman = actor
        elif isinstance(actor,Ghost):
            if (actor.x, actor.x) == (pacman.x, pacman.y):
                if mode == Mode.NORMAL:
                    print("Game Over")
                else:
                    print("kill ghsot")


