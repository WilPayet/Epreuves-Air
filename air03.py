import sys

def find_the_one(my_array):
    elements_in_array = {}
    for arg in my_array:
        if arg in elements_in_array:
            elements_in_array[arg] += 1
        else:
            elements_in_array[arg] = 1
<<<<<<< Updated upstream
    the_one = None
=======
    the_one = None ## valeur None au cas où aucun élément unique n'est trouvé.
>>>>>>> Stashed changes
    for elem in my_array:
        if elements_in_array[elem] == 1:
            the_one = elem
            break
    return the_one

<<<<<<< Updated upstream
def handle_error(argv):
    if len(argv) < 2:
        print('Error')
        sys.exit(1)
    return argv[1:]

def my_array(argv):
    my_array = handle_error(argv)
    return my_array

arguments = my_array(sys.argv)
result = find_the_one(arguments)
print(result)
=======
def is_valid_argument(argv):
    if len(argv) < 2:
        print('Error: Not Enough Argument.')
        sys.exit(1)

def get_argument():
    argv = sys.argv
    is_valid_argument(argv)
    return argv[1:]

def main():
    my_array = get_argument()
    result = find_the_one(my_array)

    if result:
        print(result)
    else:
        print('Error: Nothing unique in here.')

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
