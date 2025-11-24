import random
from Directions import Directions
from Actor import Actor


class Ghost(Actor):
    def __init__(self,x,y,color, move_interval):
        super().__init__(x, y, color, move_interval)
        self.direction = random.choice(self.get_valid_directions())
        
    def TryTurning(self, target, wallmap):
        self.direction = random.choice(self.get_valid_directions())



    

    
