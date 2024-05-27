import sys

def only_one(liste):
	my_list = [liste[0]]
	for elem in range(1, len(liste)):
		if liste[elem] != liste[elem - 1]:
			my_list.append(liste[elem])
	return ''.join(my_list)

def handle_error(argv):
    if len(argv) != 2:
        print('Error')
        sys.exit(1)
    return argv[1]

def get_arguments():
    arguments = handle_error(sys.argv)
    return arguments

def solving():
	arguments = get_arguments()
	result = only_one(arguments)
	print(result)

solving()
