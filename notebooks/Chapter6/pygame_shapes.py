# importing pygame
import pygame

# initialize pygame modules
pygame.init()

# define background color (grey)
bgColor = (180, 180, 180)

# define screen settings
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyGame Shape")

# define shape attributes
lineColor = (0, 0, 0)
lineLength = 40
lineThickness = 4

# define end points of the vertical and horizontal lines
screenRect = screen.get_rect() # first we get rect of screen
vertPoints = [(screenRect.centerx - lineLength/2, screenRect.centery),
            (screenRect.centerx + lineLength/2, screenRect.centery)] # vertical endpoints
horPoints = [(screenRect.centerx, screenRect.centery - lineLength/2 ),
            (screenRect.centerx, screenRect.centery + lineLength/2)] # horizontal endpoints

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
    #  draw both crossing lines (hor. and ver. lines)
    pygame.draw.lines(screen, lineColor, False, vertPoints, lineThickness)
    pygame.draw.lines(screen, lineColor, False, horPoints, lineThickness)
    # draw everything to foreground
    pygame.display.flip()
    # wait for 5 seconds then end the program
    pygame.time.wait(5000)
    running = False

# quit program
pygame.quit()
