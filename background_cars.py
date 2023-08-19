import pygame
import random


class BackgroundCars:
    def __init__(self, y, screen, i, lanes):
        self.width = 80
        self.height = 162
        self.image = pygame.image.load('gif_files/Car_1_01.gif').convert()
        self.lanes = [210, 315, 410, 505, 600, 700, 790, 870, 975]
        if len(lanes) > 0:
            while self.lanes[i] in lanes:
                i += 1
                i %= len(self.lanes)

        self.pos = pygame.Vector2(self.lanes[i], y)
        self.screen = screen
        self.randomSpeed = [200, 300, 250, 150, 350, 400, 420]
        self.randomApp = random.choice([900, 1200, 2000, 1700, 1500, 1400, 800])
        self.mySpeed = random.choice(self.randomSpeed)

    def update_position(self, dt, lanes):
        self.pos.y += dt * self.mySpeed
        if self.pos.y > self.randomApp:
            self.mySpeed = random.choice(self.randomSpeed)
            self.pos.y = -300
            self.randomApp = random.choice([900, 1200, 1400, 800])
            r = random.choice([210, 315, 410, 505, 600, 700, 790, 870, 975])
            if r not in lanes:
                self.pos.x = r
