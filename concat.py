import sys

def my_concatener(strings, separator):
    return separator.join(strings)

def handle_error(argv):
    if len(argv) < 3:
        print('Error')
        sys.exit(1)
    elif argv[-1] != " ":
        print('Error')
        sys.exit(1)
    return argv[1:-1], argv[-1]

strings, separator = handle_error(sys.argv)
result = my_concatener(strings, separator)
print(result)
