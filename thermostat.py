import pygame
from house import *
from car import *
from pygame.locals import *
from markers import *
import RPi.GPIO as GPIO

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 1280, 720
        self.temperature = 255
        self.clock = None
        self.houses = None
        self.active_house = None
        self.score = 0
        self._score_font = None
        self._hits = None
        self.house_image = None
        self._cars = None


    def on_init(self):
        pygame.init()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

        self.clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode(self.size, pygame.FULLSCREEN)#pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        wx = self.width/5
        hx = self.height/3
        #self.houses = [House(wx*1,hx*1),House(wx*2,hx*1),House(wx*3,hx*1),House(wx*4,hx*1),House(wx*1,hx*2),House(wx*2,hx*2),House(wx*3,hx*2),House(wx*4,hx*2)]
        self.houses = [House(272,88),House(572,88),House(848,88),House(1146,85), House(260,643),House(559,641),House(837,642),House(1134,640)]

        self.active_house = self.houses[0]
        self._score_font = pygame.font.Font("beon.ttf",42)
        self._hits = Hits()
        self._cars = Cars()
        self.house_image = pygame.transform.scale(pygame.image.load("house.png").convert(),(1280,720))
        self.house_image.set_colorkey((255,0,255))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.key == pygame.K_1:
                self.active_house=self.houses[0]
            elif event.key == pygame.K_2:
                self.active_house=self.houses[1]
            elif event.key == pygame.K_3:
                self.active_house=self.houses[2]
            elif event.key == pygame.K_4:
                self.active_house=self.houses[3]
            elif event.key == pygame.K_5:
                self.active_house=self.houses[4]
            elif event.key == pygame.K_6:
                self.active_house=self.houses[5]
            elif event.key == pygame.K_7:
                self.active_house=self.houses[6]
            elif event.key == pygame.K_8:
                self.active_house=self.houses[7]
    def on_loop(self):
        self._hits.update()
        self._cars.update()
        for h in self.houses:
            h.update(self._hits)
        #self.house.update()

        #if pygame.key.get_pressed()[pygame.K_SPACE]:
        if GPIO.input(18)==GPIO.HIGH:
            self.active_house.warmup()
        if(pygame.time.get_ticks() % 20 == 0):
            for h in self.houses:
                if(abs(h.get_accuracy())<20):
                    self.score=self.score+1
                    self._hits.spawn(h.x+(h.w/2),h.y+(h.h/2))
                elif(abs(h.get_accuracy()>100)):
                    self.score=self.score-1
                    self._hits.spawn_bad(h.x+(h.w/2),h.y+(h.h/2))
        pass
    def on_render(self):
        self._display_surf.fill((200,200,255))
        for h in self.houses:
            h.draw(self._display_surf)
        self._display_surf.blit(self.house_image,(0,0))
        self._cars.draw(self._display_surf)
        self._hits.draw(self._display_surf)

        self._display_surf.blit(self._score_font.render('$%.3f' % (float(self.score)/3000),True,(0,0,0)),(0,0))
        pygame.display.flip()
        pass
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            #self.clock.tick(50)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
