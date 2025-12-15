# Example file showing a circle moving on screen
import pygame
from PacMan import PacMan
from points import Point, punkte
from Wall import Wall
from Wall import wallmap
from Actor import Actor 
from Ghost import Ghost
from GhostState import GhostState
from DirectedGhost import DirectedGhost
from Directions import Directions
from mode import check_collision, fire_inverted
from concurrent.futures import ThreadPoolExecutor

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
dt = 0


actors = []
player1 = PacMan(6, 12)
actors.append(player1)
actors.append(Ghost(11,13,"red",.5))
actors.append(Ghost(12,13,"pink",.5))
actors.append(DirectedGhost(10,13,"purple",.5))
elapsed = 0

executor = ThreadPoolExecutor(max_workers=2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player1.change_direction(Directions.UP)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player1.change_direction(Directions.DOWN)
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player1.change_direction(Directions.LEFT)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player1.change_direction(Directions.RIGHT)

    # Paint Landscape
    screen.fill("black")
    Wall.paint(screen)

    for p in punkte.values():
        if p.typ == "klein":
            pygame.draw.circle(screen, "white", (p.x * Wall.square_size + Wall.square_size/2, p.y * Wall.square_size + Wall.square_size/2), Wall.square_size/15)
        elif p.typ == "gross":
            pygame.draw.circle(screen, "yellow", (p.x * Wall.square_size + Wall.square_size/2, p.y * Wall.square_size + Wall.square_size/2), Wall.square_size/6)
        else: #kirsche
            pygame.draw.circle(screen, "red", (p.x * Wall.square_size + Wall.square_size/2, p.y * Wall.square_size + Wall.square_size/2), Wall.square_size/4)
        
    
    elapsed += dt

    check_collision(actors)

    for actor in actors:
        actor.move(elapsed, (player1.x, player1.y), wallmap)
        direction = actor.direction.value
    
        if Wall.checkForWall(actor.x + direction[0], actor.y + direction[1]):
            actor.direction = Directions.STATIC
            direction = (0, 0)
            
        if isinstance(actor,PacMan):
            if (player1.x, player1.y) in punkte: # Check for Punkte
                if punkte[(player1.x,player1.y)].typ == "gross":
                    print("Inverted Mode Triggered")
                    executor.submit(fire_inverted, actors)
                del punkte[(player1.x,player1.y)]
            if  player1.direction != Directions.STATIC: #Pacman step frame if not static
                    player1.animate()

        pos = pygame.Vector2(actor.x * Wall.square_size + Wall.square_size/2, actor.y * Wall.square_size + Wall.square_size/2)

        partstep = (elapsed - actor.lastelapsed)/ actor.move_interval
        
        pos += pygame.Vector2(direction[0] * (partstep) * Wall.square_size, direction[1] * (partstep) * Wall.square_size)
        
        if isinstance(actor,Ghost): #Draw Ghost
            rect_g = pygame.Rect(pos.x-Wall.square_size/2.1, pos.y, 2*Wall.square_size/2.1, Wall.square_size/2.1)
            if actor.ghost_state == GhostState.VULNERABLE:
                pygame.draw.circle(screen, "blue", pos, Wall.square_size/2.1)
                pygame.draw.rect(screen, "blue", rect_g)
            elif actor.ghost_state == GhostState.CHASE:
                pygame.draw.circle(screen, actor.color, pos, Wall.square_size/2.1)
                pygame.draw.rect(screen, actor.color, rect_g)
            else:
                pygame.draw.circle(screen, "pink", pos, Wall.square_size/2.1)
                pygame.draw.rect(screen, "pink", rect_g)
        else: #Draw Pacman
            pygame.draw.circle(screen, actor.color, pos, Wall.square_size/2.1)

        

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(30) / 1000

pygame.quit()