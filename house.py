import pygame
import random

class House:
    def __init__(self,inx,iny):
        self.temperature = random.randint(0,255)
        self._w = 80
        self._h = 80
        self._surface = pygame.Surface((self._w,self._h))
        self._insulation = random.randint(8,11) #houses cool down at different rates
        self.x = inx-(self._w/2)
        self.y = iny-(self._h/2)

    def update(self):
        if(self.temperature>0):
            if(pygame.time.get_ticks() % self._insulation == 0):
                self.temperature = self.temperature - 1

    def draw(self,display):
        self._surface.fill((self.temperature,0,255-self.temperature))
        display.blit(self._surface,(self.x,self.y))


    def warmup(self):
        self.temperature = self.temperature + 5
        if(self.temperature>255):
            self.temperature = 255
