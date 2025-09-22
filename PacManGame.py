# Example file showing a circle moving on screen
import pygame
from PacMan import PacMan
from points import Point, punkte
from Wall import Wall
from Ghost import Ghost

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player1 = PacMan(0, 22)
ghost1 = Ghost(12,12,"UP","red")
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

    # Paint Landscape
    screen.fill("black")
    Wall.paint(screen)

    for p in punkte.values():
        pygame.draw.circle(screen, "orange", (p.x * 31 + 15, p.y * 31 + 15), 2)
        
    
    elapsed += dt

    x = 0
    y = 0
    xg = 0
    yg = 0

    #Determine offset for player movement
    if player1.direction == "UP":
        y = -1.0
    if player1.direction == "DOWN":
        y = 1.0
    if player1.direction == "LEFT":
        x = -1.0
    if player1.direction == "RIGHT":
        x = 1.0
    #ghost pos
    if ghost1.direction == "UP":
        yg = -1.0
    if ghost1.direction == "DOWN":
        yg = 1.0
    if ghost1.direction == "LEFT":
        xg = -1.0
    if ghost1.direction == "RIGHT":
        xg = 1.0


    #print("[DEBUG] p1_x: ", player1.x)
    #print("[DEBUG] p1_y: ", player1.y)
    #print("[DEBUG] p1_direction: ", player1.direction)
    #print("[DEBUG] Valid Direction: ", player1.get_valid_directions())
    #print("x", x)
    #print("x", y)
    if Wall.checkForWall(player1.x + int(x), player1.y + int(y)):
        player1.direction = "STATIC"
        
    if Wall.checkForWall(ghost1.x + int(x), ghost1.y + int(y)):
        ghost1.direction = "STATIC"
    
    #Paint
    ghost1_pos = pygame.Vector2(ghost1.x * 31 + 15, ghost1.y * 31 + 15)
    player_pos = pygame.Vector2(player1.x * 31 + 15, player1.y * 31 + 15)
    if elapsed > 0.5:
        elapsed -= 0.5

        

        player1.move()
        if (player1.x, player1.y) in punkte:
            del punkte[(player1.x,player1.y)]
        player_pos = pygame.Vector2(player1.x * 31 + 15, player1.y * 31 + 15)
        
        ghost1.move()
        ghost1_pos = pygame.Vector2(ghost1.x * 31 + 15, ghost1.y * 31 + 15)

    player_pos += pygame.Vector2(x * (elapsed / 0.5) * 31, y * (elapsed / 0.5) * 31)
    ghost1_pos += pygame.Vector2(xg * (elapsed / 0.5) * 31, yg * (elapsed / 0.5) * 31)



    
    #print(elapsed)
    pygame.draw.circle(screen, "yellow", player_pos, 14)
    
    pygame.draw.circle(screen, "red", ghost1_pos, 14)




    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(30) / 1000

pygame.quit()
