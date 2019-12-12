# imports
import os
from collections import OrderedDict
from datetime import datetime
import csv
import random
from itertools import zip_longest
import pygame

class Settings():

    # class attributes
    bgColor = (180, 180, 180) # bg is light grey
    blackColor = (0, 0, 0) # text is black
    redColor = (250, 0, 0) # red color
    blueColor = (0, 0, 250) # blue color
    screenSize = (1200, 800) # set screen size
    lineLength = 40 # line length of fixcross
    lineWidth = 5 # line width of fixcross
    FPS = 60 # frames per second

    # results dicts
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

    # instance attributes (constructor)
    def __init__(self):

        # init experiment and pygame
        self.init_pygame()
        self.init_experiment()

        # variable instance placeholders
        self.verPoints = None # placeholder for vert. points of fixcross
        self.horPoints = None # placeholder for hor. points of fixcross
        self.stimlist = None # placeholder for stimulus list
        self.item = None # placeholder for the item to be rendered
        self.itemRect = None # placeholder for item rectangle
        self.response = None # variable holding temporary response

        # instance attributes we fill as needed
        self.instWidth = self.screenSize[0] - self.screenSize[0] // 10 # placeholder for instruction width
        self.instHeight = self.screenSize[1] - self.screenSize[1] // 10 # placeholder for instruction height
        self.instPath = self.create_filepath("instructions") # placeholder for relative path
        self.stimuliPath = self.create_filepath("stimuli") # placeholder for stimuli path
        self.dataPath = self.create_filepath("data") # pöaceholder for data path
        self.continueVal=  0 # boolean value to control continue events
        self.starter = 0 # boolean value to control task start events
        self.quit = 0 # boolean value to control closing experiment at end
        self.filename = self.get_filename() # placeholder for filename

        # stimuli loading
        self.load_stimuli()

        # instructions placeholders
        self.inst_welcome = self.load_instructions("welcome.txt") # placeholder for welcome text
        self.inst_intro1 = self.load_instructions("intro1.txt") # placeholder for intro 1 text
        self.inst_intro2 = self.load_instructions("intro2.txt") # placeholder for intro 2 text
        self.inst_startTask = self.load_instructions("starttask.txt") # placeholder for starting task text
        self.inst_endTask = self.load_instructions("endtask.txt") # placeholder for end task text
        self.inst_goodbye = self.load_instructions("goodbye.txt") # placeholder for goodbye text


        # === define helper functions  === #
    def demographics_input(self):
        """Asks for participant demographics."""

        self.results["id"].append(input("Please enter an ID: "))
        self.results["age"].append(input("Please enter your age: "))
        self.results["gender"].append(input("Please enter your gender (m/f/other): "))
        self.results["major"].append(input("Please enter your major: "))


    def load_stimuli(self):
        """loads stimuli lists."""

        # load items (column 0)
        self.results["items"] = self.get_items("stimuli.csv", column=0)

        # load colors (column 1)
        self.results["colors"] = self.get_items("stimuli.csv", column=1)
        # zip lists together to form list of tuples
        self.stimlist = list(zip(self.results["items"], self.results["colors"]))

        # determine ground truth (congruent vs. incongruent) for each tuple in the stimlist
        [self.results["groundtruth"].append("congruent") if x[0] == x[1] else self.results["groundtruth"].append("incongruent") for x in self.stimlist]


    def get_items(self, filename, column):
        """
        loads items from a csv file and returns a randomly shuffled list
        that will serve as the stimuli list.
        arg1: filename
        arg2: column to read from
        return: shuffled list items
        """

        # opens the file
        with open(os.path.join(self.stimuliPath, filename), 'r', newline = "") as csvfile:
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

    def get_filename(self):
        res_string = self.results["id"][0] + \
                        "_stroop_data_" + \
                         datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + \
                        '.csv'
        return res_string

    def create_filepath(self, appended_text_to_abs_path):
        """ get os path and append to it custom directory."""

        absPath = os.path.abspath(os.curdir)
        finalPath = os.path.join(absPath, appended_text_to_abs_path)
        return finalPath

    def init_pygame(self):
        """init pygame explicitly."""

        # initialize pygame modules
        pygame.init()
        pygame.mouse.set_visible(False) # disable mouse

        # set frame rate
        clock = pygame.time.Clock()
        clock.tick(self.FPS)

    def init_experiment(self):
        """
        initializes pygame backends explicitly with
        predefined settings.
        """
        # get demographics
        self.demographics_input()

        # set and innit necessary pygame features
        self.screen = pygame.display.set_mode(self.screenSize, pygame.FULLSCREEN) # placeholder for screen instance
        self.itemFont = pygame.font.SysFont("Arial", 40) # placeholder for item font
        self.instFont = pygame.font.SysFont("Arial", 30) # placeholder for instructions font
        self.screenRect = self.screen.get_rect()


    def load_instructions(self, filename):
        """
        loads instructions from a text file.
        arg: name of file
        returns: content of file
        """

        # open file
        with open(os.path.join(self.instPath, filename), 'r') as file:
            infile = file.read()
        # return content as string
        return infile


    def save_results(self, filename, resultsdict):
        """
        saves results to a csv file.
        arg1: filename
        arg2: dictionary holding resultsdict
        """
        # open data file
        with open(os.path.join(self.dataPath, filename), 'w', newline="") as file:
            # create csv writer
            w = csv.writer(file, delimiter=';')
            # write first row (variable labels)
            w.writerow(resultsdict.keys())
            # write data row wise
            w.writerows(zip_longest(*resultsdict.values()))
