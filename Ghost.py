import random
import pygame

xDim = 23
yDim = 23
cell_size = 31

class Ghost:
    def __init__(self,x,y,direction,color):
        self.x = x
        self.y = y
        self.color = color
        self.direction = random.choice(['UP','DOWN','LEFT','RIGHT'])
        
    def move(self):
        if self.direction == 'UP':
            self.y -= 1
        elif self.direction == 'DOWN':
            self.y += 1
        elif self.direction == 'LEFT':
            self.x -= 1
        elif self.direction == 'RIGHT':
            self.x += 1
            
        self.direction = random.choice(['UP','DOWN','LEFT','RIGHT'])
        print(self)
        self.x %= xDim
        self.y %= yDim
    
    def get_valid_directions():
        return ['UP','DOWN','LEFT','RIGHT']
    
