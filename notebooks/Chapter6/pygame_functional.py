# importing pygame
import pygame

# define global program parameters
bgColor = (0, 204, 0)
screenSize = (800, 600)
FPS = 60
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

# main function that runs experiment
def run_program():
    """runs the program"""

    # initialize pygame
    initPygame(screenSize, FPS)

    # start main loop
    mainloop()

    # exit the program
    quitProgram()


def initPygame(screenSize, FPS):
    """
    initializes pygame backends explicitly with
    predefined settings
    """
    # initialize pygame modules
    pygame.init()

    # define screen Settings
    pygame.display.set_caption("My Second PyGame Screen")

    # set frame rate
    clock.tick(FPS)

def renderScreen(color):
    """renders something to screen"""
    # fill screen
    screen.fill(color)

def drawScreen():
    """draws rendered content to screen"""
    # render to screen backbuffer
    renderScreen(bgColor)
    # flip to foreground
    pygame.display.flip()

def mainloop():
    """runs the mainloop"""
    # boolean value to control main loop
    running = True
    # start mein loop
    while running:
        # draw everyting
        drawScreen()
        # wait for 5 seconds then end the program
        pygame.time.wait(5000)
        running = False

def quitProgram():
    """exits pygame explicitly"""
    # quit program
    pygame.quit()


# == start program == #
if __name__ == "__main__":
    run_program()
