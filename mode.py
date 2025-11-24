from enum import Enum
import time
from PacMan import *
from Ghost import *
from Actor import *



class Mode(Enum):
    NORMAL = 0
    INVERTED = 1
    
mode = Mode.NORMAL

def fire_inverted(actors):
    global mode
    print("Inverted Mode Activated")
    for actor in actors:
        if not isinstance(actor,PacMan):
            actor.is_vulnerable = True
    mode = Mode.INVERTED
    time.sleep(5)
    mode = Mode.NORMAL
    for actor in actors:
        if not isinstance(actor,PacMan):
            actor.is_vulnerable = False
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


