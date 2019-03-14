import pygame
from house import *
from car import *
from pygame.locals import *
from markers import *
# import RPi.GPIO as GPIO

class App:
    def __init__(self):
        self._running = False
        self._display_surf = None
        self.size = self.width, self.height = 1280, 720
        self.splash_on = True
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
        # REENABLE THESE FOR RPi VERSION
        # GPIO.setwarnings(False)
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

        pygame.mixer.music.load("background.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.channel1 = pygame.mixer.Channel(0)
        self.boiler = pygame.mixer.Sound("boiler.wav")


        self.clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode(self.size,pygame.FULLSCREEN)# pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        wx = self.width/5
        hx = self.height/3
        #self.houses = [House(wx*1,hx*1),House(wx*2,hx*1),House(wx*3,hx*1),House(wx*4,hx*1),House(wx*1,hx*2),House(wx*2,hx*2),House(wx*3,hx*2),House(wx*4,hx*2)]
        self.houses = [House(255,92),House(559,90),House(842,91),House(1146,88), House(245,641),House(547,640),House(832,639),House(1135,638)]

        self.active_house = self.houses[0]
        self._score_font = pygame.font.Font("beon.ttf",42)
        self._hits = Hits()
        self._cars = Cars()
        self.house_image = pygame.transform.scale(pygame.image.load("house.png").convert(),(1280,720))
        self.house_image.set_colorkey((255,0,255))

        # splash screen
        self.splash_image = pygame.transform.scale(pygame.image.load("assets/splash.png").convert(),(1280,720))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.key == pygame.K_1:
                self.active_house=self.houses[0]
            elif event.key == pygame.K_2:
                self.active_house=self.houses[4]
            elif event.key == pygame.K_3:
                self.active_house=self.houses[1]
            elif event.key == pygame.K_4:
                self.active_house=self.houses[5]
            elif event.key == pygame.K_5:
                self.active_house=self.houses[2]
            elif event.key == pygame.K_6:
                self.active_house=self.houses[6]
            elif event.key == pygame.K_7:
                self.active_house=self.houses[3]
            elif event.key == pygame.K_8:
                self.active_house=self.houses[7]

    def on_loop(self):
        if self.splash_on:
            if self.button_pressed():
                self.splash_on = False
                self._running = True

        if self._running:
            self._hits.update()
            self._cars.update()
            for h in self.houses:
                h.update(self._hits)

            if self.button_pressed():
                self.active_house.warmup()
                if not self.channel1.get_busy():
                    self.channel1.play(self.boiler)
            else:
                if self.channel1.get_busy():
                    self.channel1.fadeout(500)
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
        if self.splash_on:
            self._display_surf.blit(self.splash_image, (0,0))
            pygame.display.flip()
        else:
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
            self.clock.tick(30)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def button_pressed(self):
        # UNCOMMENT FOR RPi VERSION
        # if GPIO.input(18)==GPIO.HIGH:
        #     return True
        # else: 
        #     return False

        return pygame.key.get_pressed()[pygame.K_SPACE]

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
