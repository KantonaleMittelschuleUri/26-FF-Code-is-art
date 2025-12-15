from Directions import Directions
from Ghost import Ghost
from GhostState import GhostState


class DirectedGhost(Ghost):

    def __init__(self, x, y, color, move_interval):
        super().__init__(x, y, color, move_interval)
  

    def TryTurning(self, target, wallmap):
        if self.ghost_state == GhostState.CHASE:
            self.direction = self.find_direction_to_position(target, wallmap)
        else:
            super().TryTurning(target, wallmap)



    