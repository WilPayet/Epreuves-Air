import sys

<<<<<<< Updated upstream
def pass_control(my_array, string):
    results = []
    strings = string.lower()
    for arg in my_array:
        arg = arg.lower()
        contains_letter = 0     ## équivalent de false
        for letter in arg:
            if letter == strings:
                contains_letter = 1     ## équivalent de true
                break
        if not contains_letter:
            results.append(arg)
    return results

def handle_error(argv):
    if len(argv) < 2:
        print('Error: not enough arguments')
        sys.exit(1)
    for arg in argv[:-1]:
        if not isinstance(arg, str):
            print('Error: arguments have to be strings')
            sys.exit(1)
    if not isinstance(argv[-1], str):
        print('Error: last argument has to be a string')
        sys.exit(1)
    return argv[:-1], argv[-1]

def get_arguments():
    my_array, string = handle_error(sys.argv[1:])
    return my_array, string

def solution():
    arguments, string = get_arguments()
    results = pass_control(arguments, string)
    print("Results:", ', '.join(results))

solution()
=======
def pass_control(my_array, strings):
    results = []
    strings = strings.lower()
    for arg in my_array:
        args = arg.lower()
        contains_letters = False
        for letter in strings:
            if letter in args:
                contains_letters = True
                break
        if not contains_letters:
            results.append(arg)
    return results

def is_valid_argument(argv):
    if len(argv) < 2:
        print('Error: not enough arguments provided')
        sys.exit(1)
    
    return argv[:-1], argv[-1]

def get_arguments():
    my_array, strings = is_valid_argument(sys.argv[1:])
    return my_array, strings

def main():
    arguments, strings = get_arguments()
    results = pass_control(arguments, strings)
    if results:
        print(", ".join(results))
    else:
        print("All arguments contain one of the search strings:", ', '.join(strings))

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
