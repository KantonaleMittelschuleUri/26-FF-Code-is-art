from Directions import Directions
from Ghost import Ghost
from collections import deque
from random import choice

class DirectedGhost(Ghost):

    def __init__(self, x, y, color, move_interval):
        super().__init__(x, y, color, move_interval)
  

    def TryTurning(self, target, wallmap):
        new_direction = self.find_direction_to_pacman(target, wallmap)
        print(new_direction)
        self.direction = new_direction


    def find_direction_to_pacman(self, pacman_pos, wallmap):
        rows, cols = len(wallmap), len(wallmap[0])
        visited = {}
        parent = {}
        q = deque()
        gx, gy = self.x, self.y
        px, py = pacman_pos
        q.append((gx, gy))
        visited[(gx,gy)] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        while len(q) > 0:
            x, y = q.popleft()
            if (x, y) == (px, py):
                print("found pacman")
                break
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and wallmap[ny][nx] == 0 and (nx, ny) not in visited:
                    visited[(nx,ny)] = True
                    parent[(nx, ny)] = (x, y)
                    q.append((nx, ny))


        print(f"Reconstructing Path, parent map:{len(parent)}")
        if (px, py) not in parent:
            print("random")
            return choice([Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT])
        cur = (px, py)
        i = 0
        while parent[cur] != (gx, gy):
            i += 1
            cur = parent[cur]

        print(f"Steps to PacMan: {i+1}")

        cx, cy = cur
        print(f"Next Step: {cx},{cy} from {gx},{gy}, wallmap value: {wallmap[cx][cy]} ")
        if cx == gx - 1 and cy == gy:
            return Directions.LEFT
        elif cx == gx + 1 and cy == gy:
            return Directions.RIGHT
        elif cx == gx and cy == gy - 1:
            return Directions.UP
        elif cx == gx and cy == gy + 1:
            return Directions.DOWN

        return choice([Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT])