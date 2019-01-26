import pygame
from house import *
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        self.temperature = 255
        self.clock = None
        self.houses = None
        self.active_house = None

    def on_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        wx = self.width/5
        hx = self.height/3
        self.houses = [House(wx*1,hx*1),House(wx*2,hx*1),House(wx*3,hx*1),House(wx*4,hx*1),House(wx*1,hx*2),House(wx*2,hx*2),House(wx*3,hx*2),House(wx*4,hx*2)]
        self.active_house = self.houses[0]

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
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
        for h in self.houses:
            h.update()
        #self.house.update()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.active_house.warmup()
        #    self.temperature = self.temperature +5
        #if(self.temperature>0):
        #        self.temperature = self.temperature - 1
        pass
    def on_render(self):
        self._display_surf.fill((200,200,255))
        for h in self.houses:
            h.draw(self._display_surf)
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
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
