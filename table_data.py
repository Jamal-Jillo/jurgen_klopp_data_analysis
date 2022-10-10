
# a function that iterates through a text file and returns the next eight lines of the file as a list of strings
# the function iterates until the end of the file
# the function groups the lines into a list of lists, where each list contains the records for a table


def into_lists(filename):
    with open(filename) as f:
        data = f.readlines()
    return [data[i:i+8] for i in range(0, len(data), 8)]
