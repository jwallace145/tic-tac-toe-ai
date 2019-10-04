# import necessary game modules
import pygame
import game_constants

# initialize pygame
pygame.init()

# initialize screen
screen = pygame.display.set_mode((game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))
pygame.display.set_caption(game_constants.SCREEN_TITLE)

# initialize surface
surface = pygame.Surface(screen.get_size())

# initialize game clock
clock = pygame.time.Clock()

image = pygame.image.load("/Users/jameswallace/Documents/tic-tac-toe/media/spaceship.png")


def spaceship(x, y):
    screen.blit(image, (x, y))


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(game_constants.WHITE)
    spaceship(100, 100 )

    pygame.display.update()
    clock.tick(game_constants.FRAMES_PER_SECOND)
