# import modules
import pygame
import math

# === define global program parameters in a dict === #
# this ensures that they are accessible in each function
expGlobals = {"bgColor" : (180, 180, 180), # bg is light grey
              "shapeColor" : (255, 255, 102), # star is yellow
              "fixcrossColor" : (0, 0, 0), # color of fixation cross is black
              "screenSize" : (500, 500), # set screen screenSize
              "FPS" : 60, # frames per second
              "screen" : None, # placeholder for screen instance
              "screenRect" : None, # placeholder for screen rectangle
              "vertPoints" : None, # placeholder for vert. line endpoints of fixation cross
              "horPoints" : None, # placeholder for vert. line endpoints of fixation cross
              "pointList" : None, # placeholder for points list of the star
              "radius" : 80, # radius of the star
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
    pygame.display.set_caption("Star Presentation")

    # set frame rate
    clock = pygame.time.Clock()
    clock.tick(expGlobals["FPS"])

    # get screen rect
    expGlobals["screenRect"] = expGlobals["screen"].get_rect()


def createStar(npoints):
    """creates the points of the star."""
    # set number of points
    npoints = npoints
    # init empty list to store point coordinates
    pointList = []
    # loop through points
    for point in range(npoints * 2):
        # get radius of thr star
        radius = expGlobals["radius"]
        if point % 2 == 0:
            # devde by 2 evry second point
            radius = radius // 2
        # set angle using pi
        ang = (point * 3.14159) / (npoints + 3.14159/60)
        # set x and y relative to screen
        x = expGlobals["screenRect"].centerx + int(math.cos(ang) * radius)
        y = expGlobals["screenRect"].centery + int(math.sin(ang) * radius)
        # append to pointslist
        pointList.append((x, y))

    # store the final list in global dict
    expGlobals["pointList"] = pointList


def drawStar(duration):
    """draws a star for a given duration of time."""

    # get time stamp and convert it to seconds
    startTime = pygame.time.get_ticks() / 1000

    # create the points of the star
    createStar(8)

    # fill screen background
    expGlobals["screen"].fill(expGlobals["bgColor"])

    # draw the circle for duration of time
    while (pygame.time.get_ticks() / 1000) - startTime < duration:
        # draw circle to backbuffer
        pygame.draw.polygon(expGlobals["screen"], expGlobals["shapeColor"], expGlobals["pointList"])
        # flip to foreground
        pygame.display.flip()

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

def startPresentation(ntrials):
    """
    presents stars for amount of ntrials
    with an ISI of 1 sec.
    """

    for trialIdx in range(ntrials):

        # draw the fixcross followed by the star
        drawFixCross(1.0)
        drawStar(4.0)


def quitPygame():
    """exits pygame explicitly."""
    # quit program
    pygame.quit()


# == start the program == #
if __name__ == '__main__':
    runExperiment()
