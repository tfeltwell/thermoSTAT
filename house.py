import pygame
import random
from markers import *

class House:
    def __init__(self,inx,iny):
        self.temperature = random.randint(0,255)
        self.desired_temperature = random.randint(0,255)
        self.w = 165
        self.h = 142
        self._surface = pygame.Surface((self.w,self.h))
        self._insulation = random.randint(8,11) #houses cool down at different rates
        self.x = inx-(self.w/2)
        self.y = iny-(self.h/2)
        #self._surface.set_alpha(180)
        self.next_change = random.randint(500,2000)
        self.channel2 = pygame.mixer.Channel(1)
        self.bing = pygame.mixer.Sound("bing.wav")
        self.bing.set_volume(0.2)

    def update(self,hits):
        if(self.temperature>0):
            if(pygame.time.get_ticks() % self._insulation == 0):
                self.temperature = self.temperature - 1
        #randomly set a new desired_temperature
        if(self.next_change == 0):
            self.desired_temperature = random.randint(0,255)
            hits.spawn_warning(self.x+(self.w/2),self.y+(self.h/2))
            self.next_change = random.randint(550,900)
            if not self.channel2.get_busy():
                self.channel2.play(self.bing)
	else:
	    self.next_change = self.next_change -1

    def draw(self,display):
        self._surface.fill((self.temperature,0,255-self.temperature))
        pygame.draw.rect(self._surface,(self.desired_temperature,0,255-self.desired_temperature),(2,2,self.w/4,self.h/4),0)
        display.blit(self._surface,(self.x,self.y))

    def warmup(self):
        self.temperature = self.temperature + 5
        if(self.temperature>255):
            self.temperature = 255

    def get_accuracy(self):
        return (self.temperature - self.desired_temperature)
