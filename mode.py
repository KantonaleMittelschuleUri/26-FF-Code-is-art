from enum import Enum
import time
from PacMan import *
from Ghost import *
from Actor import *
from GhostState import GhostState



fire_inverted_count = 0

def fire_inverted(actors):
    global fire_inverted_count
    fire_inverted_count += 1
    for actor in actors:
        if not isinstance(actor,PacMan):
            actor.ghost_state = GhostState.VULNERABLE
    time.sleep(10)
    fire_inverted_count -= 1
    if fire_inverted_count == 0:
        for actor in actors:
            if not isinstance(actor,PacMan) and actor.ghost_state == GhostState.VULNERABLE:
                actor.ghost_state = GhostState.CHASE

def check_collision(actors):
    pacman = None
    for actor in actors:
        if isinstance(actor,PacMan):
            pacman = actor
        elif isinstance(actor,Ghost):
            if ((actor.x, actor.y) == (pacman.x, pacman.y) or 
               (pacman.x + pacman.direction.value[0], pacman.y + pacman.direction.value[1]) == (actor.x, actor.y)):
                if actor.ghost_state == GhostState.CHASE:
                    print("Game Over")
                else:
                    actor.ghost_state = GhostState.EATEN


