import sys

def my_concatener(strings, separator):
    concatenated_string = ""
    for arg in range(len(strings)):
        if arg > 0:
            concatenated_string += separator
        concatenated_string += strings[arg]
    return concatenated_string

def handle_error(argv):
    if len(argv) < 3:
        print('Error')
        sys.exit(1)
    separator = argv[-1]
    if separator != " ":
        print('Error')
        sys.exit(1)
    return argv[1:-1], separator

strings, separator = handle_error(sys.argv)
result = my_concatener(strings, separator)
print(result)
