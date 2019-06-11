# importing pygame
import pygame

# initialize pygame modules
pygame.init()

# define background color (grey)
bgColor = (180, 180, 180)

# define scren Settings
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyGame Shape")

# define shape attributes
shapeColor = (0, 0, 250)
pointlist = [(100, 200), (200, 100), (300, 200)]

# define main loop parameters and start the main loop
FPS = 60 # frames per second (FPS)
clock = pygame.time.Clock() # create pygame clock instance
running = True # boolean value to control main loop

# start main loop
while running:

    # limiting the while loop to FPS (60 times per second)
    clock.tick(FPS)
    # fill screen
    screen.fill(bgColor)
    #  draw the shape
    pygame.draw.polygon(screen, shapeColor, pointlist)
    # draw everything to foreground
    pygame.display.flip()
    # wait for 5 seconds then end the program
    pygame.time.wait(5000)
    running = False

# quit program
pygame.quit()
