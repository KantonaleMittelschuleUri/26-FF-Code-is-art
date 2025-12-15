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

