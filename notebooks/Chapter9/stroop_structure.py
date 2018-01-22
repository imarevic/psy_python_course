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

    # start stroop task
    start_begintask_block()
    start_task()
    start_endtask_block()

    # debriefing and endtask
    start_goodbye_block()

    # save results to file
    save_results()

    # exit experiment
    quit_pygame()


# === define helper functions that are called inside run_experiment() === #
def demographics_input():
    """Asks for participant demographics."""

    pass


def load_stimuli():
    """loads stimuli lists."""

    pass


def init_pygame_and_exp():
    """
    initializes pygame backends explicitly with
    predefined settings.
    """

    pass

def start_welcome_block():
    """presents welcome instructions to participant."""

    pass


def start_inst1_block():
    """
    presents instructions about purpose
    of experiment to participant.
    """

    pass


def start_inst2_block():
    """
    presents instructions about purpose
    of experiment to participant.
    """

    pass


def start_begintask_block():
    """
    presents instruction to start task
    via pressing space bar.
    """

    pass


def start_endtask_block():
    """
    presents end task instructions for duration
    of time.
    """

    pass


def start_goodbye_block():
    """
    presents goodbye instructions
    at end to participant.
    """

    pass


def start_task():
    """
    presents items in differing colors.
    """

    pass


def save_results():
    """
    saves results to a csv file.
    """

    pass


def quit_pygame():
    """exits pygame explicitly."""

    pass


# == start the program == #
if __name__ == '__main__':
    run_experiment()
