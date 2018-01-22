# === import modules === #
import pygame, os, sys, csv, random
import TextPresenter
from collections import OrderedDict
from itertools import zip_longest

# === define global program parameters in dicts === #
# settings dict
_s = {"bgColor" : (180, 180, 180), # bg is light grey
      "blackColor" : (0, 0, 0), # text is black
      "redColor" : (250, 0, 0), # red color
      "blueColor" : (0, 0, 250), # blue color
      "screenSize" : (1200, 800), # set screen size
      "verPoints" : None, # placeholder for vert. points of fixcross
      "horPoints" : None, # placeholder for hor. points of fixcross
      "lineLength" : 40, # line length of fixcross
      "lineWidth" : 5, # line width of fixcross
      "FPS" : 60, # frames per second
      "screen" : None, # placeholder for screen instance
      "screenRect" : None, # placeholder for screen rectangle
      "stimlist" : None, # placeholder for stimulus list
      "item" : None, # placeholder for the item to be rendered
      "itemRect" : None, # placeholder for item rectangle
      "itemFont" : None, # placeholder for item font
      "instFont" : None, # placeholder for instructions font
      "instWidth" : None, # placeholder for instruction width
      "instHeight" : None, # placeholder for instruction height
      "absPath" : None, # placeholder for absolute path
      "instPath" : None, # placeholdr for relative path
      "stimuliPath" : None, # placeholder for stimuli path
      "dataPath" : None, # pöaceholder for data path
      "continue" : 0, # boolean value to control continue events
      "starter" : 0, # boolean value to control task start events
      "quit" : 0, # boolean value to control closing experiment at end
      "response" : None, # variable holding temporary response
      "filename" : None # placeholder for filename
      }

# instructions dict
instructions = {"welcome" : None, # placeholder for welcome text
                "intro1" : None, # placeholder for intro 1 text
                "intro2" : None, # placeholder for intro 2 text
                "startTask" : None, # placeholder for starting task text
                "endTask" : None, # placeholder for end task text
                "goodbye" : None # placeholder for goodbye text
                }

# results dict
results = OrderedDict([("id", []),
                       ("age", []),
                       ("gender", []),
                       ("major", []),
                       ("items", None),
                       ("colors", None),
                       ("groundtruth", []),
                       ("responses", []),
                       ("rts", []),
                       ])

# ===  define procedures that run the experiment === #
def run_experiment():
    """runs the experiment."""

    # ask for demographics
    demographics_input()

    # initialize pygame and font
    init_pygame()

    # load stimuli
    load_stimuli()

    # start welcome, inst1 and inst 2 block
    start_welcome_block()
    start_inst1_block()
    start_inst2_block()

    # start stroop task
    start_begintask_block()
    start_task(_s["stimlist"])
    start_endtask_block(1.0)

    # debriefing and endtask
    start_goodbye_block()
    
    # save results to file
    save_results(_s["filename"], results)

    # exit experiment
    quit_pygame()

# === define helper functions that are called inside run_experiment() === #
def demographics_input():
    """asks for participant demographics."""

    results["id"].append(input("Please enter an ID: "))
    results["age"].append(input("Please enter your age: "))
    results["gender"].append(input("Please enter your gender (m/f/other): "))
    results["major"].append(input("Please enter your major: "))

def load_stimuli():
    """loads stimuli lists."""

    # load items (column 0)
    results["items"] = get_items("stimuli.csv", column=0)
    # load colors (column 1)
    results["colors"] = get_items("stimuli.csv", column=1)
    # zip lists together to form list of tuples
    _s["stimlist"] = list(zip(results["items"], results["colors"]))
    # determine ground truth (congruent vs. incongruent) for each tuple in the stimlist
    [results["groundtruth"].append("congruent") if x[0] == x[1] else results["groundtruth"].append("incongruent") for x in _s["stimlist"]]

