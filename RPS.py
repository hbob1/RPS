import random
import pygame

# Sizing Game
Nx = int(9)  # Maximum X pos
Ny = int(9)  # Maximum Y pos
Ngo = int(25)  # How many Game Objects

# Graphic const
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

CIRCLE_RADIUS = 10

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

print(goXpos)
print(goYpos)
print(goType)

# Display Game
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Draw game objects
    for ii, go in enumerate(goType):
        position = (100 * goXpos[ii], 100 * goYpos[ii])
        if goType[ii] == 1:
            color = RED
        elif goType[ii] == 2:
            color = GREEN
        else:
            color = BLUE

        pygame.draw.circle(window, color, position, CIRCLE_RADIUS)
        pygame.display.flip()  # Update the display
    # Test position
    # pygame.draw.circle(window, PCOLOR, (0, 0), CIRCLE_RADIUS)
    # pygame.display.flip()
