from Directions import Directions
from Actor import Actor


class PacMan(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, color="yellow")

        self.direction = Directions.UP  # Initial direction
        self.nextDirection = Directions.UP

    def TryTurning(self):
        if self.nextDirection in self.get_valid_directions():
            self.direction = self.nextDirection


    def change_direction(self, new_direction):
        self.nextDirection = new_direction
        #if new_direction in valid_directions:
        #    self.nextDirection = new_direction

