from Directions import Directions
from GhostState import GhostState
from Wall import Wall
import math
import pygame


class Actor:



    def __init__(self, x, y, color, move_interval=0.5):
        self.x = x
        self.y = y
        self.direction = Directions.STATIC
        self.color = color
        
        self.move_interval = move_interval
        self.base_move_interval = move_interval
        self.lastelapsed = 0
        self.ghost_state = GhostState.CHASE


    # One Discrete Time Step
    def move(self, elapsed, target, wallmap):
        if self.lastelapsed + self.move_interval <= elapsed:

            #if not self.direction in self.get_valid_directions():
            #self.TryTurning()
            #    return
            if self.ghost_state == GhostState.VULNERABLE:
                self.move_interval = self.base_move_interval * 1.5
            else:
                self.move_interval = self.base_move_interval

            moveValue = self.direction.value
            self.x += moveValue[0]
            self.y += moveValue[1]  

            # Ensure PacMan stays within bounds
            self.x %= Wall.xDim # Wrap around horizontally
            self.y %= Wall.yDim # Wrap around vertically

            self.TryTurning(target, wallmap)
            self.lastelapsed += self.move_interval

    def get_valid_directions(self):

        valid_directions = []
        
        if not Wall.checkForWall(self.x,self.y-1):
            valid_directions.append(Directions.UP)
        if not Wall.checkForWall(self.x,self.y+1):
            valid_directions.append(Directions.DOWN)
        if not Wall.checkForWall(self.x-1,self.y):
            valid_directions.append(Directions.LEFT)
        if not Wall.checkForWall(self.x+1,self.y):
            valid_directions.append(Directions.RIGHT)

        return valid_directions
    
    def TryTurning(self, target, wallmap):
        pass
    
def draw_slice(surface, color, center, radius, start_deg, end_deg, steps):
    cx, cy = center
    start_rad = math.radians(start_deg)
    end_rad   = math.radians(end_deg)

    points = [center]
    for i in range(steps + 1):
        t = start_rad + (end_rad - start_rad) * i / steps
        x = cx + radius * math.cos(t)
        y = cy + radius * math.sin(t)
        points.append((x, y))
        

    pygame.draw.polygon(surface, color, points)
    
