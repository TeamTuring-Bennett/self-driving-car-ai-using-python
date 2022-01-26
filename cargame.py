import pygame
import os
import sys

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
        self.player = pygame.draw.rect(self.screen, color=(46,45,45), rect=(self.sloc, (45, 21)))
        self.screen.blit(self.car, self.sloc)
        self.pos_x = self.sloc[0]
        self.pos_y = self.sloc[1]
        vel = 0
        self.isDecel = False
        self.isAccel = False
        self.fw = False
        self.rv = False

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
                if pog.type == pygame.KEYUP:
                    if pog.key == pygame.K_UP:
                        self.isDecel = True
                        self.fw = False
                        self.rv = False
                    elif pog.key == pygame.K_DOWN:
                        self.isAccel = True
                        self.fw = False
                        self.rv = False

            if self.fw:
                vel += 0.6
            elif self.rv:
                vel -= 0.6 

            if self.isAccel and vel < 0:
                vel += 0.1
            elif self.isDecel and vel > 0:
                vel -= 0.1
            self.pos_x += vel
            self.screen.blit(self.map, (0, 0))
            self.player.move(vel, 0)
            self.screen.blit(self.car, (self.pos_x, self.pos_y))
            pygame.display.update()
            self.clock.tick_busy_loop(60)

    def findstartline(self):
        for y in range(720):
            for x in range(1280):
                p = self.screen.get_at([x, y])[:3]
                if p == (245, 210, 31):
                    self.arr = []
                    self.y1 = y
                    for z in range(90):
                        q = self.screen.get_at([x, y+z])[:3]
                        if q == (245, 210, 31):
                            pass
                        else:
                            return [x - 60, y+10+(z/2)]
                

class Car:
    def __init__(self, pox, poy):
        self.ix = pox
        self.iy = poy