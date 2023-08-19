import pygame


class Track:
    def __init__(self, y):
        self.image = pygame.image.load('gif_files/ourBackground_updated.gif').convert()
        self.pos = pygame.Vector2(0, y)

    def advance(self, dt):
        self.pos.y += 500 * dt
