import sys

def my_split(string_entered, separator):
    splitted_array = []
    argument = 0
<<<<<<< Updated upstream
    for char in range(len(string_entered)):
        if string_entered[char:char+len(separator)] == separator:
            splitted_array.append(string_entered[argument:char])
=======
    for char in range(len(string_entered)):  ##on parcourt chaque éléments de string-entered.
        if string_entered[char:char+len(separator)] == separator:  ##verifie si l'index char est de longueur égale à separator à chaque itération. 
            splitted_array.append(string_entered[argument:char]) ##on ajoute à splitted_array si le separateur est trouvé
>>>>>>> Stashed changes
            argument = char + len(separator)
    splitted_array.append(string_entered[argument:])
    return splitted_array


<<<<<<< Updated upstream
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
=======
def is_valid_argument(argv):
    if len(argv) != 3:
        print("Error: Exactly Two arguments are required")
        sys.exit(1)

def is_non_empty(string_entered):
    if len(string_entered) == 0:
        print('Error: the string cannot be empty')
        sys.exit(1)

def get_argument():
    argv = sys.argv
    is_valid_argument(argv)
    string_entered = argv[1]
    separator = argv[2]
    is_non_empty(string_entered)
    return string_entered, separator


def main():
    string_entered, separator = get_argument()
    result = my_split(string_entered, separator)

    for sentence in result:
        print(sentence)

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
