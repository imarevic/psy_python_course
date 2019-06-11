# import modules
import random
import pygame

# === define global program parameters in a dict === #
# this ensures that they are accessible in each function
expGlobals = {"bgColor" : (180, 180, 180), # bg is light grey
              "textColor" : (0, 0, 0), # text is black
              "screenSize" : (800, 600), # set screen screenSize
              "FPS" : 60, # frames per second
              "screen" : None, # placeholder for screen instance
              "screenRect" : None, # placeholder for screen rectangle
              "font" : None, # placeholder for font
              "textItem" : None, # placeholder for the final text item
              "textItemRect" : None # placeholder for final item rect
}

# list with study items (animals and flowers)
studyItems = ['dog', 'cat', 'tiger', 'lion', 'rose', 'tulip', 'daisy', 'sunflower']

# shuffle the list by using the random modules shuffle function
# START CODE HERE # (1 line of code)


# END CODE HERE #

def runExperiment():
    """runs the experiment."""

    # initialize pygame and font
    initPygame(expGlobals["screenSize"], expGlobals["FPS"])

    # start study Block
    startStudy(studyItems)

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

    # get screen rect
    expGlobals["font"] = pygame.font.SysFont("Arial", 40)
    expGlobals["screenRect"] = expGlobals["screen"].get_rect()


def renderStimulus(itemlist, trial):
    """
    renders a stimulus randomly either on
    left or right side of the screen.
    """

    # render textItem in the specified font
    # START CODE HERE # (1 line of code)

    
    # END CODE HERE #

    # get text item rect
    # START CODE HERE # (1 line of code)


    # END CODE HERE #

    # place that rectangle either on left or right on the screen
    # depending on a random number drawn between 1 and 10:
        # if number == even then left
        # if number == odd then right
    number = random.randint(1, 10)

    # STAR CODE HERE # (aprox. 4 - 6 line of code)





    # END CODE HERE #

def drawStimulus(duration):
    """draws a stimulus for a given duration of time."""

    # get time stamp and convert it to seonds
    startTime = pygame.time.get_ticks() / 1000

    # fill background
    expGlobals["screen"].fill(expGlobals["bgColor"])

    # while loop for drawing stimulus to screen for "duration" of time
    while (pygame.time.get_ticks() / 1000) - startTime < duration:
        # draw to backbuffer
        expGlobals["screen"].blit(expGlobals["textItem"], expGlobals["textItemRect"])
        # flip to foreground
        pygame.display.flip()

def drawISI(duration):
    """
    draws a blank screen for a given duration of time (inter stimulus intervall (ISI)).
    Note that nothing needs to be rendered, as this is only the ISI
    with a blank background."""

    # get time stamp and convert it to seconds
    startTime = pygame.time.get_ticks() / 1000

    # fill background
    expGlobals["screen"].fill(expGlobals["bgColor"])

    # while loop for drawing blank ISI screen for "duration" of time.
    while (pygame.time.get_ticks() / 1000) - startTime < duration:
        pygame.display.flip()

def startStudy(itemlist):
    "loops through item list and presents each item."

    for trialIdx in range(len(itemlist)):

        # render stimuli stimuli
        renderStimulus(itemlist, trialIdx)

        # draw stimuli and ISI to screen
        drawStimulus(5.0)
        drawISI(1.0)

def quitPygame():
    """exits pygame explicitly."""
    # quit program
    pygame.quit()


# == start the program == #
if __name__ == '__main__':
    runExperiment()
