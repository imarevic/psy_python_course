# import pygame modules
import pygame, os, sys
import TextPresenter

# === define global program parameters in a dict === #
expGlobals = {"bgColor" : (180, 180, 180), # bg is light grey
              "textColor" : (0, 0, 0), # text is black
              "screenSize" : (800, 600), # set screen screenSize
              "FPS" : 60, # frames per second
              "screen" : None, # placeholder for screen instance
              "screenRect" : None, # placeholder for screen rectangle
              "font" : None, # placeholder for font
              "instWidth" : None, # placeholder for instruction width
              "instHeight" : None, # placeholder for instruction height
              "absPath" : None, # placeholder for absolute path
              "instPath" : None, # placeholdr for relative path
              "continue" : 0 # boolean value to control continue events
              }

instructions = {"welcome" : None, # placeholder for welcome text
                "studyPurpose1" : None, # placeholder for purpose 1 text
                "studyPurpose2" : None # placeholdr for purpose 2 text
                }


def run_experiment():
    """runs the experiment."""

    # initialize pygame and font
    init_pygame(expGlobals["screenSize"], expGlobals["FPS"])

    # start welcome block
    start_welcome_block()

    # exit Experiment
    quit_pygame()



def init_pygame(screenSize, FPS):
    """
    initializes pygame backends explicitly with
    predefined settings.
    """

    # initialize pygame modules
    pygame.init()

    # get nstructions path
    expGlobals["absPath"] = os.path.abspath(os.curdir)
    expGlobals["instPath"] = os.path.join(expGlobals["absPath"], "instructions/")

    # load all instructions
    instructions["welcome"] = load_instructions("welcome.txt")
    instructions["studyPurpose1"] = load_instructions("studyintro1.txt")
    instructions["studyPurpose2"] = load_instructions("studyintro2.txt")

    # define screen Settings
    expGlobals["screen"] = pygame.display.set_mode(expGlobals["screenSize"])
    pygame.display.set_caption("Learning Experiment")

    # set frame rate
    clock = pygame.time.Clock()
    clock.tick(expGlobals["FPS"])

    # get screen rect and set font
    expGlobals["font"] = pygame.font.SysFont("Arial", 40)
    expGlobals["screenRect"] = expGlobals["screen"].get_rect()

    # set instruciton text width and height
    expGlobals["instWidth"] = expGlobals["screenSize"][0] - (expGlobals["screenSize"][0] // 10)
    expGlobals["instHeight"] = expGlobals["screenSize"][1] - (expGlobals["screenSize"][1] // 10)

def load_instructions(filename):
    """loads instructions from a text file"""

    with open(expGlobals["instPath"] + filename, 'r') as file:
        infile = file.read()

    return infile

def process_continue_event():
    """processes continue events."""
    for event in pygame.event.get():
        # handle quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
        # respond to a keypress
            if event.key == pygame.K_RETURN:
                expGlobals["continue"] = 1

def process_space_event():
    """processes continue events."""
    for event in pygame.event.get():
        # handle quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
        # respond to a keypress
            if event.key == pygame.K_SPACE:
                expGlobals["continue"] = 1

def start_welcome_block():
    """presents welcome instructions to participant."""

    # set background
    expGlobals["screen"].fill(expGlobals["bgColor"])
    expGlobals["continue"] = 0

    while expGlobals["continue"] != 1:

        # create welcome instruction object
        welcomeInst = TextPresenter.text_object(instructions["welcome"], expGlobals["font"],
                                                    expGlobals["instWidth"], expGlobals["instHeight"])
        # blit instructions to screen
        expGlobals["screen"].blit(welcomeInst, (expGlobals["screenRect"].centerx - (expGlobals["instWidth"] // 2),
                                               expGlobals["screenRect"].centery - (expGlobals["instHeight"] // 2)))
        # flip to foreground
        pygame.display.flip()

        # process continue event
        process_continue_event()

    # redrawing background and reseting continue to 0
    expGlobals["screen"].fill(expGlobals["bgColor"])
    expGlobals["continue"] = 0
    while expGlobals["continue"] != 1:

        # create welcome instruction object
        studyInst1 = TextPresenter.text_object(instructions["studyPurpose1"], expGlobals["font"],
                                                    expGlobals["instWidth"], expGlobals["instHeight"])
        # blit instructions to screen
        expGlobals["screen"].blit(studyInst1, (expGlobals["screenRect"].centerx - (expGlobals["instWidth"] // 2),
                                               expGlobals["screenRect"].centery - (expGlobals["instHeight"] // 2)))
        # flip to foreground
        pygame.display.flip()

        # process continue event
        process_continue_event()

    # redrawing background and reseting continue to 0
    expGlobals["screen"].fill(expGlobals["bgColor"])
    expGlobals["continue"] = 0
    while expGlobals["continue"] != 1:

        # create welcome instruction object
        studyInst2 = TextPresenter.text_object(instructions["studyPurpose2"], expGlobals["font"],
                                                    expGlobals["instWidth"], expGlobals["instHeight"])
        # blit instructions to screen
        expGlobals["screen"].blit(studyInst2, (expGlobals["screenRect"].centerx - (expGlobals["instWidth"] // 2),
                                               expGlobals["screenRect"].centery - (expGlobals["instHeight"] // 2)))
        # flip to foreground
        pygame.display.flip()

        # process continue event
        process_space_event()


def quit_pygame():
    """exits pygame explicitly."""
    # quit program
    pygame.quit()


# == start the program == #
if __name__ == '__main__':
    run_experiment()
