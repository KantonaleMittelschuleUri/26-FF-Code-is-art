from Wall import Wall

xDim = 23
yDim = 23


class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 'UP'  # Initial direction
        self.nextDirection = 'UP'

    # One Discrete Time Step
    def move(self):
        #if not self.direction in self.get_valid_directions():
        self.TryTurning()
        #    return

        if self.direction == 'UP':
            self.y -= 1
        elif self.direction == 'DOWN':
            self.y += 1
        elif self.direction == 'LEFT':
            self.x -= 1
        elif self.direction == 'RIGHT':
            self.x += 1

        # Ensure PacMan stays within bounds
        self.x %= xDim # Wrap around horizontally
        self.y %= yDim # Wrap around vertically

        self.TryTurning()

    def TryTurning(self):
        if self.nextDirection in self.get_valid_directions():
            self.direction = self.nextDirection


    def change_direction(self, new_direction):
        self.nextDirection = new_direction
        #if new_direction in valid_directions:
        #    self.nextDirection = new_direction

    def get_valid_directions(self):

        valid_directions = []
        
        if not Wall.checkForWall(self.x,self.y-1):
            valid_directions.append('UP')
        if not Wall.checkForWall(self.x,self.y+1):
            valid_directions.append('DOWN')
        if not Wall.checkForWall(self.x-1,self.y):
            valid_directions.append('LEFT')
        if not Wall.checkForWall(self.x+1,self.y):
            valid_directions.append('RIGHT')

        return valid_directions