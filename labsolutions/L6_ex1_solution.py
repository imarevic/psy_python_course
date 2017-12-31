# importing pygame
import pygame

# initialize pygame modules
pygame.init()

# define background color
bgOrange = (255, 165, 0)
bgBlue = (0, 0, 205)

# define scren Settings
size = (400, 400)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

# define main loop parameters and start the main loop
FPS = 60 # frames per second (FPS)
clock = pygame.time.Clock() # create pygame clock instance
running = True # boolean value to control main loop

# start main loop
while running:

    # limiting the while loop to FPS (60 times per second)
    clock.tick(FPS)
    # fill screen with orange
    screen.fill(bgOrange)
    # draw everything to foreground for 3 seconds
    pygame.display.flip()
    pygame.time.wait(3000)
    # change screen color to blue
    screen.fill(bgBlue)
    #draw everything again
    pygame.display.flip()
    # wait for another 4.5 seconds then end the program
    pygame.time.wait(4500)
    # program ran for 7.5 seconds in total, so now let's exit
    running = False

# quit program
pygame.quit()
