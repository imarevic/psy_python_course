# import modules
import pygame, random, math

# === define global program parameters in a dict === #
# this ensures that they are accessible in each function
expGlobals = {"bgColor" : (180, 180, 180), # bg is light grey
              "fixcrossColor" : (0, 0, 0), # color of fixation cross
              "screenSize" : (500, 500), # set screen screenSize
              "FPS" : 60, # frames per second
              "screen" : None, # placeholder for screen instance
              "screenRect" : None, # placeholder for screen rectangle
              "squareRect" : None, # placeholder for square rectangle
              "circlePos" : None, # placeholder for circle position
              "vertPoints" : None, # placeholder for vert. line endpoints of fixation cross
              "horPoints" : None, # placeholder for vert. line endpoints of fixation cross
              "radius" : 50, # radius of circles
              "squareHeight" : 100, # height of squares
              "squareWidth" : 100, # width of squares
              "lineLength" : 40, # lenght of fixation cross lines
              "lineThickness" : 4, # thickness of fixation cross lines
              "colors" : [(250,0,0), (0,250,0), (0,0,250), (250,0,0), (0,0,250), (0,250,0)], # colors of stimuli
              "response" : None
}

def runExperiment():
    """runs the experiment."""

    # initialize pygame
    initPygame(expGlobals["screenSize"], expGlobals["FPS"])

    # start presentation of n trials
    startPresentation()

    # exit Experiment
    quitPygame()


def initPygame(screenSize, FPS):
    """
    initializes pygame backends explicitly with
    predefined settings.
    """

    # initialize pygame modules
    pygame.init()

    # define screen Settings
    expGlobals["screen"] = pygame.display.set_mode(expGlobals["screenSize"])
    pygame.display.set_caption("Learning Experiment")

    # set frame rate
    clock = pygame.time.Clock()
    clock.tick(expGlobals["FPS"])

    # get screen rect, square rect, and circle position
    expGlobals["screenRect"] = expGlobals["screen"].get_rect()
    expGlobals["squareRect"] = pygame.Rect(expGlobals["screenRect"].centerx - expGlobals["squareWidth"]/2,
                                           expGlobals["screenRect"].centery - expGlobals["squareHeight"]/2,
                                           expGlobals["squareWidth"], expGlobals["squareHeight"])
    expGlobals["circlePos"] = (expGlobals["screenRect"].centerx, expGlobals["screenRect"].centery)

# START CODE HERE # (10 - 14 lines of code)
# modify this function
def processMouseEvents():
    """sample user input from the mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

#  END CODE HERE #

def drawCircle(color):
    """draws a circle in a specific color."""

    # start event loop
    while expGlobals["response"] != 1 and expGlobals["response"] != 0:
        # fill screen background
        expGlobals["screen"].fill(expGlobals["bgColor"])
        # draw circle to backbuffer
        pygame.draw.circle(expGlobals["screen"], color,
                           expGlobals["circlePos"], expGlobals["radius"])
        # flip to foreground
        pygame.display.flip()
        # process mouse events
        processMouseEvents()


def createFixCross():
    """creates a fixation cross."""
    # vertical endpoints
    expGlobals["vertPoints"] = [(expGlobals["screenRect"].centerx - expGlobals["lineLength"]/2, expGlobals["screenRect"].centery),
                                (expGlobals["screenRect"].centerx + expGlobals["lineLength"]/2, expGlobals["screenRect"].centery)]
    # horizontal endpoints
    expGlobals["horPoints"] = [(expGlobals["screenRect"].centerx, expGlobals["screenRect"].centery - expGlobals["lineLength"]/2),
                                (expGlobals["screenRect"].centerx, expGlobals["screenRect"].centery + expGlobals["lineLength"]/2)]


def drawFixCross(duration):
    """
    draws the fixation cross to the screen for
    a predefined amount of time.
    """

    # get time stamp and convert it to seconds
    startTime = pygame.time.get_ticks() / 1000

    # create fixation cross
    createFixCross()

    # fill screen background
    expGlobals["screen"].fill(expGlobals["bgColor"])

    # draw the fixcross for duration of time
    while (pygame.time.get_ticks() / 1000) - startTime < duration:
        # draw crossing lines to backbuffer
        pygame.draw.lines(expGlobals["screen"], expGlobals["fixcrossColor"],
                          False, expGlobals["horPoints"], expGlobals["lineThickness"])
        pygame.draw.lines(expGlobals["screen"], expGlobals["fixcrossColor"],
                          False, expGlobals["vertPoints"], expGlobals["lineThickness"])
        # flip to foreground
        pygame.display.flip()


def startPresentation():
    """
    presents circles in differing colors
    and waits for user mouse response.
    """

    for color in expGlobals["colors"]:
        # reset response to None on each trial
        expGlobals["response"] = None
        # draw fix cross
        drawFixCross(1.0)
        # draw circle
        drawCircle(color)

def quitPygame():
    """exits pygame explicitly."""
    # quit program
    pygame.quit()


# == start the program == #
if __name__ == '__main__':
    runExperiment()
