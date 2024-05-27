import sys

def my_split(string_entered, separator):
    splitted_array = []
    argument = ""
    for char in string_entered:
        if char == separator:
            if argument:
                splitted_array.append(argument)
            argument = ""
        else:
            argument += char
    splitted_array.append(argument)
    return splitted_array


def handle_error(argv):
    if len(argv) != 3:
        print('Error')
        sys.exit(1)
    elif len(argv[1]) == 0:
        print('Error')
        sys.exit(1)
    else:
        return argv[1]


string_entered = handle_error(sys.argv)
separator = sys.argv[2]

result = my_split(string_entered, separator)

for sentence in result:
    print(sentence, end=' ')
