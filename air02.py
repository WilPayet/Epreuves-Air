import sys

def my_concatener(strings, separator):
    concatenated_string = ""
    for arg in range(len(strings)):
        if arg > 0:
            concatenated_string += separator
        concatenated_string += strings[arg]
    return concatenated_string

<<<<<<< Updated upstream
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
=======
def is_valid_argument(argv):
    if len(argv) < 3:
        print('Error: Not enough arguments')
        sys.exit(1)

def is_non_empty(strings):
    if len(strings) == 0:
        print('Error: The Strings Cannot be empty')
        sys.exit(1)

def get_argument():
    argv = sys.argv[1:]
    is_valid_argument(argv)
    separator = argv[-1]
    strings = argv[:-1]
    is_non_empty(strings)
    return strings, separator

def main():
    strings, separator = get_argument()
    result = my_concatener(strings, separator)
    print(result)

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
