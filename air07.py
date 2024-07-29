import sys

def sorted_array(my_array, element):
    new_array = my_array.copy()  # Créer une copie du tableau pour éviter de modifier l'original
    index = 0
    for num in new_array:
        if int(element) < num:
            break
        index += 1
    new_array = new_array[:index] + [int(element)] + new_array[index:] ## partager le tableau 'new_array' en 2 et concatener l'element en dernier argument entre les deux
    return new_array

def handle_error(argv):
    my_numbers = []
    for num in argv:
        if not num.isdigit():
            print('Error: arguments have to be numbers')
            sys.exit(1)
        my_numbers.append(int(num))
    if len(my_numbers) < 2:
        print('Error: not enough arguments')
        sys.exit(1)
    return my_numbers[:-1], argv[-1]

def get_numbers():
    my_array, element = handle_error(sys.argv[1:])
    return my_array, element

def solving():
    arguments, element = get_numbers()
    results = sorted_array(arguments, element)
    print(" ".join(map(str, results)))

solving()
