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
shapeColor = (250, 0, 0)
shapeWidth = 100
shapeHeight = 100

# positioning
# get screen rect and place shape at center
screenRect = screen.get_rect()
shapeRect = pygame.Rect(screenRect.centerx - shapeWidth/2, screenRect.centery - shapeHeight/2,
                        shapeWidth, shapeHeight)

# define main loop parameters and start the main loop
FPS = 60 # frames per second (FPS)
clock = pygame.time.Clock() # create pygame clock instance
running = True # boolean value to control main loop

# start main loop
while running:
    # check for events
    for event in pygame.event.get():
        # if quit button pressed exit the loop
        if event.type == pygame.QUIT:
            running = False
    # limiting the while loop to FPS (60 times per second)
    clock.tick(FPS)
    # fill screen
    screen.fill(bgColor)
    #  draw the shape
    pygame.draw.rect(screen, shapeColor, shapeRect)
    # draw everything to foreground
    pygame.display.flip()

# quit pygame
pygame.quit()
