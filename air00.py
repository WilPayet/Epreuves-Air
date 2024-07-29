import sys


def my_split(string_entered):
    splitted_array = []
    argument = ""
    for arg in string_entered:
        if arg in [' ', '\t', '\n']:
            if argument:
                splitted_array.append(argument)
                argument = ""
        else:
            argument += arg
    if argument:
        splitted_array.append(argument)
    return splitted_array

def handle_error(argv):
    if len(argv) < 2:
        print('Error')
        sys.exit(1)
    elif len(argv[1]) == 0:
        print('Error')
        sys.exit(1)
    else:
        return argv[1]


string_entered = handle_error(sys.argv)

result = my_split(string_entered)

for sentence in result:
    print(sentence)