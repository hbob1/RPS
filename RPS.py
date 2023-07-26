import random
import pygame
import math
import time

# Sizing Game
Nx = int(900)  # Maximum X pos
Ny = int(900)  # Maximum Y pos
Ngo = int(200)  # How many Game Objects

# Graphic const
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0
GREY = 128, 128, 128
WHITE = 255, 255, 255
CIRCLE_RADIUS = 5
COLLISION_THRASHOLD = CIRCLE_RADIUS * 10
VELNX = -7
VELPX = 7
VELNY = -4
VELPY = 4

# Game Objects types
ROCK = 1
SCISSORS = 3
PAPER = 2
DEAD = 10

clock = pygame.time.Clock()

# Initializing the game
goType = Ngo * [0]
goXpos = Ngo * [0]
goYpos = Ngo * [0]

# Variables for Statistics
num_r = 0
num_p = 0
num_s = 0
iter_count = 0

# Initializing display
WIDTH = 1200
HEIGHT = 1000
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mark Segal-----------RSP")

pygame.init()
# populating Game
for ii, go in enumerate(goType):
    goType[ii] = random.randint(ROCK, SCISSORS)
    goXpos[ii] = random.randint(0, Nx)
    goYpos[ii] = random.randint(0, Ny)

# Initiallize old as current
goXpos_old = goXpos.copy()
goYpos_old = goYpos.copy()


# Statistics
def display_statistics(mywin, r, p, s):
    font = pygame.font.Font(None, 30)
    stat1_text = font.render("Rock: {}".format(r), True, RED)
    stat2_text = font.render("Paper: {}".format(p), True, GREEN)
    stat3_text = font.render("Scissors: {}".format(s), True, BLUE)

    pygame.draw.rect(window, BLACK, pygame.Rect(1000, 10, 140, 80))
    pygame.display.update(1000, 10, 140, 80)

    mywin.blit(stat1_text, (1000, 10))
    mywin.blit(stat2_text, (1000, 40))
    mywin.blit(stat3_text, (1000, 70))


# Display Game
while True:
    # time.sleep(0.05)
    clock.tick(120)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw game objects
    for ii, go in enumerate(goType):
        position_old = (1 * goXpos_old[ii], 1 * goYpos_old[ii])
        position = (1 * goXpos[ii], 1 * goYpos[ii])
        if goType[ii] == ROCK:
            color = RED
            num_r = num_r + 1
        elif goType[ii] == PAPER:
            color = GREEN
            num_p = num_p + 1
        elif goType[ii] == SCISSORS:
            color = BLUE
            num_s = num_s + 1
        else:
            color = BLACK

        # erasing circle at old position
        pygame.draw.circle(window, BLACK, position_old, CIRCLE_RADIUS)
        pygame.display.update(
            position_old[0] - CIRCLE_RADIUS,
            position_old[1] - CIRCLE_RADIUS,
            CIRCLE_RADIUS * 2,
            CIRCLE_RADIUS * 2
        )

        # draw circle at new position
        pygame.draw.circle(window, color, position, CIRCLE_RADIUS)
        pygame.display.update(
            position[0] - CIRCLE_RADIUS,
            position[1] - CIRCLE_RADIUS,
            CIRCLE_RADIUS * 2,
            CIRCLE_RADIUS * 2
        )
    # end of loop that draws all circles

    # Displaying Statistics
    iter_count = iter_count + 1
    if iter_count == 5:
        display_statistics(window, num_r, num_p, num_s)
        iter_count = 0

    num_r = 0
    num_p = 0
    num_s = 0

    # Moving objects
    for ii, go in enumerate(goType):
        goXpos_old[ii] = goXpos[ii]
        goXpos[ii] = goXpos[ii] + random.randint(VELNX, VELPX)
        if goXpos[ii] > Nx:
            goXpos[ii] = 0
        if goXpos[ii] < 0:
            goXpos[ii] = Nx

        # Applying for y movement
        goYpos_old[ii] = goYpos[ii]
        goYpos[ii] = goYpos[ii] + random.randint(VELNY, VELPY)
        if goYpos[ii] > Ny:
            goYpos[ii] = 0
        if goYpos[ii] < 0:
            goYpos[ii] = Ny

        for jj, other in enumerate(goType):
            # Computing distance
            dist = math.sqrt((goXpos[jj] - goXpos[ii]) ** 2 + (goYpos[jj] - goYpos[ii]) ** 2)
            # if goXpos[ii] == goXpos[jj] and goYpos[ii] == goYpos[jj]: # Checking exact position
            if dist < COLLISION_THRASHOLD:
                if goType[ii] == ROCK and goType[jj] == PAPER:
                    goType[ii] = PAPER
                    # print("R <- P at " + str(goXpos[ii]) + "," + str(goYpos[ii]))
                if goType[ii] == ROCK and goType[jj] == SCISSORS:
                    goType[jj] = ROCK
                    # print("R -> S at " + str(goXpos[ii]) + "," + str(goYpos[ii]))
                if goType[ii] == SCISSORS and goType[jj] == PAPER:
                    goType[jj] = SCISSORS
                if goType[ii] == SCISSORS and goType[jj] == ROCK:
                    goType[ii] = ROCK
                if goType[ii] == PAPER and goType[jj] == SCISSORS:
                    goType[ii] = SCISSORS
                if goType[ii] == PAPER and goType[jj] == ROCK:
                    goType[jj] = PAPER

    # end of loop that moves and deletes circles

    # Test position
    # pygame.draw.circle(window, PCOLOR, (0, 0), CIRCLE_RADIUS)
    # pygame.display.flip()
