from enum import Enum

class GhostState(Enum):
    CHASE = 1
    VULNERABLE = 2
    EATEN = 3