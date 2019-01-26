import pygame
import random
class Cars:
    def __init__(self):
        self.car_image = pygame.image.load("car.png")
        self.cars = []
        self._last_car = 0
        return
    def update(self):
        for c in self.cars:
            c.update()
            if (c.right and c.coord[0]>1300) or ((not c.right) and c.coord[0]<-100):
                self.cars.remove(c)
        if(pygame.time.get_ticks()>self._last_car):
            if random.randint(0,2)==0:
                self.cars.append(Car(self.car_image,(-100,370),True))
            else:
                self.cars.append(Car(self.car_image,(1300,318),False))
            self._last_car = pygame.time.get_ticks() + 1000 + random.randint(0,8000)
        #make new car?
        return
    def draw(self,display):
        for c in self.cars:
            c.draw(display)
        return

class Car:
    def __init__(self,img,coord,right):
        self._img = img
        self.coord = coord
        self.right = right # travelling to the right?
        self.speed = random.randint(6,10)

        return
    def update(self):
        if self.right:
            self.coord = (self.coord[0]+self.speed,self.coord[1])
        else:
            self.coord = (self.coord[0]-self.speed,self.coord[1])
        return
    def draw(self,display):
        if(self.right):
            display.blit(pygame.transform.flip(self._img,True,False),self.coord)
        else:
            display.blit(self._img,self.coord)
        return
