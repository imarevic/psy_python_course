# import modules
import pygame
import random

# === define global program parameters in a dict === #
# this ensures that they are accessible in each function
expGlobals = {"bgColor" : (180, 180, 180), # bg is light grey
              "shapeColor" : (250, 0, 0), # shapes are red
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
              "nTrials" : 5 # number of trials
}

def runExperiment():
    """runs the experiment."""


    # initialize pygame
    initPygame(expGlobals["screenSize"], expGlobals["FPS"])

    # start presentation of n trials
    startPresentation(expGlobals["nTrials"])

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


def drawSquare(duration):
    """renders a square for given duration of time."""

    # get time stamp and convert it to seconds
    startTime = pygame.time.get_ticks() / 1000

    # fill screen background
    expGlobals["screen"].fill(expGlobals["bgColor"])

    # draw the square for duration of time
    while (pygame.time.get_ticks() / 1000) - startTime < duration:
        # draw square to backbuffer
        pygame.draw.rect(expGlobals["screen"], expGlobals["shapeColor"], expGlobals["squareRect"])
        # flip to foreground
        pygame.display.flip()


def drawCircle(duration):
    """draws a circle for a given duration of time."""

    # get time stamp and convert it to seconds
    startTime = pygame.time.get_ticks() / 1000

    # fill screen background
    expGlobals["screen"].fill(expGlobals["bgColor"])

    # draw the circle for duration of time
    while (pygame.time.get_ticks() / 1000) - startTime < duration:
        # draw circle to backbuffer
        pygame.draw.circle(expGlobals["screen"], expGlobals["shapeColor"],
                           expGlobals["circlePos"], expGlobals["radius"])
        # flip to foreground
        pygame.display.flip()

# START CODE HERE # (apr. 3 - 5 lines of code)
def createFixCross():
    """creates a fixation cross."""
    # vertical endpoints
    expGlobals["vertPoints"] = [(expGlobals["screenRect"].centerx - expGlobals["lineLength"]/2, expGlobals["screenRect"].centery),
                                (expGlobals["screenRect"].centerx + expGlobals["lineLength"]/2, expGlobals["screenRect"].centery)]
    # horizontal endpoints
    expGlobals["horPoints"] = [(expGlobals["screenRect"].centerx, expGlobals["screenRect"].centery - expGlobals["lineLength"]/2),
                                (expGlobals["screenRect"].centerx, expGlobals["screenRect"].centery + expGlobals["lineLength"]/2)]
# END CODE HERE #

# START CODE HERE # (apr. 6 - 8 lines of code)
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
# END CODE HERE #

def startPresentation(ntrials):
    """
    presents squares and circles randomly intermixed for amount of ntrials
    with an ISI of 1 sec.
    """

    for trialIdx in range(ntrials):

        # draw a random number between 1 and 10
        randNum = random.randint(1, 10)

        if randNum % 2 == 0:
            # START CODE HERE # (1 line of code)
            drawFixCross(1.0)
            # END CODE HERE #

            # draw square (4 sec) and fixcross (1 sec)
            drawSquare(4.0)

        else:
            # START CODE HERE # (1 line of code)
            drawFixCross(1.0)
            # END CODE HERE #

            # draw circle (4 sec) and fixcross (1 sec)
            drawCircle(4.0)



def quitPygame():
    """exits pygame explicitly."""
    # quit program
    pygame.quit()


# == start the program == #
if __name__ == '__main__':
    runExperiment()
