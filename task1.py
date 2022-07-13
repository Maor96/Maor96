# Print a dictionary of name : address.

from random import choice
def read_ranges():

    # task a - take a country name as an arguement.

    arguments = {}

    with open('ranges.txt', 'r') as f:
        for line in f:
            list_values = []
            line = line.split(':')
            if line[0] in arguments:
                list_values.append(line[1].replace('/24\n', ''))
                arguments[line[0]] += list_values
            else:
                arguments[line[0]] = [line[1].replace('/24\n', '')]

    return arguments

if __name__ == '__main__':
    print(read_ranges())