# imports
import os
import csv
import random
import pygame
from datetime import datetime
from itertools import zip_longest
from collections import OrderedDict

# Settings class
class Settings():

    # class attributes
    radius = 60 # radius of cricle
    lineLength = 40 # line length of fixcross
    lineWidth = 5 # line width of fixcross
    FPS = 60 # frames per second
    bgColor = (180, 180, 180) # bg is light grey
    blackColor = (0, 0, 0) # text is black
    redColor = (255, 0, 0) # red color
    greenColor = (0, 255, 0) # blue color
    screenSize = (1200, 800) # set screen size

    # results dict
    results = OrderedDict([("id", []),
                           ("age", []),
                           ("gender", []),
                           ("major", []),
                           ("stimlist", []),
                           ("responses", []),
                           ("rts", []),
                           ])

    # instance attributes
    def __init__(self):

        # init experiment and pygame
        self.init_pygame()
        self.init_experiment()

        # variable instance placeholders
        self.stimcolor = None # placeholder for stimulus color
        self.verPoints = None # placeholder for vert. points of fixcross
        self.horPoints = None # placeholder for hor. points of fixcross
        self.response = None # variable holding temporary response

        # attributes that get filled
        self.instWidth = self.screenSize[0] - (self.screenSize[0] // 10)
        self.instHeight = self.screenSize[1] - (self.screenSize[1] // 10)
        self.continueVal = 0 # boolean value to control continue events
        self.starter = 0 # boolean value to control task start events
        self.quit = 0 # boolean value to control closing experiment at end
        self.filename = self.get_filename()
        self.instPath = self.create_filepath("instructions")
        self.stimuliPath = self.create_filepath("stimuli")
        self.dataPath = self.create_filepath("data")

        # stimuli loading
        self.load_stimuli()

        # load load instructions
        self.inst_welcome = self.load_instructions("welcome.txt")
        self.inst_intro1 = self.load_instructions("intro1.txt")
        self.inst_intro2 = self.load_instructions("intro2.txt")
        self.inst_startTask = self.load_instructions("starttask.txt")
        self.inst_endTask = self.load_instructions("endtask.txt")
        self.inst_goodbye = self.load_instructions("goodbye.txt")


    # === define helper functions that are called inside run_experiment() === #
    def demographics_input(self):
        """Asks for participant demographics."""

        self.results["id"].append(input("Please enter an ID: "))
        self.results["age"].append(input("Please enter your age: "))
        self.results["gender"].append(input("Please enter your gender (m/f/other): "))
        self.results["major"].append(input("Please enter your major: "))

    def init_pygame(self):
        """
        initializes pygame explicitly.
        """
        # initialize pygame modules
        pygame.init()
        pygame.mouse.set_visible(False) # disable mouse

        # set frame rate
        clock = pygame.time.Clock()
        clock.tick(self.FPS)


    def init_experiment(self):
        """
        initializes experiment pygame settings explicitly with
        predefined params.
        """

        # get demographics
        self.demographics_input()
        # define screen settings
        self.screen = pygame.display.set_mode(self.screenSize, pygame.FULLSCREEN)
        # get screen rect and set font
        self.instFont = pygame.font.SysFont("Arial", 30)
        self.screenRect = self.screen.get_rect()
        # set circle position
        self.circlePos = (self.screenRect.centerx, self.screenRect.centery)

    def create_filepath(self, appended_text_to_abs_path):
        """ get os path and append to it custom directory."""

        absPath = os.path.abspath(os.curdir)
        finalPath = os.path.join(absPath, appended_text_to_abs_path)
        return finalPath

    def get_filename(self):
        res_string = self.results["id"][0] + \
                        "_stroop_data_" + \
                         datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + \
                        '.csv'
        return res_string

    def load_stimuli(self):
        """loads stimuli lists."""

        # load items (column 0)
        self.results["stimlist"] = self.get_items("stimuli.csv", column=0)


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
        with open(os.path.join(self.dataPath ,filename), 'w', newline="") as file:
            # create csv writer
            w = csv.writer(file, delimiter=';')
            # write first row (variable labels)
            w.writerow(resultsdict.keys())
            # write data row wise
            w.writerows(zip_longest(*resultsdict.values()))
