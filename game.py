import tkinter

import pygame
import random
from background_cars import BackgroundCars
from car import Car
from star import Star
from track import Track
import pyautogui


class Game:
    def start_game(self):
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((1281, 720))
        clock = pygame.time.Clock()
        font = pygame.font.SysFont('Comic Sans MS', 20)
        running = True
        dt = 0

        player = Car(screen)
        star = Star()
        road = []
        cars = []
        lanes = []
        score = 0
        with open("high_score.txt") as file:
            high_score = int(file.read())
        score_incrementer_cooldown = 50
        time_passed = 0

        for i in range(2):
            if len(road) == 0:
                road.append(Track(0))
            else:
                road.append(Track(road[len(road) - 1].pos.y - 720))

        for i in range(3):
            r = random.randint(0, 8)
            while r in lanes:
                r = random.randint(0, 8)
            lanes.append(r)

        for emp in range(len(lanes)):
            cars.append(BackgroundCars(-700, screen, lanes[emp], []))

        lanes.clear()

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("green")

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move_left(dt)
            if keys[pygame.K_RIGHT]:
                player.move_right(dt)

            for t in road:
                t.advance(dt)

            for t in road:
                if t.pos.y > 720:
                    road.remove(t)
                    road.append(Track(road[len(road) - 1].pos.y - 720))

            for t in road:
                screen.blit(t.image, t.pos)

            star.cooldown_manage()
            if star.check_car_collision(player.pos):
                score += 10

            star.advance(dt)
            screen.blit(star.image, star.pos)

            if score_incrementer_cooldown != 0:
                score_incrementer_cooldown -= 1
            else:
                score += 1
                score_incrementer_cooldown = 50

            screen.blit(font.render(f"High Score = {high_score}", False, (0, 0, 0)), (1100, 20))
            screen.blit(font.render(f"Score = {score}", False, (0, 0, 0)), (1120, 60))

            posY = []
            for car in cars:
                lanes.append(car.pos.x)
                posY.append(car.pos.y)

            notApp = 0  # cars not appearing on screen

            for i in range(len(posY)):
                if posY[i] < -100 or posY[i] > 800:
                    notApp += 1
            if notApp > int(len(cars) / 2):
                for car in cars:
                    i = 0
                    if car.pos.y < -200 or car.pos.y > 1000:
                        car.pos.y = -130 - i * 20
                    i += 1
            if time_passed % 1000 == 0 and time_passed > 0 and len(cars) < 9:
                cars.append(BackgroundCars(-300, screen, emp, lanes))

            for car in cars:
                car.update_position(dt, lanes)
                car.screen.blit(car.image, car.pos)

            for car in cars:
                if player.check_traffic_collision(car.pos):
                    if score > high_score:
                        high_score = score
                        with open("high_score.txt", mode="w") as file:
                            file.write(f"{score}")
                        pyautogui.alert(text="          Game\n          Over\n          New High score !!!")

                    else:
                        pyautogui.alert(text="          Game\n          Over")

                    running = False

            screen.blit(player.image, player.pos)
            pygame.display.update()
            time_passed += 1
            lanes.clear()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate -
            # independent physics.
            dt = clock.tick(60) / 1000

        pygame.quit()
