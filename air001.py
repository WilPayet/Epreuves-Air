import sys

def my_split(string_entered, separator):
    splitted_array = []
    argument = 0
    for char in range(len(string_entered)):
        if string_entered[char:char+len(separator)] == separator:
            splitted_array.append(string_entered[argument:char])
            argument = char + len(separator)
    splitted_array.append(string_entered[argument:])
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
    print(sentence)
