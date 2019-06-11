#!/usr/bin/env python3

# The time module provides useful commands for working with time
# e.g. obtaining the current time. We will need it later, so we import it.
# The random module provides commands for, surprise!, working with random
# numbers, e.g. choosing a stimulus at random from a given list etc.
# We will also need it for the experiment, so we import it.
import time
import random


def run_experiment():
    """
    This function is the main entry for the experiment.
    It calls and coordinates the other helper functions we will use
    for the experiment.
    """

    # Here, we initialize a dictionary to store relevant information
    # about our participant. In this simple experiment, we only need
    # four pieces of information: participant ID, age, sex, major (psychology), a list
    # to store the participant's reaction times, a list to store the stimulus
    # types, and a list to store the whether the participant responded correctly or not.
    # It is always a good practice to set dictionary values which
    # are to-be-filled later to the corresponding empty types
    participant_info = {
        "participantID": "",
        "age": "",
        "sex": "",
        "major": "",
        "reaction_times": [],
        "stimulus_types": [],
        "correct": []
    }

    # Call helper function collect_infos(participant_info)
    # to obtain biographic data
    # Note that the helper functions modifies the participant_info
    # dict, so changes will be reflected in the current function
    # START CODE HERE (1 line of code)

    # END CODE HERE #

    # Call helper function prepare_stimuli()
    # to obtain a list of randomly shuffled stimuli
    # START CODE HERE # (1 line of code)

    # END CODE HERE #

    # Call helper function present_instructions() to display
    # some text explaining the (bizarre) purpose of our experiment
    # START CODE HERE (1 line of code)

    # END CODE HERE #

    # Call helper function start_main_loop(participant_info, stimuli)
    # to run your first experiment!
    # START CODE HERE # (1 line of code)

    # END CODE HERE #

    # Call helper function save_results(participant_info)
    # to save the results from the experiment
    # START CODE HERE # (1 line of code)

    # END CODE HERE

    # Say goodbye to the participant
    goodbye()


def start_main_loop(participant_info, stimuli):
    """
    This function starts the experiment and runs
    len(stimuli) number of trials. As the experiment progresses, the participants'
    responses are stored into the responses key of the info dict.
    :param participant_info: the participant info dict with filled bio data
    :param stimuli: a list of randomly shuffled stimuli
    :return: nothing, since responses are stored in participant_info dict
    """

    # We start the experiment by looping through the list of stimuli
    for stimulus in stimuli:
        # We obtain a timestamp of when the stimulus was presented
        # using the time function

        # START CODE HERE # (1 line of code)

        # END CODE HERE #

        # Then, we present the word by simply printing it to the screen
        # The "\n" * 50 part simply print 50 newlines, to that the last stimulus is hidden
        # form the screen
        print("\n" * 50, stimulus)

        # After that, we wait for the participant to respond
        response = input()

        # Immediately after the response, we calculate the reaction time
        # we use the built-in round() function to round down the rt to
        # 4 decimal places
        rt = round(time.time() - start, 4)
        # ...we evaluate the response
        response_correct = evaluate_response(stimulus, response)
        # ...and add all the information to the participant info dict

        # START CODE HERE # (3 lines of code)



        # END CODE HERE #

def evaluate_response(stimulus, response):
    """
    This function evaluates a response as correct (1) or wrong (0)
    :param stimulus: a string (GO, or NO-GO)
    :param response: the participant's response, should be empty string,
    if stimulus were GO, otherwise an 'a'
    :return: 1, if response correct, 0, if incorrect
    """

    if stimulus == "GO" and response == "":
        return True
    elif stimulus == "NO-GO" and response == "a":
        return True
    else:
        # The only two correct responses are exhausted, so if we reach
        # this block, then the participant responded incorrectly
        return False


def present_instructions():
    """
    This function simply presents the instructions
    and waits for the participant to respond with any key.
    """

    # Prepare text as multi-line string
    instructions = """
    Welcome to our Go/No-Go experiment!\n
    In the following, You are going to see a sequence of words.\n
    The words can be of two types: GO and NO-GO. As You expect,\n
    You are supposed to respond with the enter key as fast as possible\n
    upon seeing the word GO. If the word is NO-GO, you should first type\n
    the letter 'a', and then press enter, thus indicating that you did not\n
    trigger a false alarm.\n\n\n
    Press Enter to continue with the experiment...\n
    """

    # Print on screen and wait for response (collect input with input())
    # START CODE HERE # (2 lines of code)


    # END CODE HERE #

def prepare_stimuli():
    """
    This function initializes a list with 20 randomly shuffled stimuli
    for our reaction time experiment. The stimuli comprise only two types: GO, NO-GO
    Later, these stimuli will be presented in the console window.
    :return: a list with 20 stimuli in a shuffled order.
    """

    # This line initializes a list with 10 'GO' and 10 'NO-GO' stimuli (you can confirm that
    # by printing the list after creation.
    stimuli = ["GO", "NO-GO"] * 10

    # We have initialized our stimuli. The problem is, that they now follow the same
    # pattern: GO, NO-GO, GO,... This is boring and kinda deterministic. Your goal is
    # to look up the online documentation of the random module and find a proper function
    # to randomly shuffle the elements of the list (hint: shuffle)
    # https://docs.python.org/3/library/random.html

    # shuffle the stimuli
    # START CODE HERE # (1 line of code)

    # END CODE HERE #

    # Finaly, we return the randomly shuffled sequence
    return stimuli


def collect_info(participant_info):
    """
    This function collects demographical data from the participant
    and writes it into the participant_info dictionary
    :param participant_info: a dictionary containing keys with empty value
    :return: nothing, since it modified the participant_info dict
    """

    # Collect all data sequentially using the input() function
    # START CODE HERE # (4 lines of code)




    # END CODE HERE #

    # Store input data into the dictionary
    # Note, that we could have performed the collection
    # and the storing in a single step, e.g. p_info['age'] = input(...)
    # Here we will do it in two steps. So next, store the collected info in the
    # participant_info dict:

    # STAR CODE HERE # (4 lines of code)




    # END CODE HERE #

def goodbye():
    """Be nice to the participant and thank her or him for participation."""

    # Define text as a multi-line string
    goodbye_text = """
        Thank you for participating in the experiment!\n
        Your participation means a lot to us. You really\n
        helped pushing science to the next level!\n\n\n
        See you next time!
        """

    # "Clear screen" and present text
    print("\n" * 50, goodbye_text)


def save_results(participant_info):
    """
    This functions saves the participant infos to the disk.
    :param participant_info: the full dictionary
    :return: None
    """

    # Construct a filename from ID and age
    file_name = participant_info["participantID"] + "_" + \
                str(participant_info['age']) + ".txt"

    # Open the file as we already learned
    with open(file_name, "w") as outfile:
        # Write dict to file: note that you cannot
        # simply write the dict itself, as you can
        # normally print it to the screen, but first
        # we have to convert it to a string, since
        # the write() function only accepts a string

        # STAR CODE HERE # (1 line of code)
        
        # END CODE HERE #

        # btw., you usually want to save your data in such a
        # format, so that you can easily read it with a statistical
        # program like SPSS (if SPSS can be called a program) or R
        # can you come up with a better formatting?

if __name__ == "__main__":
    run_experiment()
