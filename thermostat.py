import pygame

# define a main function
def main():
    temperature = 255
    # initialize the pygame module
    pygame.init()
    clock = pygame.time.Clock()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Thermostat")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((640,480))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        clock.tick(30)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.key.get_pressed()[pygame.K_SPACE] and temperature<250:
            temperature = temperature +5
        screen.fill((temperature,0,255-temperature))
        if(temperature>0):
            temperature = temperature - 1

        pygame.display.flip()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
