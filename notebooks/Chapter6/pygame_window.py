# importing pygame
import pygame

# initialize pygame modules
pygame.init()

# define background color
bgColor = (160, 160, 160)

# define scren Settings
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First PyGame Screen")

# define main loop parameters and start the main loop
FPS = 60 # frames per second (FPS)
clock = pygame.time.Clock() # create pygame clock instance
running = True # boolean value to control main loop

# start mein loop
while running:

    # limiting the while loop to FPS (60 times per second)
    clock.tick(FPS)
    # fill screen
    screen.fill(bgColor)
    # draw everything to foreground
    pygame.display.flip()
    # wait for 5 seconds then end the program
    pygame.time.wait(5000)
    running = False

# quit program
pygame.quit()
