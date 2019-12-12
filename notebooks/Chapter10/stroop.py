# === import modules === #
import pygame
import sys
# === import custom modules === #
import TextPresenter
from config import Settings

# instatiate classes
settings = Settings()

# ===  define procedure that runs the experiment === #
def run_experiment():
    """runs the experiment."""

    # start welcome, inst1 and inst 2 block
    start_welcome_block()
    start_inst1_block()
    start_inst2_block()
    # start stroop task
    start_begintask_block()
    start_task()
    start_endtask_block(1.0)

    # debriefing and endtask
    start_goodbye_block()

    # save results to file
    settings.save_results(settings.filename, settings.results)

    # exit experiment
    quit_pygame()

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
                settings.continueVal = 1


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
                settings.starter = 1


def process_quit_event():
    """processes final quit event."""
    for event in pygame.event.get():
        # handle quit event
        if event.type == pygame.QUIT:
            quit_pygame()

        elif event.type == pygame.KEYDOWN:
        # respond to a keypress
            if event.key == pygame.K_q:
                settings.quit = 1


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
            if event.key == pygame.K_f:
                settings.response = "congruent"
            elif event.key == pygame.K_j:
                settings.response = "incongruent"


def start_welcome_block():
    """presents welcome instructions to participant."""

    # set background
    settings.screen.fill(settings.bgColor)
    settings.continueVal = 0

    while settings.continueVal != 1:

        # create welcome instruction object
        welcomeInst = TextPresenter.text_object(settings.inst_welcome, settings.instFont,
                                                settings.instWidth, settings.instHeight)
        # blit instructions to screen
        settings.screen.blit(welcomeInst, (settings.screenRect.centerx - (settings.instWidth // 2),
                                               settings.screenRect.centery - (settings.instHeight // 2)))
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
    settings.screen.fill(settings.bgColor)
    settings.continueVal = 0

    while settings.continueVal != 1:

        # create instruction 1 object
        inst1 = TextPresenter.text_object(settings.inst_intro1, settings.instFont,
                                                    settings.instWidth, settings.instHeight)
        # blit instructions to screen
        settings.screen.blit(inst1, (settings.screenRect.centerx - (settings.instWidth // 2),
                                               settings.screenRect.centery - (settings.instHeight // 2)))
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
    settings.screen.fill(settings.bgColor)
    settings.continueVal = 0

    while settings.continueVal != 1:

        # create nstruction 2 object
        inst2 = TextPresenter.text_object(settings.inst_intro2, settings.instFont,
                                                    settings.instWidth, settings.instHeight)
        # blit instructions to screen
        settings.screen.blit(inst2, (settings.screenRect.centerx - (settings.instWidth // 2),
                                               settings.screenRect.centery - (settings.instHeight // 2)))
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
    settings.screen.fill(settings.bgColor)
    settings.continueVal = 0

    while settings.starter != 1:

        # create begin task intruction object
        startInst = TextPresenter.text_object(settings.inst_startTask, settings.instFont,
                                                    settings.instWidth, settings.instHeight)
        # blit instructions to screen
        settings.screen.blit(startInst, (settings.screenRect.centerx - (settings.instWidth // 2),
                                               settings.screenRect.centery - (settings.instHeight // 2)))
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
    settings.screen.fill(settings.bgColor)

    # while loop for drawing end task instructions for "duration" of time.
    while (pygame.time.get_ticks() / 1000) - startTime < duration:

        # create end task instruction object
        endtaskInst = TextPresenter.text_object(settings.inst_endTask, settings.instFont,
                                                    settings.instWidth, settings.instHeight)
        # blit instructions to screen
        settings.screen.blit(endtaskInst, (settings.screenRect.centerx - (settings.instWidth // 2),
                                               settings.screenRect.centery - (settings.instHeight // 2)))
        # flip to foreground
        pygame.display.flip()


def start_goodbye_block():
    """
    presents goodbye instructions
    at end to participant.
    """

    # set background
    settings.screen.fill(settings.bgColor)

    while settings.quit != 1:

        # create nstruction 2 object
        goodbyeInst = TextPresenter.text_object(settings.inst_goodbye, settings.instFont,
                                                    settings.instWidth, settings.instHeight)
        # blit instructions to screen
        settings.screen.blit(goodbyeInst, (settings.screenRect.centerx - (settings.instWidth // 2),
                                               settings.screenRect.centery - (settings.instHeight // 2)))
        # flip to foreground
        pygame.display.flip()

        # process continue event
        process_quit_event()


def start_task():
    """
    presents items in differing colors.
    arg: stimuluslist of tuples (item, color)
    """

    for stimulus in settings.stimlist:
        # prepare red stimulus
        prepare_stimulus(stimulus)
        # draw fixcross, stimulus and ISI
        draw_fixation(1.0)
        draw_stimulus()
        draw_isi(1.0)


def prepare_stimulus(stimulus):
    """
    Sets individual stimulus at
    center of the screen.
    arg1: stimulus to be centered
    """

    # render word depending on color
    if stimulus[1] == "red":
        color = settings.redColor
    else:
        color = settings.blueColor

    # parameters are the string, anti-aliasing, color of text, color of background
    settings.item = settings.itemFont.render(stimulus[0], True, color, settings.bgColor)
    # get the rectangle of the item
    settings.itemRect = settings.item.get_rect()
    # place at the center of the screen
    settings.itemRect.center = settings.screenRect.center


def create_fixation():
    """
    creates fixation cross by defining
    endpoints of the lines.
    """
    # Parameters are two tuples - (x1, y1) - (x2, y2)
    settings.verPoints = [(settings.screenRect.centerx - settings.lineLength*0.5,
                       settings.screenRect.centery),
                      (settings.screenRect.centerx + settings.lineLength*0.5,
                       settings.screenRect.centery)]

    settings.horPoints = [(settings.screenRect.centerx,
                       settings.screenRect.centery + settings.lineLength*0.5),
                       (settings.screenRect.centerx,
                        settings.screenRect.centery - settings.lineLength*0.5)]


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
    settings.screen.fill(settings.bgColor)

    # while loop for drawing end task instructions for "duration" of time.
    while (pygame.time.get_ticks() / 1000) - startTime < duration:

        # draw vert. and hor. lines
        pygame.draw.lines(settings.screen, settings.blackColor, False, settings.verPoints, settings.lineWidth)
        pygame.draw.lines(settings.screen, settings.blackColor, False, settings.horPoints, settings.lineWidth)
        # flip to foreground
        pygame.display.flip()
        # process queue
        process_isi_event()


def draw_stimulus():
    """draws stimuli to screen."""

    # get time stamp for rt recording
    t0 = pygame.time.get_ticks()
    # fill background
    settings.screen.fill(settings.bgColor)
    # reset response variable
    settings.response = None
    # while loop for drawing stimulus to screen for "duration" of time
    while settings.response != "congruent" and settings.response != "incongruent":

        # process responses
        process_response_event()
        # draw to background
        settings.screen.blit(settings.item, settings.itemRect)
        # flip to foreground
        pygame.display.flip()
    # record reaction time
    rt = pygame.time.get_ticks() - t0
    # append response and rt to results dicts
    settings.results["rts"].append(rt)
    settings.results["responses"].append(settings.response)


def draw_isi(duration):
    """
    draws blank inter-stimulus-interval
    for duration of time.
    arg: duration
    """

    # set background
    settings.screen.fill(settings.bgColor)

    # get time stamp
    startTime = pygame.time.get_ticks() / 1000

    # while loop for drawing ISI
    while (pygame.time.get_ticks() / 1000) - startTime < duration:

        # just flip empty screen to foreground
        pygame.display.flip()

        # process event in isi
        process_isi_event()


def quit_pygame():
    """exits pygame explicitly."""
    # quit program
    pygame.quit()
    # exit python
    sys.exit()


# == start the program == #
if __name__ == '__main__':
    run_experiment()
