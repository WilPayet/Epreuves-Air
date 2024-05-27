import sys

def my_split(string_entered, separator):
    return string_entered.split(separator)


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
