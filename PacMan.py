

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
        if not self.direction in self.get_valid_directions():
            self.TryTurning()
            return

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
        valid_directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        if new_direction in valid_directions:
            self.nextDirection = new_direction