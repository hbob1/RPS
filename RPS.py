import random
import pygame

# Sizing Game
Nx = int(9)
Ny = int(9)
Ngo = int(5)

# Graphic const
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

RCOLOR = RED
PCOLOR = GREEN
SCOLOR = BLUE
CIRCLE_RADIUS = 10

# Initializing the game
goType = Ngo * [None]
goXpos = Ngo * [None]
goYpos = Ngo * [None]


# Initializing display
WIDTH = 1000
HEIGHT = 1000
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mark Segal-----------RSP")

# populating Game
for ii, go in enumerate(goType):
    goType[ii] = 'R'
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
        pygame.draw.circle(window, RCOLOR, position, CIRCLE_RADIUS)
        pygame.display.flip()  # Update the display
    # Test position
    # pygame.draw.circle(window, PCOLOR, (0, 0), CIRCLE_RADIUS)
    # pygame.display.flip()