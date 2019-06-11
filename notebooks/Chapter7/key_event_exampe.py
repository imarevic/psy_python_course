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
radius = 60

# positioning
# get screen rect and place shape at center
screenRect = screen.get_rect()
shapeRect = pygame.Rect(screenRect.centerx - shapeWidth/2, screenRect.centery - shapeHeight/2,
                        shapeWidth, shapeHeight)
# get x and y coordinates for circle
xPos = screenRect.centerx
yPos = screenRect.centery

# stimulus list
stimuli = ["square", "circle", "square", "circle", "square"]

# results dictionary
results = {"responses" : []}

# start loop over stimuli
for stimulus in stimuli:
    # if stimulus is square, present squares and handle events
    if stimulus == "square":
        # present until one of the 2 keys (f=sqaure vs. j=circle) is pressed
        response = ""
        while response != "circle" and response != "square":
            # check for events
            for event in pygame.event.get():
                # if quit button pressed exit the loop
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                # respond to a keypress
                    if event.key == pygame.K_f:
                        response = "square"
                    elif event.key == pygame.K_j:
                        response = "circle"
            # fill screen
            screen.fill(bgColor)
            #  draw the square
            pygame.draw.rect(screen, shapeColor, shapeRect)
            # draw everything to foreground
            pygame.display.flip()

        # append response to results list
        results["responses"].append(response)

    # if stimulus is circle, present circles and handle events
    elif stimulus == "circle":
        # present until one of the 2 keys (f=sqaure vs. j=circle) is pressed
        response = ""
        while response != "circle" and response != "square":
            # check for events
            for event in pygame.event.get():
                # if quit button pressed exit the loop
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                # respond to a keypress
                    if event.key == pygame.K_f:
                        response = "square"
                    elif event.key == pygame.K_j:
                        response = "circle"
            # fill screen
            screen.fill(bgColor)
            #  draw the square
            pygame.draw.circle(screen, shapeColor, (xPos, yPos), radius)
            # draw everything to foreground
            pygame.display.flip()

        # append response to results list
        results["responses"].append(response)

print(results)
# quit pygame
pygame.quit()
