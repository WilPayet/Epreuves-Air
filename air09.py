import sys

def rotation_to_the_left(array):
    if not array:       #si le tableau est vide, return pour éviter les erreurs
        return array
    return array[1:] + [array[0]]   #rotation vers la gauche: le premier elements devient le dernier

<<<<<<< Updated upstream
def handle_error(argv):
    if len(argv) < 2:
        print('Error: not enough arguments')
        sys.exit(1)
    
    for arg in argv:
        if not arg.isalpha():
            print('Error: all arguments must be words (letters only)')
            sys.exit(1)

    return argv

def get_arguments():
    array = handle_error(sys.argv[1:])
    return array

def solving():
=======
def is_valid_argument(argv):
    if len(argv) < 2:
        print('Error: not enough arguments')
        sys.exit(1)
    return argv
    
def is_valid_character(argv):
    for char in argv:
        if not char.isalpha():
            print('Error: all arguments must be words (letters only)')
            sys.exit(1)
    return argv

def get_arguments():
    argv = sys.argv[1:]
    array = is_valid_argument(argv)
    is_valid_character(array)
    return array

def main():
>>>>>>> Stashed changes
    arguments = get_arguments()
    result = rotation_to_the_left(arguments)
    print(" ".join(result))

<<<<<<< Updated upstream
solving()
=======
if __name__ == '__main__':
    main()
>>>>>>> Stashed changes
