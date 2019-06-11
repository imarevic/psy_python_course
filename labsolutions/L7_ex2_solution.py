# import modules
import csv
from itertools import zip_longest
from collections import OrderedDict

# results dictionary
results = [("id", [1]), ("age", [22]), ("gender", ["female"]),
("major", ["psychology"]),
("items", ["house", "mouse", "grass", "table", "cup", "pen", "candle", "floor", "window"]),
("recalled", ["table", "pen", "grass", "carpet", "floor", "couch", "plant", "candle", "window"]),
("latencies", [2343, 5421, 3245, 2987, 3897, 6763, 2345, 2134, 9875])]

# convert to OrderedDict()
# START CODE HERE #
ordDict = OrderedDict(results)
# END CODE HERE #

# function that saves result to file
# START CODE HERE #
def save(filename, dictname):
    """
    saves dict to a csv file.
    arg1: filename
    arg2: dictionary that needs to bew ritten to csv.
    """

    # open file and write row wise
    with open(filename, 'w') as file:
        # create writer
        writer = csv.writer(file, delimiter=',')
        # write first row with variable names (keys of the dict)
        writer.writerow(dictname.keys())
        # write values row wise
        writer.writerows(zip_longest(*dictname.values())) # dict list values are unpacked first
# END CODE HERE #

# calling saver() function
# START CODE HERE # (1 line of code)
save("results.csv", ordDict)
# END CODE HERE

# print sucess
print("results were saved sucessfully!")
