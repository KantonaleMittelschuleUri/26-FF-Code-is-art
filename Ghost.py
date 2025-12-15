import random
from Directions import Directions
from Actor import Actor
from collections import deque
from random import choice

from GhostState import GhostState


class Ghost(Actor):
    def __init__(self,x,y,color, move_interval):
        super().__init__(x, y, color, move_interval)
        self.direction = random.choice(self.get_valid_directions())
        self.initial_x = x
        self.initial_y = y
        
    def TryTurning(self, target, wallmap):
        if self.ghost_state == GhostState.EATEN:
            if self.x == self.initial_x and self.y == self.initial_y:
                self.ghost_state = GhostState.CHASE
            self.direction = self.find_direction_to_position((self.initial_x, self.initial_y), wallmap)
        else:
            self.direction = random.choice(self.get_valid_directions())



    def find_direction_to_position(self, pos, wallmap):
        rows, cols = len(wallmap), len(wallmap[0])
        visited = {}
        parent = {}
        q = deque()
        gx, gy = self.x, self.y
        px, py = pos
        q.append((gx, gy))
        visited[(gx,gy)] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        while len(q) > 0:
            x, y = q.popleft()
            if (x, y) == (px, py):
                break
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and wallmap[ny][nx] == 0 and (nx, ny) not in visited:
                    visited[(nx,ny)] = True
                    parent[(nx, ny)] = (x, y)
                    q.append((nx, ny))

        cur = (px, py)
        i = 0
        try:
            while parent[cur] != (gx, gy):
                i += 1
                cur = parent[cur]

            cx, cy = cur
            if cx == gx - 1 and cy == gy:
                return Directions.LEFT
            elif cx == gx + 1 and cy == gy:
                return Directions.RIGHT
            elif cx == gx and cy == gy - 1:
                return Directions.UP
            elif cx == gx and cy == gy + 1:
                return Directions.DOWN
        except KeyError:
            return choice([Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT])



    

    
