# === import modules === #
import pygame
import sys
# === import custom modules === #
import TextPresenter
from config import Settings

# ===  define class that handles experiment logic === #
class Experiment():

    # constructor
    def __init__(self):

        # instantiate settings class
        self.settings = Settings()

        # instance experiment attributes
        self.startTime = None
        self.color = None
        self.t_zero = None
        self.rt = None


    def run(self):
        """runs the experiment."""

        # start welcome, inst1 and inst 2 block
        self.start_welcome_block()
        self.start_inst1_block()
        self.start_inst2_block()
        # start stroop task
        self.start_begintask_block()
        self.start_task()
        self.start_endtask_block(1.0)

        # debriefing and endtask
        self.start_goodbye_block()

        # save results to file
        settings.save_results(self.settings.filename, self.settings.results)

        # exit experiment
        self.quit_pygame()

    def process_continue_event(self):
        """processes continue events."""
        for event in pygame.event.get():
            # handle quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
            # respond to a keypress
                if event.key == pygame.K_RETURN:
                    self.settings.continueVal = 1


    def process_start_event(self):
        """processes continue events."""
        for event in pygame.event.get():
            # handle quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
            # respond to a keypress
                if event.key == pygame.K_SPACE:
                    self.settings.starter = 1


    def process_quit_event(self):
        """processes final quit event."""
        for event in pygame.event.get():
            # handle quit event
            if event.type == pygame.QUIT:
                quit_pygame()

            elif event.type == pygame.KEYDOWN:
            # respond to a keypress
                if event.key == pygame.K_q:
                    self.settings.quit = 1


    def process_isi_event(self):
        """processes isi event."""
        for event in pygame.event.get():
            # handle quit event
            if event.type == pygame.QUIT:
                quit_pygame()


    def process_response_event(self):
        """processes response event."""
        for event in pygame.event.get():
            # handle quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
            # respond to a keypress
                if event.key == pygame.K_f:
                    self.settings.response = "congruent"
                elif event.key == pygame.K_j:
                    self.settings.response = "incongruent"


    def start_welcome_block(self):
        """presents welcome instructions to participant."""

        # set background
        self.settings.screen.fill(self.settings.bgColor)
        self.settings.continueVal = 0

        while self.settings.continueVal != 1:

            # create welcome instruction object
            welcomeInst = TextPresenter.text_object(self.settings.inst_welcome, self.settings.instFont,
                                                    self.settings.instWidth, self.settings.instHeight)
            # blit instructions to screen
            self.settings.screen.blit(welcomeInst, (self.settings.screenRect.centerx - (self.settings.instWidth // 2),
                                                   self.settings.screenRect.centery - (self.settings.instHeight // 2)))
            # flip to foreground
            pygame.display.flip()

            # process continue event
            self.process_continue_event()


    def start_inst1_block(self):
        """
        presents instructions about purpose
        of experiment to participant.
        """

        # set background
        self.settings.screen.fill(self.settings.bgColor)
        self.settings.continueVal = 0

        while self.settings.continueVal != 1:

            # create instruction 1 object
            inst1 = TextPresenter.text_object(self.settings.inst_intro1, self.settings.instFont,
                                              self.settings.instWidth, self.settings.instHeight)
            # blit instructions to screen
            self.settings.screen.blit(inst1, (self.settings.screenRect.centerx - (self.settings.instWidth // 2),
                                              self.settings.screenRect.centery - (self.settings.instHeight // 2)))
            # flip to foreground
            pygame.display.flip()

            # process continue event
            self.process_continue_event()


    def start_inst2_block(self):
        """
        presents instructions about purpose
        of experiment to participant.
        """

        # set background
        self.settings.screen.fill(self.settings.bgColor)
        self.settings.continueVal = 0

        while self.settings.continueVal != 1:

            # create nstruction 2 object
            inst2 = TextPresenter.text_object(self.settings.inst_intro2, self.settings.instFont,
                                              self.settings.instWidth, self.settings.instHeight)
            # blit instructions to screen
            self.settings.screen.blit(inst2, (self.settings.screenRect.centerx - (self.settings.instWidth // 2),
                                         self.settings.screenRect.centery - (self.settings.instHeight // 2)))
            # flip to foreground
            pygame.display.flip()

            # process continue event
            self.process_continue_event()


    def start_begintask_block(self):
        """
        presents instruction to start task
        via pressing space bar.
        """

        # set background
        self.settings.screen.fill(self.settings.bgColor)
        self.settings.continueVal = 0

        while self.settings.starter != 1:

            # create begin task intruction object
            startInst = TextPresenter.text_object(self.settings.inst_startTask, self.settings.instFont,
                                                  self.settings.instWidth, self.settings.instHeight)
            # blit instructions to screen
            self.settings.screen.blit(startInst, (self.settings.screenRect.centerx - (self.settings.instWidth // 2),
                                                  self.settings.screenRect.centery - (self.settings.instHeight // 2)))
            # flip to foreground
            pygame.display.flip()

            # process continue event
            self.process_start_event()


    def start_endtask_block(self, duration):
        """
        presents end task instructions for duration
        of time.
        arg: duration (in seconds)
        """

        # get time stamp
        self.startTime = pygame.time.get_ticks() / 1000

        # set background
        self.settings.screen.fill(self.settings.bgColor)

        # while loop for drawing end task instructions for "duration" of time.
        while (pygame.time.get_ticks() / 1000) - self.startTime < duration:

            # create end task instruction object
            endtaskInst = TextPresenter.text_object(self.settings.inst_endTask, self.settings.instFont,
                                                    self.settings.instWidth, self.settings.instHeight)
            # blit instructions to screen
            self.settings.screen.blit(endtaskInst, (self.settings.screenRect.centerx - (self.settings.instWidth // 2),
                                                   self.settings.screenRect.centery - (self.settings.instHeight // 2)))
            # flip to foreground
            pygame.display.flip()


    def start_goodbye_block(self):
        """
        presents goodbye instructions
        at end to participant.
        """

        # set background
        self.settings.screen.fill(self.settings.bgColor)

        while self.settings.quit != 1:

            # create nstruction 2 object
            goodbyeInst = TextPresenter.text_object(self.settings.inst_goodbye, self.settings.instFont,
                                                    self.settings.instWidth, self.settings.instHeight)
            # blit instructions to screen
            self.settings.screen.blit(goodbyeInst, (self.settings.screenRect.centerx - (self.settings.instWidth // 2),
                                               self.settings.screenRect.centery - (self.settings.instHeight // 2)))
            # flip to foreground
            pygame.display.flip()

            # process continue event
            self.process_quit_event()


    def start_task(self):
        """
        presents items in differing colors.
        arg: stimuluslist of tuples (item, color)
        """

        for stimulus in self.settings.stimlist:
            # prepare red stimulus
            self.prepare_stimulus(stimulus)
            # draw fixcross, stimulus and ISI
            self.draw_fixation(1.0)
            self.draw_stimulus()
            self.draw_isi(1.0)


    def prepare_stimulus(self, stimulus):
        """
        Sets individual stimulus at
        center of the screen.
        arg1: stimulus to be centered
        """

        # render word depending on color
        if stimulus[1] == "red":
            self.color = self.settings.redColor
        else:
            self.color = self.settings.blueColor

        # parameters are the string, anti-aliasing, color of text, color of background
        self.settings.item = self.settings.itemFont.render(stimulus[0], True, self.color, self.settings.bgColor)
        # get the rectangle of the item
        self.settings.itemRect = self.settings.item.get_rect()
        # place at the center of the screen
        self.settings.itemRect.center = self.settings.screenRect.center


    def create_fixation(self):
        """
        creates fixation cross by defining
        endpoints of the lines.
        """
        # Parameters are two tuples - (x1, y1) - (x2, y2)
        self.settings.verPoints = [(self.settings.screenRect.centerx - self.settings.lineLength*0.5,
                           self.settings.screenRect.centery),
                          (self.settings.screenRect.centerx + self.settings.lineLength*0.5,
                           self.settings.screenRect.centery)]

        self.settings.horPoints = [(self.settings.screenRect.centerx,
                           self.settings.screenRect.centery + self.settings.lineLength*0.5),
                           (self.settings.screenRect.centerx,
                            self.settings.screenRect.centery - self.settings.lineLength*0.5)]


    def draw_fixation(self, duration):
        """
        draws fixation cross for duration
        of time.
        arg: duration
        """
        # create points of fixcross
        self.create_fixation()

        # get time stamp
        self.startTime = pygame.time.get_ticks() / 1000

        # set background
        self.settings.screen.fill(self.settings.bgColor)

        # while loop for drawing end task instructions for "duration" of time.
        while (pygame.time.get_ticks() / 1000) - self.startTime < duration:

            # draw vert. and hor. lines
            pygame.draw.lines(self.settings.screen, self.settings.blackColor, False, self.settings.verPoints, self.settings.lineWidth)
            pygame.draw.lines(self.settings.screen, self.settings.blackColor, False, self.settings.horPoints, self.settings.lineWidth)
            # flip to foreground
            pygame.display.flip()
            # process queue
            self.process_isi_event()


    def draw_stimulus(self):
        """draws stimuli to screen."""

        # get time stamp for rt recording
        self.t_zero = pygame.time.get_ticks()
        # fill background
        self.settings.screen.fill(self.settings.bgColor)
        # reset response variable
        self.settings.response = None
        # while loop for drawing stimulus to screen for "duration" of time
        while self.settings.response != "congruent" and self.settings.response != "incongruent":

            # process responses
            self.process_response_event()
            # draw to background
            self.settings.screen.blit(self.settings.item, self.settings.itemRect)
            # flip to foreground
            pygame.display.flip()
        # record reaction time
        self.rt = pygame.time.get_ticks() - self.t_zero
        # append response and rt to results dicts
        self.settings.results["rts"].append(self.rt)
        self.settings.results["responses"].append(self.settings.response)


    def draw_isi(self, duration):
        """
        draws blank inter-stimulus-interval
        for duration of time.
        arg: duration
        """

        # set background
        self.settings.screen.fill(self.settings.bgColor)

        # get time stamp
        self.startTime = pygame.time.get_ticks() / 1000

        # while loop for drawing ISI
        while (pygame.time.get_ticks() / 1000) - self.startTime < duration:

            # just flip empty screen to foreground
            pygame.display.flip()

            # process event in isi
            self.process_isi_event()


    def quit_pygame(self):
        """exits pygame explicitly."""
        # quit program
        pygame.quit()
        # exit python
        sys.exit()
