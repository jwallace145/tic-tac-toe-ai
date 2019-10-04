import pygame

pygame.init()

class XPlayer(pygame.sprite.Sprite):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.width = 300
        self.height = 300
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.screen_height = pygame.display.get_surface().get_height()
        self.screen_width = pygame.display.get_surface().get_width()
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def display(self, screen):
        screen.blit()