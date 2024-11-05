import sys


def my_split(string_entered):
<<<<<<< Updated upstream
    splitted_array = []
    argument = ""
    for arg in string_entered:
        if arg in [' ', '\t', '\n']:
=======

    splitted_array = []
    argument = ""
    for char in string_entered:
        if char.isspace():  #Vérifie si le caractère est un espace, une tab ou un saut de ligne
>>>>>>> Stashed changes
            if argument:
                splitted_array.append(argument)
                argument = ""
        else:
<<<<<<< Updated upstream
            argument += arg
=======
            argument += char
>>>>>>> Stashed changes
    if argument:
        splitted_array.append(argument)
    return splitted_array

<<<<<<< Updated upstream
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
=======
def is_valid_argument(argv):

    if len(argv) < 2:
        print("Error: One argument is required")
        sys.exit(1)

def is_non_empty(string_entered):

    if len(string_entered) == 0:
        print('Error: the string cannot be empty')
        sys.exit(1)

def get_argument():

    argv = sys.argv
    is_valid_argument(argv)
    string_entered = argv[1]
    is_non_empty(string_entered)
    return string_entered

def main():

    string_entered = get_argument()
    result = my_split(string_entered)
    for sentence in result:
        print(sentence)

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
