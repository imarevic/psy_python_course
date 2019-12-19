# task: create an Experiment class that holds
# all experimeent logic
# Instantiate the Settings class here and use it instead of the settings dictionary
# === import modules === #
import pygame
from datetime import datetime
import os
import sys
import csv
import random
from itertools import zip_longest
# === import custom modules === #
import TextPresenter
from config import *


# ===  define procedures that run the experiment === #
def run_experiment():
    """runs the experiment."""

    # ask for demographics
    demographics_input()

    # initialize pygame and font
    init_pygame_and_exp()

    # load stimuli
    load_stimuli()

    # start welcome, inst1 and inst 2 block
    start_welcome_block()
    start_inst1_block()
    start_inst2_block()

    # start go-nogo task
    start_begintask_block()
    start_task()
    start_endtask_block(1.0)

    # debriefing and endtask
    start_goodbye_block()

    # save results to file
    save_results(settings["filename"], results)

    # exit experiment
    quit_pygame()


# === define helper functions that are called inside run_experiment() === #

# implement this function
# it should ask for demographics input and store it in
# the results dict accordingly
# START CODE HERE #
def demographics_input():
    """Asks for participant demographics."""

    pass
# END CODE HERE #

def load_stimuli():
    """loads stimuli lists."""

    # load items (column 0)
    results["stimlist"] = get_items("stimuli.csv", column=0)


def get_items(filename, column):
    """
    loads items from a csv file and returns a randomly shuffled list
    that will serve as the stimuli list.
    arg1: filename
    arg2: column to read from
    return: shuffled list items
    """

    # opens the file
    with open(os.path.join(settings["stimuliPath"], filename), 'r', newline = "") as csvfile:
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


