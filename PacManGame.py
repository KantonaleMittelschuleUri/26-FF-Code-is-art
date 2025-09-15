# Example file showing a circle moving on screen
import pygame
from PacMan import PacMan
from points import Point, punkte

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player1 = PacMan(5, 5)
elapsed = 0


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player1.change_direction('UP')
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player1.change_direction('DOWN')
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player1.change_direction('LEFT')
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player1.change_direction('RIGHT')

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    for p in punkte.values():
        pygame.draw.circle(screen, "yellow", (p.x * 31 + 15, p.y * 31 + 15), 2)
        

    elapsed += dt

    x = 0
    y = 0
    if player1.direction == "UP":
        y = -1.0
    if player1.direction == "DOWN":
        y = 1.0
    if player1.direction == "LEFT":
        x = -1.0
    if player1.direction == "RIGHT":
        x = 1.0

    player_pos = pygame.Vector2(player1.x * 31 + 15, player1.y * 31 + 15)
    if elapsed > 0.5:
        elapsed -= 0.5
        player1.move()
        if (player1.x, player1.y) in punkte:
            del punkte[(player1.x,player1.y)]
        player_pos = pygame.Vector2(player1.x * 31 + 15, player1.y * 31 + 15)

    player_pos += pygame.Vector2(x * (elapsed / 0.5) * 31, y * (elapsed / 0.5) * 31)



    
    print(elapsed)
    pygame.draw.circle(screen, "red", player_pos, 14)




    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(30) / 1000

pygame.quit()