import pygame
import random


class Star:
    def __init__(self):
        self.image = pygame.image.load('gif_files/Star_Gold.gif').convert()
        self.pos = pygame.Vector2(-200, -200)
        self.cooldown = 200
        self.visible = False

    def cooldown_manage(self):
        if self.cooldown != 0:
            self.cooldown -= 1
        else:
            self.reset()

    def advance(self, dt):
        self.pos.y += 500 * dt

    def reset(self):
        lanes = [238, 330, 418, 510, 600, 688, 780, 867, 960]

        self.pos.x = random.choice(lanes)
        self.pos.y = -800
        self.cooldown = 200

    def check_car_collision(self, car_pos):
        if self.pos.y >= car_pos.y - 60 and (car_pos.x + 80 > self.pos.x > car_pos.x or car_pos.x + 80 > self.pos.x + 60 > car_pos.x):
            self.reset()
            return True
