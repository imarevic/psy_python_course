# import pygame modules
import pygame, os
import TextPresenter

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Solution Rendering Multiline Text")

# create a font object
# parameters are 'system font type' and 'size'
font = pygame.font.SysFont("Arial", 28)

# === loading instructions text === #
# get path
absPath = os.path.abspath(os.curdir)
instPath = os.path.join(absPath, "instructions/")

# defining instructions loading function
def load_instructions(filename):
    """loads instructions from a text file"""

    with open(instPath + filename, 'r') as file:
        infile = file.read()

    return infile

# ===================================================== #

# === section that creates the rendered text object === #
# create a text string, text color, background color, and a rendered text object
# params of the render method are 'text', anti-aliasing, color and background color
text = load_instructions("welcome.txt")
textColor = (0, 0, 0) # text is black
bgColor = (160, 160, 160) # bgColor will be light grey
screenRect = screen.get_rect() # get screen rect

# define width and height of text
textwidth = screenRect.width - (screenRect.width//10)
textheight = screenRect.height - (screenRect.height//10)

# create instruction block object
instWelcome = TextPresenter.text_object(text, font, textwidth, textheight)

# ===================================================== #

# change color of screen and draw everything
screen.fill(bgColor)
# blit text with the textRect as positional argument
screen.blit(instWelcome, (screenRect.centerx - (textwidth // 2),
                          screenRect.centery - (textheight // 2)))
# flip to foreground
pygame.display.flip()

# wait for 8 seconds
pygame.time.wait(8000)
