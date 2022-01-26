import pygame
import os
import sys
import math

class Race:
    def __init__(self, track, mode):
        self.track = os.path.join('.\\tracks', track)
        self.mode = mode
        self.setup()
        

    def setup(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720), vsync=1)
        self.map = pygame.image.load(self.track).convert()
        self.run = True
        self.screen.blit(self.map, (0, 0))
        self.clock = pygame.time.Clock()

        #car stuff for now make this a class later
        self.car = pygame.image.load('car.png').convert_alpha()
        self.sloc = list(self.findstartline())
        self.screen.blit(self.car, self.sloc)
        self.rotated_sprite = self.car
        self.pos_x = self.sloc[0]
        self.pos_y = self.sloc[1]
        self.center = [int(self.pos_y) + 45 / 2, int(self.pos_y) - 21 / 2]
        self.speed = 0
        self.angle = 0
        self.isDecel = False
        self.isAccel = False
        self.fw = False
        self.rv = False
        self.rt = False
        self.lt = False

        while self.run:    
            for pog in pygame.event.get():
                if pog.type == pygame.QUIT:
                    pygame.quit()
                    self.run = False
                    sys.exit()
                if pog.type == pygame.KEYDOWN:
                    if pog.key == pygame.K_UP:
                        self.fw = True
                        self.rv = False
                        self.isDecel = False
                        self.isAccel = False
                    elif pog.key ==pygame.K_DOWN:
                        self.fw = False
                        self.rv = True
                        self.isDecel = False
                        self.isAccel = False
                    if pog.key == pygame.K_RIGHT:
                        self.rt = True
                        self.lt = False
                    elif pog.key == pygame.K_LEFT:
                        self.lt = True
                        self.rt = False
                if pog.type == pygame.KEYUP:
                    if pog.key == pygame.K_UP:
                        self.isDecel = True
                        self.fw = False
                        self.rv = False
                    elif pog.key == pygame.K_DOWN:
                        self.isAccel = True
                        self.fw = False
                        self.rv = False
                    if pog.key == pygame.K_RIGHT:
                        self.rt = False
                        self.lt = False
                    elif pog.key == pygame.K_LEFT:
                        self.lt = False
                        self.rt = False

            if self.fw:
                self.speed += 0.4
            elif self.rv:
                self.speed -= 0.4
            if self.isAccel and self.speed < 0:
                self.speed += 0.1
            elif self.isDecel and self.speed > 0:
                self.speed -= 0.1
            if self.rt:
                self.angle -= 4
            if self.lt:
                self.angle += 4

            self.update()
            print(self.alive)
            self.screen.blit(self.map, (0, 0))
            self.screen.blit(self.rotated_sprite, (self.pos_x, self.pos_y))
            pygame.display.update()
            self.clock.tick_busy_loop(60)
        
    def update(self):

        self.rotated_sprite = self.rotate_center(self.car, self.angle)
        self.pos_x += math.cos(math.radians(360 - self.angle)) * self.speed
        self.pos_x = max(self.pos_x, 20)
        self.pos_x = min(self.pos_x, 1280)

        #self.distance += self.speed
        #self.time += 1
        
        self.pos_y += math.sin(math.radians(360 - self.angle)) * self.speed
        self.pos_y = max(self.pos_y, 20)
        self.pos_y = min(self.pos_y, 1280 - 120)

        self.center = [int(self.pos_y) + 45 / 2, int(self.pos_y) - 21 / 2]

        #FIX THIS
        length = 0.5 * (((45**2) + (21**2))**0.5)
        left_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 25))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 30))) * length]
        right_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 155))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 150))) * length]
        left_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 215))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 210))) * length]
        right_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 335))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 330))) * length]
        self.corners = [left_top, right_top, left_bottom, right_bottom]

        self.check_collision()
    
    def rotate_center(self, image, angle):
        # Rotate The Rectangle
        rectangle = image.get_rect()
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_rectangle = rectangle.copy()
        rotated_rectangle.center = rotated_image.get_rect().center
        rotated_image = rotated_image.subsurface(rotated_rectangle).copy()
        return rotated_image
    
    def check_collision(self):
        self.alive = True
        for point in self.corners:
            pog = self.map.get_at((int(point[0]), int(point[1])))[:3]
            if pog == (95,204,166):
                self.alive = False
                print(pog)
                break

    def findstartline(self):
        for y in range(720):
            for x in range(1280):
                p = self.screen.get_at([x, y])[:3]
                if p == (245, 210, 31):
                    self.y1 = y
                    for z in range(90):
                        q = self.screen.get_at([x, y+z])[:3]
                        if q != (245, 210, 31):
                            return [x - 60, y-10+(z/2)]
                

class Car:
    def __init__(self, pox, poy):
        self.ix = pox
        self.iy = poy

Race('map02.png', "Manual")