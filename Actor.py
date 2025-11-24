from Directions import Directions
from Wall import Wall


class Actor:



    def __init__(self, x, y, color, move_interval=0.5):
        self.x = x
        self.y = y
        self.direction = Directions.STATIC
        self.color = color
        
        self.move_interval = move_interval
        self.lastelapsed = 0


    # One Discrete Time Step
    def move(self, elapsed, target, wallmap):
        if self.lastelapsed + self.move_interval <= elapsed:

            #if not self.direction in self.get_valid_directions():
            #self.TryTurning()
            #    return

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
    
