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

        #car stuff for now make this a class later
        self.car = pygame.image.load('car.png').convert_alpha()
        self.sloc = list(self.findstartline())
        self.screen.blit(self.car, self.sloc)
        #self.player = pygame.draw.rect(self.car, color=(0, 0, 0, 0))

        while self.run:    
            for pog in pygame.event.get():
                if pog.type == pygame.QUIT:
                    pygame.quit()
                    self.run = False
                    sys.exit()
            pygame.display.update()

    def findstartline(self):
        for y in range(720):
            for x in range(1280):
                p = self.screen.get_at([x, y])[:3]
                if p == (245, 210, 31):
                    return [x - 60, y + 15]
                    break
                

Race('map01.png', "AI")