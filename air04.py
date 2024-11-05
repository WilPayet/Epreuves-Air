import sys

def only_one(liste):
	my_list = [liste[0]]
	for elem in range(1, len(liste)):
		if liste[elem] != liste[elem - 1]:
			my_list.append(liste[elem])
	return ''.join(my_list)

<<<<<<< Updated upstream
def handle_error(argv):
    if len(argv) != 2:
        print('Error')
=======
def is_valid_argument(argv):
    if len(argv) != 2:
        print('Error: Only one argument is required')
>>>>>>> Stashed changes
        sys.exit(1)
    return argv[1]

def get_arguments():
<<<<<<< Updated upstream
    arguments = handle_error(sys.argv)
    return arguments

def solving():
=======
    arguments = is_valid_argument(sys.argv)
    return arguments

def main():
>>>>>>> Stashed changes
	arguments = get_arguments()
	result = only_one(arguments)
	print(result)

<<<<<<< Updated upstream
solving()
=======
if __name__ == "__main__":
	main()
>>>>>>> Stashed changes
