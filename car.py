import pygame


class Car:
    def __init__(self, screen):
        self.image = pygame.image.load('gif_files/Car_3_01.gif').convert()
        self.pos = pygame.Vector2(screen.get_width() / 2 - 50, 560)

    def move_left(self, dt):
        if self.pos.x > 235:
            self.pos.x -= 800 * dt

    def move_right(self, dt):
        if self.pos.x < 950:
            self.pos.x += 800 * dt

    def check_traffic_collision(self, traffic_car_pos):
        if (traffic_car_pos.y + 160 >= self.pos.y and traffic_car_pos.y < 700) and (abs(self.pos.x - traffic_car_pos.x) < 70):
            return True