def get_items(filename, column):
    """
    loads items from a csv file and returns a randomly shuffled list
    that will serve as the stimuli list.
    arg1: filenmae
    arg2: column to read from
    return: shuffled list items
    """

    # opens the file
    with open(_s["stimuliPath"] + filename, 'r', newline = "") as csvfile:
        # define reader
        reader = csv.reader(csvfile, delimiter=';')
        # initialize local empty list
        items = []
        # iterate over rows of sepcified column
        for row in reader:
            item = row[column]
            items.append(item) # append to local list
        # shuffle list
        random.shuffle(items)
    # return shuffled list
    return items

def init_pygame():
    """
    initializes pygame backends explicitly with
    predefined settings.
    """

    # initialize pygame modules
    pygame.init()

    # define results filname
    _s["filename"] = results["id"][0] + "_stroop_data"

    # get all relevant paths
    _s["absPath"] = os.path.abspath(os.curdir)
    _s["instPath"] = os.path.join(_s["absPath"], "instructions/")
    _s["stimuliPath"] = os.path.join(_s["absPath"], "stimuli/")
    _s["dataPath"] = os.path.join(_s["absPath"], "data/")

    # load all instructions
    instructions["welcome"] = load_instructions("welcome.txt")
    instructions["intro1"] = load_instructions("intro1.txt")
    instructions["intro2"] = load_instructions("intro2.txt")
    instructions["startTask"] = load_instructions("starttask.txt")
    instructions["endTask"] = load_instructions("endtask.txt")
    instructions["goodbye"] = load_instructions("goodbye.txt")

    # define screen settings
    _s["screen"] = pygame.display.set_mode(_s["screenSize"], pygame.FULLSCREEN)
    pygame.mouse.set_visible(False) # disable mouse
    pygame.display.set_caption("Stroop Experiment")

    # set frame rate
    clock = pygame.time.Clock()
    clock.tick(_s["FPS"])

    # get screen rect and set font
    _s["instFont"] = pygame.font.SysFont("Arial", 30)
    _s["itemFont"] = pygame.font.SysFont("Arial", 40)
    _s["screenRect"] = _s["screen"].get_rect()

    # set instruciton text width and height
    _s["instWidth"] = _s["screenSize"][0] - (_s["screenSize"][0] // 10)
    _s["instHeight"] = _s["screenSize"][1] - (_s["screenSize"][1] // 10)

def load_instructions(filename):
    """
    loads instructions from a text file.
    arg: name of file
    returns: content of file
    """

    # open file
    with open(_s["instPath"] + filename, 'r') as file:
        infile = file.read()
    # return content as string
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
                _s["continue"] = 1

def process_start_event():
    """processes continue events."""
    for event in pygame.event.get():
        # handle quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
        # respond to a keypress
            if event.key == pygame.K_SPACE:
                _s["starter"] = 1

def process_quit_event():
    """processes final quit event."""
    for event in pygame.event.get():
        # handle quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
        # respond to a keypress
            if event.key == pygame.K_q:
                _s["quit"] = 1

def process_response_event():
    """processes response event."""
    for event in pygame.event.get():
        # handle quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
        # respond to a keypress
            if event.key == pygame.K_f:
                _s["response"] = "congruent"
            elif event.key == pygame.K_j:
                _s["response"] = "incongruent"


def start_welcome_block():
    """presents welcome instructions to participant."""

    # set background
    _s["screen"].fill(_s["bgColor"])
    _s["continue"] = 0

    while _s["continue"] != 1:

        # create welcome instruction object
        welcomeInst = TextPresenter.text_object(instructions["welcome"], _s["instFont"],
                                                    _s["instWidth"], _s["instHeight"])
        # blit instructions to screen
        _s["screen"].blit(welcomeInst, (_s["screenRect"].centerx - (_s["instWidth"] // 2),
                                               _s["screenRect"].centery - (_s["instHeight"] // 2)))
        # flip to foreground
        pygame.display.flip()

        # process continue event
        process_continue_event()

def start_inst1_block():
    """
    presents instructions about purpose
    of experiment to participant.
    """

    # set background
    _s["screen"].fill(_s["bgColor"])
    _s["continue"] = 0

    while _s["continue"] != 1:

        # create instruction 1 object
        inst1 = TextPresenter.text_object(instructions["intro1"], _s["instFont"],
                                                    _s["instWidth"], _s["instHeight"])
        # blit instructions to screen
        _s["screen"].blit(inst1, (_s["screenRect"].centerx - (_s["instWidth"] // 2),
                                               _s["screenRect"].centery - (_s["instHeight"] // 2)))
        # flip to foreground
        pygame.display.flip()

        # process continue event
        process_continue_event()

def start_inst2_block():
    """
    presents instructions about purpose
    of experiment to participant.
    """

    # set background
    _s["screen"].fill(_s["bgColor"])
    _s["continue"] = 0

    while _s["continue"] != 1:

        # create nstruction 2 object
        inst2 = TextPresenter.text_object(instructions["intro2"], _s["instFont"],
                                                    _s["instWidth"], _s["instHeight"])
        # blit instructions to screen
        _s["screen"].blit(inst2, (_s["screenRect"].centerx - (_s["instWidth"] // 2),
                                               _s["screenRect"].centery - (_s["instHeight"] // 2)))
        # flip to foreground
        pygame.display.flip()

        # process continue event
        process_continue_event()

def start_begintask_block():
    """
    presents instruction to start task
    via pressing space bar.
    """

    # set background
    _s["screen"].fill(_s["bgColor"])
    _s["continue"] = 0

    while _s["starter"] != 1:

        # create begin task intruction object
        startInst = TextPresenter.text_object(instructions["startTask"], _s["instFont"],
                                                    _s["instWidth"], _s["instHeight"])
        # blit instructions to screen
        _s["screen"].blit(startInst, (_s["screenRect"].centerx - (_s["instWidth"] // 2),
                                               _s["screenRect"].centery - (_s["instHeight"] // 2)))
        # flip to foreground
        pygame.display.flip()

        # process continue event
        process_start_event()

def start_endtask_block(duration):
    """
    presents end task instructions for duration
    of time.
    arg: duration (in seconds)
    """

    # get time stamp
    startTime = pygame.time.get_ticks() / 1000

    # set background
    _s["screen"].fill(_s["bgColor"])

    # while loop for drawing end task instructions for "duration" of time.
    while (pygame.time.get_ticks() / 1000) - startTime < duration:

        # create end task instruction object
        endtaskInst = TextPresenter.text_object(instructions["endTask"], _s["instFont"],
                                                    _s["instWidth"], _s["instHeight"])
        # blit instructions to screen
        _s["screen"].blit(endtaskInst, (_s["screenRect"].centerx - (_s["instWidth"] // 2),
                                               _s["screenRect"].centery - (_s["instHeight"] // 2)))
        # flip to foreground
        pygame.display.flip()

def start_goodbye_block():
    """
    presents goodbye instructions
    at end to participant.
    """

    # set background
    _s["screen"].fill(_s["bgColor"])
    _s["continue"] = 0

    while _s["quit"] != 1:

        # create nstruction 2 object
        goodbyeInst = TextPresenter.text_object(instructions["goodbye"], _s["instFont"],
                                                    _s["instWidth"], _s["instHeight"])
        # blit instructions to screen
        _s["screen"].blit(goodbyeInst, (_s["screenRect"].centerx - (_s["instWidth"] // 2),
                                               _s["screenRect"].centery - (_s["instHeight"] // 2)))
        # flip to foreground
        pygame.display.flip()

        # process continue event
        process_quit_event()

def start_task(stimlist):
    """
    presents items in differing colors.
    arg: stimuluslist of tuples (item, color)
    """

    for trialIdx in range(len(stimlist)):
        # prepare red stimulus
        render_stimulus(stimlist, trialIdx)
        # draw fixcross, stimulus and ISI
        draw_fixation(1.0)
        draw_stimulus()
        draw_isi(1.0)
        # append response to results dict
        #

def render_stimulus(stimuli, trial):
    """
    renders individual stimulus at
    center of the screen.
    arg1: itemlist to be rendered
    arg2: current trial
    """

    # render word depending on color
    if stimuli[trial][1] == "red":
        # parameters are the string, anti-aliasing, color of text, color of background
        _s["item"] = _s["itemFont"].render(stimuli[trial][0], True, _s["redColor"], _s["bgColor"])
        # get the rectangle of the item
        _s["itemRect"] = _s["item"].get_rect()
        # place at the center of the screen
        _s["itemRect"].center = _s["screenRect"].center

    elif stimuli[trial][1] == "blue":
        # parameters are the string, anti-aliasing, color of text, color of background
        _s["item"] = _s["itemFont"].render(stimuli[trial][0], True, _s["blueColor"], _s["bgColor"])
        # get the rectangle of the item
        _s["itemRect"] = _s["item"].get_rect()
        # place at the center of the screen
        _s["itemRect"].center = _s["screenRect"].center

def create_fixation():
    """
    creates fixation cross by defining
    endpoints of the lines.
    """
    # Parameters are two tuples - (x1, y1) - (x2, y2)
    _s["verPoints"] = [(_s["screenRect"].centerx - _s["lineLength"]*0.5,
                       _s["screenRect"].centery),
                      (_s["screenRect"].centerx + _s["lineLength"]*0.5,
                       _s["screenRect"].centery)]

    _s["horPoints"] = [(_s["screenRect"].centerx,
                       _s["screenRect"].centery + _s["lineLength"]*0.5),
                       (_s["screenRect"].centerx,
                        _s["screenRect"].centery -_s["lineLength"]*0.5)]
def draw_fixation(duration):
    """
    draws fixation cross for duration
    of time.
    arg: duration
    """
    # create points of fixcross
    create_fixation()

    # get time stamp
    startTime = pygame.time.get_ticks() / 1000

    # set background
    _s["screen"].fill(_s["bgColor"])

    # while loop for drawing end task instructions for "duration" of time.
    while (pygame.time.get_ticks() / 1000) - startTime < duration:

        # draw vert. and hor. lines
        pygame.draw.lines(_s["screen"], _s["blackColor"], False, _s["verPoints"], _s["lineWidth"])
        pygame.draw.lines(_s["screen"], _s["blackColor"], False, _s["horPoints"], _s["lineWidth"])
        # flip to foreground
        pygame.display.flip()

def draw_stimulus():
    """draws stimuli to screen."""

    # get time stamp for rt recording
    t0 = pygame.time.get_ticks()
    # fill background
    _s["screen"].fill(_s["bgColor"])
    # reset response variable
    _s["response"] = None
    # while loop for drawing stimulus to screen for "duration" of time
    while _s["response"] != "congruent" and _s["response"] != "incongruent":

        # process responses
        process_response_event()
        # draw to background
        _s["screen"].blit(_s["item"], _s["itemRect"])
        # flip to foreground
        pygame.display.flip()
    # record reaction time
    rt = pygame.time.get_ticks() - t0
    # append response and rt to results dicts
    results["rts"].append(rt)
    results["responses"].append(_s["response"])

def draw_isi(duration):
    """
    draws blank inter-stimulus-interval
    for duration of time.
    arg: duration
    """
    # get time stamp
    startTime = pygame.time.get_ticks() / 1000

    # set background
    _s["screen"].fill(_s["bgColor"])

    # while loop for drawing ISI
    while (pygame.time.get_ticks() / 1000) - startTime < duration:

        # just flip emoty screen to foreground
        pygame.display.flip()

def save_results(filename, resultsdict):
    """
    saves results to a csv file.
    arg1: filename
    arg2: dictionary holding resultsdict
    """
    # open data file
    with open(_s["dataPath"] + filename, 'w', newline="") as file:
        # create csv writer
        w = csv.writer(file, delimiter=';')
        # write first row (variable labels)
        w.writerow(resultsdict.keys())
        # write data row wise
        w.writerows(zip_longest(*resultsdict.values()))

def quit_pygame():
    """exits pygame explicitly."""
    # quit program
    pygame.quit()
    # exit python
    sys.exit()


# == start the program == #
if __name__ == '__main__':
    run_experiment()
