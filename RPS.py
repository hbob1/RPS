import random
import pygame
import time

# Sizing Game
Nx = int(900)  # Maximum X pos
Ny = int(900)  # Maximum Y pos
Ngo = int(100)  # How many Game Objects

# Graphic const
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0
GREY = 128, 128, 128
CIRCLE_RADIUS = 5


# Initializing the game
goType = Ngo * [0]
goXpos = Ngo * [0]
goYpos = Ngo * [0]


# Initializing display
WIDTH = 1000
HEIGHT = 1000
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mark Segal-----------RSP")

# populating Game
for ii, go in enumerate(goType):
    goType[ii] = random.randint(1, 3)
    goXpos[ii] = random.randint(0, Nx)
    goYpos[ii] = random.randint(0, Ny)

# Initiallize old as current
goXpos_old = goXpos.copy()
goYpos_old = goYpos.copy()


print(goXpos)
print(goYpos)
print(goType)

# Display Game
while True:
    time.sleep(0.05)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()




    # Draw game objects
    for ii, go in enumerate(goType):
        position_old = (1 * goXpos_old[ii], 1 * goYpos_old[ii])
        position = (1 * goXpos[ii], 1 * goYpos[ii])
        if goType[ii] == 1:
            color = RED
        elif goType[ii] == 2:
            color = GREEN
        else:
            color = BLUE

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



    # Moving objects
    for ii, go in enumerate(goType):
        goXpos_old[ii] = goXpos[ii]
        goXpos[ii] = goXpos[ii] + random.randint(-1, 3)
        if goXpos[ii] > Nx:
            goXpos[ii] = 0
        if goXpos[ii] < 0:
            goXpos[ii] = Nx


    # Test position
    # pygame.draw.circle(window, PCOLOR, (0, 0), CIRCLE_RADIUS)
    # pygame.display.flip()