def init_pygame_and_exp():
    """
    initializes pygame backends explicitly with
    predefined settings.
    """

    # initialize pygame modules
    pygame.init()

    # define results filname
    settings["filename"] = results["id"][0] + \
                          "_gonogo_data_" + \
                          datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + \
                          '.csv'

    # get all relevant paths
    settings["absPath"] = os.path.abspath(os.curdir)
    settings["instPath"] = os.path.join(settings["absPath"], "instructions")
    settings["stimuliPath"] = os.path.join(settings["absPath"], "stimuli")
    settings["dataPath"] = os.path.join(settings["absPath"], "data")

    # load all instructions
    instructions["welcome"] = load_instructions("welcome.txt")
    instructions["intro1"] = load_instructions("intro1.txt")
    instructions["intro2"] = load_instructions("intro2.txt")
    instructions["startTask"] = load_instructions("starttask.txt")
    instructions["endTask"] = load_instructions("endtask.txt")
    instructions["goodbye"] = load_instructions("goodbye.txt")

    # define screen settings
    settings["screen"] = pygame.display.set_mode(settings["screenSize"], pygame.FULLSCREEN)
    pygame.mouse.set_visible(False) # disable mouse

    # set frame rate
    clock = pygame.time.Clock()
    clock.tick(settings["FPS"])

    # get screen rect and set font
    settings["instFont"] = pygame.font.SysFont("Arial", 30)
    settings["screenRect"] = settings["screen"].get_rect()

    # set circle position
    settings["circlePos"] = (settings["screenRect"].centerx, settings["screenRect"].centery)

    # set instruciton text width and height
    settings["instWidth"] = settings["screenSize"][0] - (settings["screenSize"][0] // 10)
    settings["instHeight"] = settings["screenSize"][1] - (settings["screenSize"][1] // 10)


def load_instructions(filename):
    """
    loads instructions from a text file.
    arg: name of file
    returns: content of file
    """

    # open file
    with open(os.path.join(settings["instPath"], filename), 'r') as file:
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
                settings["continue"] = 1


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
                settings["starter"] = 1


def process_quit_event():
    """processes final quit event."""
    for event in pygame.event.get():
        # handle quit event
        if event.type == pygame.QUIT:
            quit_pygame()

        elif event.type == pygame.KEYDOWN:
        # respond to a keypress
            if event.key == pygame.K_q:
                settings["quit"] = 1


def process_isi_event():
    """processes isi event."""
    for event in pygame.event.get():
        # handle quit event
        if event.type == pygame.QUIT:
            quit_pygame()


def process_response_event():
    """processes response event."""
    for event in pygame.event.get():
        # handle quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
        # respond to a keypress
            if event.key == pygame.K_SPACE:
                settings["response"] = "resp"
            else:
                settings["response"] = "noresp"


def start_welcome_block():
    """presents welcome instructions to participant."""

    # set background
    settings["screen"].fill(settings["bgColor"])
    settings["continue"] = 0

    while settings["continue"] != 1:

        # create welcome instruction object
        welcomeInst = TextPresenter.text_object(instructions["welcome"], settings["instFont"],
                                                    settings["instWidth"], settings["instHeight"])
        # blit instructions to screen
        settings["screen"].blit(welcomeInst, (settings["screenRect"].centerx - (settings["instWidth"] // 2),
                                               settings["screenRect"].centery - (settings["instHeight"] // 2)))
        # flip to foreground
        pygame.display.flip()

        # process continue event
        process_continue_event()

# START CODE HERE #
def start_inst1_block():
    """
    presents instructions about purpose
    of experiment to participant.
    """

    pass
# END CODE HERE #

# START CODE HERE #
def start_inst2_block():
    """
    presents instructions about purpose
    of experiment to participant.
    """

    pass
# END CODE HERE #

def start_begintask_block():
    """
    presents instruction to start task
    via pressing space bar.
    """

    # set background
    settings["screen"].fill(settings["bgColor"])
    settings["continue"] = 0

    while settings["starter"] != 1:

        # create begin task intruction object
        startInst = TextPresenter.text_object(instructions["startTask"], settings["instFont"],
                                                    settings["instWidth"], settings["instHeight"])
        # blit instructions to screen
        settings["screen"].blit(startInst, (settings["screenRect"].centerx - (settings["instWidth"] // 2),
                                               settings["screenRect"].centery - (settings["instHeight"] // 2)))
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
    settings["screen"].fill(settings["bgColor"])

    # while loop for drawing end task instructions for "duration" of time.
    while (pygame.time.get_ticks() / 1000) - startTime < duration:

        # create end task instruction object
        endtaskInst = TextPresenter.text_object(instructions["endTask"], settings["instFont"],
                                                    settings["instWidth"], settings["instHeight"])
        # blit instructions to screen
        settings["screen"].blit(endtaskInst, (settings["screenRect"].centerx - (settings["instWidth"] // 2),
                                               settings["screenRect"].centery - (settings["instHeight"] // 2)))
        # flip to foreground
        pygame.display.flip()


def start_goodbye_block():
    """
    presents goodbye instructions
    at end to participant.
    """

    # set background
    settings["screen"].fill(settings["bgColor"])

    while settings["quit"] != 1:

        # create nstruction 2 object
        goodbyeInst = TextPresenter.text_object(instructions["goodbye"], settings["instFont"],
                                                    settings["instWidth"], settings["instHeight"])
        # blit instructions to screen
        settings["screen"].blit(goodbyeInst, (settings["screenRect"].centerx - (settings["instWidth"] // 2),
                                               settings["screenRect"].centery - (settings["instHeight"] // 2)))
        # flip to foreground
        pygame.display.flip()

        # process continue event
        process_quit_event()


def start_task():
    """
    presents items in differing colors.
    arg: stimuluslist of tuples (item, color)
    """

    for stimulus in results['stimlist']:
        # prepare color
        prepare_color(stimulus)

        # draw fixcross, stimulus and ISI
        draw_fixation(1.0)
        draw_stimulus(5.0)
        draw_isi(1.0)


def create_fixation():
    """
    creates fixation cross by defining
    endpoints of the lines.
    """
    # Parameters are two tuples - (x1, y1) - (x2, y2)
    settings["verPoints"] = [(settings["screenRect"].centerx - settings["lineLength"]*0.5,
                       settings["screenRect"].centery),
                      (settings["screenRect"].centerx + settings["lineLength"]*0.5,
                       settings["screenRect"].centery)]

    settings["horPoints"] = [(settings["screenRect"].centerx,
                       settings["screenRect"].centery + settings["lineLength"]*0.5),
                       (settings["screenRect"].centerx,
                        settings["screenRect"].centery -settings["lineLength"]*0.5)]


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
    settings["screen"].fill(settings["bgColor"])

    # while loop for drawing end task instructions for "duration" of time.
    while (pygame.time.get_ticks() / 1000) - startTime < duration:

        # draw vert. and hor. lines
        pygame.draw.lines(settings["screen"], settings["blackColor"], False, settings["verPoints"], settings["lineWidth"])
        pygame.draw.lines(settings["screen"], settings["blackColor"], False, settings["horPoints"], settings["lineWidth"])
        # flip to foreground
        pygame.display.flip()
        # process queue
        process_isi_event()

# implement a function that sets settings["stimcolor"]
# to settings["redColor"] if the passed in stimulus is a "nogo" trial
# and to settings["greenColor"] if the pased in stimulus is a "go" trial
# START CODE HERE #
def prepare_color(stimulus):
    """prepares color to be displayed."""

    pass
# END CODE HERE #

# implement a function that gets a duration as Parameters
# this function should present a circle of color settings["stimcolor"] until
# either 5 seconds have passed without a response or a response was made
# you can check whether a respomnse was made by checking if settings["response"] == "resp"
# if a response was amde, append the reaction time for that trial to results["rts"]
# also append the current response to results["responses"]
# if no response was made, append a reaction time with value "na"
# START CODE HERE #
def draw_stimulus(duration):
    """
    draws stimuli to screen fo duration of time.
    arg: duration
    """

    pass
# END CODE HERE #


def draw_isi(duration):
    """
    draws blank inter-stimulus-interval
    for duration of time.
    arg: duration
    """

    # set background
    settings["screen"].fill(settings["bgColor"])

    # get time stamp
    startTime = pygame.time.get_ticks() / 1000

    # while loop for drawing ISI
    while (pygame.time.get_ticks() / 1000) - startTime < duration:

        # just flip emoty screen to foreground
        pygame.display.flip()

        # process event in isi
        process_isi_event()


def save_results(filename, resultsdict):
    """
    saves results to a csv file.
    arg1: filename
    arg2: dictionary holding resultsdict
    """
    # open data file
    with open(os.path.join(settings["dataPath"] ,filename), 'w', newline="") as file:
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
