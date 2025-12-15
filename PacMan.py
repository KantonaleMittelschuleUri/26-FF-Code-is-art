from Directions import Directions
from Actor import Actor
import pygame
import math


class PacMan(Actor):
    def __init__(self, x, y, counter, interval=0.5):
        super().__init__(x, y, "yellow",interval)

        self.direction = Directions.UP  # Initial direction
        self.nextDirection = Directions.UP
        self.counter = counter % 30

    def TryTurning(self, target, wallmap):
        if self.nextDirection in self.get_valid_directions():
            self.direction = self.nextDirection


    def change_direction(self, new_direction):
        self.nextDirection = new_direction
        #if new_direction in valid_directions:
        #    self.nextDirection = new_direction
    
    def animate(self):
        match self.direction:
            case Directions.UP:
                print("frame_step_animate_up")
            case Directions.DOWN:
                print("frame_step_animate_down")
            case Directions.LEFT:
                print("frame_step_animate_left")
            case Directions.RIGHT:
                print("frame_step_animate_right")

