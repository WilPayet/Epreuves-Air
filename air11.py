import sys

def my_pyramid(element, rows):
	for i in range(1, rows + 1):
		print("  " * (rows - i), end="")
		print((element + " ") * (2 * i - 1))

<<<<<<< Updated upstream
def error_handling(argv):
	if len(argv) != 3:
		print('Error: expected two arguments')
		sys.exit(1)
	elif not argv[2].isdigit():
		print('Error: Second argument must be the number of rows')
		sys.exit(1)

	return argv[1], int(argv[2])

def parse_arguments(argv):
	return error_handling(argv)

def solving(element, rows):
=======

def is_valid_argument(argv):
	if len(argv) != 3:
		print('Error: expected two arguments')
		sys.exit(1)

def correct_rows_entered(argv):
	if not argv[2].isdigit():
		print('Error: Second argument must be the number of rows')
		sys.exit(1)
	return int(argv[2])


def parse_arguments(argv):
	is_valid_argument(argv)
	rows = correct_rows_entered(argv)
	element = argv[1]
	return element, rows


def main(element, rows):
>>>>>>> Stashed changes
	my_pyramid(element, rows)


if __name__=="__main__":
	element, rows = parse_arguments(sys.argv)
<<<<<<< Updated upstream
	solving(element, rows)
=======
	main(element, rows)
>>>>>>> Stashed changes
