import pygame


class Hits:
    def __init__(self):
        self._hits =[]
        self.thumb = pygame.transform.scale(pygame.image.load("thumb-up.png").convert(),(50,50))
        self.thumb.set_colorkey((0,0,0))

    def update(self):
        for h in self._hits:
            if(not h.update()):
                self._hits.remove(h)
    def draw(self,display):
        for h in self._hits:
            h.draw(display)
    def spawn(self,x,y):
        self._hits.append(Hit(x,y,self.thumb))


class Hit:
    def __init__(self,x,y,img):
        self._coord = (x,y)
        self._img = img
        self._ticks = 30
        return
    def update(self):
        self._ticks = self._ticks - 1
        if self._ticks < 0:
            return False
        self._coord = (self._coord[0],self._coord[1]-5)
        return True
    def draw(self,display):

        self._img.set_alpha(self._ticks*9)
        display.blit(self._img,self._coord)
        return
