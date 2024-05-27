import sys

def find_the_one(my_array):
    elements_in_array = {}
    for arg in my_array:
        if arg in elements_in_array:
            elements_in_array[arg] += 1
        else:
            elements_in_array[arg] = 1
    the_one = None
    for elem in my_array:
        if elements_in_array[elem] == 1:
            the_one = elem
            break
    return the_one

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
