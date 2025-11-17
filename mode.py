from enum import Enum
import time
from PacMan import *
from Ghost import *
from Actor import *

mode = 0

class Mode(Enum):
    NORMAL = 0
    INVERTED = 1
    
def fire_inverted():
    mode = Mode.INVERTED
    time.sleep(5)
    mode = Mode.NORMAL

def check_collision(actors):
    for actor in actors:
        if actor.self == Ghost:
            if (actor.x, actor.x) == (PacMan.x, PacMan.y):
                if mode == Mode.NORMAL:
                    print("Game Over")
                else:
                    print("kill ghsot")
