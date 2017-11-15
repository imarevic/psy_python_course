#!/usr/bin/env python3

# import time and random module
import time
import random


def run_experiment():
    """
    This function is the main entry for the experiment.
    It calls and coordinates the other helper functions we will use
    for the experiment.
    """

    # initialize a dictionary to store results in
    participant_info = {
        "participantID": "",
        "age": "",
        "sex": "",
        "major": "",
        "reaction_times": [],
        "stimulus_types": [],
        "correct": []
    }

    # call helper function collect_info(participant_info)
    collect_info(participant_info)

    # Call helper function prepare_stimuli()
    # to obtain a list of randomly shuffled stimuli
    stimuli = prepare_stimuli()

    # Call helper function present_instructions() to display
    # some text explaining the task
    present_instructions()

    # Call helper function start_main_loop(participant_info, stimuli)
    # to run the experiment!
    start_main_loop(participant_info, stimuli)

    # Call helper function save_results(participant_info)
    # to save the results from the experiment
    save_results(participant_info)

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
        start = time.time()

        # Then, we present the word by simply printing it to the screen
        # The "\n" * 50 part simply print 50 newlines, to that the last stimulus is hidden
        # from the screen
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
        participant_info['reaction_times'].append(rt)
        participant_info['stimulus_types'].append(stimulus)
        participant_info['correct'].append(response_correct)

def evaluate_response(stimulus, response):
    """
    This function evaluates a response as correct (1) or wrong (0)
    :param stimulus: a string (RED, or BLUE)
    :param response: the participant's response, should be a "j",
    if stimulus was RED, and 'f' is stimulus was BLUE
    :return: 1, if response correct, 0, if incorrect
    """

    if stimulus == "RED" and response == "j":
        return True
    elif stimulus == "BLUE" and response == "f":
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
    Welcome to our reaction time experiment!\n
    In the following, You are going to see a sequence of words.\n
    The words can be of two types: RED or BLUE.\n
    You are asked to press the follwing keys followed by ENTER depending\n
    on the word that is presented:\n
    For RED press the 'j'-key\n
    For BLUE press the 'f'-key\n
    It is important that you press the respective key followed by ENTER\n
    as fast as possible!\n\n\n
    Press ENTER to start the experiment.\n
    """

    # Print on screen and wait for response (collect input with input())
    print(instructions)
    input()

def prepare_stimuli():
    """
    This function initializes a list with 20 randomly shuffled stimuli
    for our reaction time experiment. The stimuli comprise only two types: RED, BLUE
    Later, these stimuli will be presented in the console window.
    :return: a list with 20 stimuli in a shuffled order.
    """

    # This line initializes a list with 10 'RED' and 10 'BLUE' stimuli
    stimuli = ["RED", "BLUE"] * 10

    # shuffle the stimuli
    random.shuffle(stimuli)

    return stimuli


def collect_info(participant_info):
    """
    This function collects demographical data from the participant
    and writes it into the participant_info dictionary
    :param participant_info: a dictionary containing keys with empty value
    :return: nothing, since it modified the participant_info dict
    """

    # Collect all data sequentially using the input() function
    partID = input("Enter a participant ID: ")
    age = input("Enter your age: ")
    sex = input("Enter your gender(m\w\o): ")
    major = input("Enter your subject of study: ")

    # Store input data in the dictionary
    participant_info['participantID'] = partID
    participant_info['age'] = age
    participant_info['sex'] = sex
    participant_info['major'] = major

def goodbye():
    """Be nice to the participant and thank her or him for participation."""

    # Define text as a multi-line string
    goodbye_text = """
        Thank you for participating in the experiment!\n
        Please remain seated until all participants are done.\n\n\n
        Enjoy your day!
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


        # write the dict to file_name
        # convert to to a string to be able to write to a .txt file
        outfile.write(str(participant_info))

if __name__ == "__main__":
    run_experiment()
