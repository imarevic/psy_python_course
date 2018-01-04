# import modules
import pygame
import random

# === define global program parameters in a dict === #
# this ensures that they are accessible in each function
expGlobals = {"bgColor" : (180, 180, 180), # bg is light grey
              "shapeColor" : (250, 0, 0), # shapes are red
              "screenSize" : (500, 500), # set screen screenSize
              "FPS" : 60, # frames per second
              "screen" : None, # placeholder for screen instance
              "screenRect" : None, # placeholder for screen rectangle
              "squareRect" : None, # placeholder for square rectangle
              "circlePos" : None, # placeholder for circle position
              "radius" : 50, # radius of circles
              "squareHeight" : 100, # height of squares
              "squareWidth" : 100, # width of squares
              "nTrials" : 5, # number of trials
              "response" : None # holds response on each trial
}

results = {"stimuli" : [],
           "responses" : []
}

def runExperiment():
    """runs the experiment."""

    # initialize pygame and font
    initPygame(expGlobals["screenSize"], expGlobals["FPS"])

    # start presentation of n trials
    startPresentation(expGlobals["nTrials"])

    # print the stimuli and response list
    print("stimmuli were: ", results["stimuli"])
    print("resonses were: ", results["responses"])

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

def processEvents():
    """sample user input for the task."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
        # Respond to a keypress
            if event.key == pygame.K_f:
                expGlobals["response"] = "square"
            elif event.key == pygame.K_j:
                expGlobals["response"] = "circle"


def drawSquare():
    """draws a square."""

    # set response to be None
    expGlobals["response"] = None

    # draw circle until user responds
    while expGlobals["response"] != "square" and expGlobals["response"] != "circle":

        # fill screen background
        expGlobals["screen"].fill(expGlobals["bgColor"])
        # draw square to backbuffer
        pygame.draw.rect(expGlobals["screen"], expGlobals["shapeColor"], expGlobals["squareRect"])
        # flip to foreground
        pygame.display.flip()
        # process events
        processEvents()


def drawCircle():
    """draws a circle."""

    # set response to be None
    expGlobals["response"] = None

    # draw circle until user responds
    while expGlobals["response"] != "square" and expGlobals["response"] != "circle":

        # fill screen background
        expGlobals["screen"].fill(expGlobals["bgColor"])
        # draw circle to backbuffer
        pygame.draw.circle(expGlobals["screen"], expGlobals["shapeColor"],
                           expGlobals["circlePos"], expGlobals["radius"])
        # flip to foreground
        pygame.display.flip()
        # process events
        processEvents()

def drawISI(duration):
    """
    draws a blank screen for a given duration of time (inter stimulus intervall (ISI)).
    Note that nothing needs to be rendered, as this is only the ISI
    with a blank background.
    """

    # get time stamp and convert it to seconds
    startTime = pygame.time.get_ticks() / 1000

    # fill background
    expGlobals["screen"].fill(expGlobals["bgColor"])

    # while loop for drawing blank ISI screen for "duration" of time.
    while (pygame.time.get_ticks() / 1000) - startTime < duration:
        pygame.display.flip()


def startPresentation(ntrials):
    """
    presents squares and circles randomly intermixed for amount of ntrials
    with an ISI of 1 sec.
    """

    for trialIdx in range(ntrials):

        # draw a random number between 1 and 10
        randNum = random.randint(1, 10)

        if randNum % 2 == 0:
            # draw square and ISI
            drawISI(1.0)
            drawSquare()
            results["stimuli"].append("square")

        else:
            # draw circle and ISI
            drawISI(1.0)
            drawCircle()
            results["stimuli"].append("circle")

        # append response to results dictionary
        results["responses"].append(expGlobals["response"])

def quitPygame():
    """exits pygame explicitly."""
    # quit program
    pygame.quit()


# == start the program == #
if __name__ == '__main__':
    runExperiment()
