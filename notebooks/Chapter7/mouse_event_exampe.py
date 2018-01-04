# importing pygame
import pygame, math

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
shapeRect = pygame.Rect(screenRect.centerx/2 - shapeWidth/2, screenRect.centery - shapeHeight/2,
                        shapeWidth, shapeHeight)
# get x and y coordinates for circle
xPos = screenRect.width - screenRect.width//4
yPos = screenRect.centery

# stimulus list
stimuli = ["square", "circle", "square", "circle", "square"]

# results dictionary
results = {"responses" : []}

# start loop over stimuli
for stimulus in stimuli:
    # if stimulus is square, present squares and handle events
    if stimulus == "square":
        # present until mouse response is given
        response = None
        running = True
        while running:
            # check for events
            for event in pygame.event.get():
                # if quit button pressed exit the loop
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    # respond to a mousepress
                    mousePos = pygame.mouse.get_pos()
                    clicked = shapeRect.collidepoint(mousePos)
                    # give feedback
                    if clicked == True:
                        response = True
                        print("Correct click!")
                    else:
                        response = False
                        print("False click!")
                    # exit loop
                    running = False

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
        # present until mouse response is given
        response = None
        running = True
        while running:
            # check for events
            for event in pygame.event.get():
                # if quit button pressed exit the loop
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    # get mouse coordinates
                    mousePosX = pygame.mouse.get_pos()[0]
                    mousePosY = pygame.mouse.get_pos()[1]

                    # use distance formula to calculate if mouse inside the circle
                    sqDistX = (mousePosX - xPos)**2
                    sqDistY = (mousePosY - yPos)**2
                    # check if square root distance smaller than radius
                    if math.sqrt(sqDistX + sqDistY) < radius:
                        response = True
                        print("Correct click!")
                    else:
                        response = False
                        print("False click!")
                    # exit loop
                    running = False

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
