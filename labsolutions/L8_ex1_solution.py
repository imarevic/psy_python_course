
# importing modules
import os

# specifiying directory path where instructions are located
# first we get absolute path of currrent directory
absPath = os.path.abspath(os.curdir)

# then we join absPath with the taregt directory
instPath = os.path.join(absPath, "instructions")

# initialyzing an empty instructions dictionary
instructions = {"inst1" : None,
                "inst2" : None,
                "inst3" : None
                }

# defining instructions loading function
def load_instructions(filename):
    """loads instructions from a text file"""

    with open(os.path.join(instPath, filename), 'r') as file:
        infile = file.read()

    return infile

# call function to store information in the
# instructions dictionary
instructions["inst1"] = load_instructions("inst1.txt")
instructions["inst2"] = load_instructions("inst2.txt")
instructions["inst3"] = load_instructions("inst3.txt")

# print contents of the dictionary to check that they are stored correctly
print("The contents of the dictionary are:\n")
print(instructions)
print("\n")
print("Instructions printed to console in nice format:\n")
print(instructions["inst1"])
print("\n" + ("#") * 50 + "\n")
print(instructions["inst2"])
print("\n" + ("#") * 50 + "\n")
print(instructions["inst3"])
