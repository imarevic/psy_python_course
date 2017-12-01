# import pygame module
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
              "textItem" : None, # placeholder for the text item
              "textItemRect" : None # placeholder for the item rect
}

# list with study items
studyItems = ['house', 'cat', 'grass', 'dog', 'table', 'pen', 'book']

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
    """renders a stimulus at center of the screen."""

    # render textItem
    expGlobals["textItem"] = expGlobals["font"].render(itemlist[trial], True, expGlobals["textColor"], expGlobals["bgColor"])

    # get text item rect
    expGlobals["textItemRect"] = expGlobals["textItem"].get_rect()

    # place at center of the screen
    expGlobals["textItemRect"].center = expGlobals["screenRect"].center


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
