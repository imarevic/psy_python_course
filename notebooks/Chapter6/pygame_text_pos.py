# import pygame modules
import pygame

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("My First Text Screen")

# create a font object
# parameters are 'system font type' and 'size'
font = pygame.font.SysFont("Arial", 40)

# === section that creates the rendered text object === #
# create a text string, text color, background color, and a rendered text object
# params of the render method are 'text', anti-aliasing, color and background color
text = "Hello"
textColor = (0, 0, 0) # text is black
bgColor = (160, 160, 160) # bgColor will be light grey
textItem = font.render(text, True, textColor, bgColor)

# specify positions
# first we get the textItem rectangle and the rectangle of the screen
textRect = textItem.get_rect()
screenRect = screen.get_rect()

# next, we place the rect at the center of the screen
textRect.center = screenRect.center
# ===================================================== #

# change color of screen and draw everything
screen.fill(bgColor)
# blit text with the textRect as positional argument
screen.blit(textItem, textRect)
# flip to foreground
pygame.display.flip()

# wait for 8 seconds
pygame.time.wait(8000)
