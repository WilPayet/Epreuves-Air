import sys

def fused_sorted_array(array1, array2):
	new_array = []
	i, j= 0, 0

	while i < len(array1) and j < len(array2):
		if array1[i] < array2[j]:
			new_array.append(array1[i])
			i += 1
		else:
			new_array.append(array2[j])
			j += 1

	new_array += array1[i:]
	new_array += array2[j:]

	return new_array

<<<<<<< Updated upstream
def error_handling(argv):
=======

def is_valid_argument(argv):
>>>>>>> Stashed changes
	have_fusion = False
	for arg in argv:
		if arg == 'fusion':
			have_fusion = True
			break
	if not have_fusion:
<<<<<<< Updated upstream
		print('Error: must be "array1" fusion "array2"')
=======
		print('Error: must contain "fusion" word between "array1" and "array2"')
>>>>>>> Stashed changes
		sys.exit(1)

	fusion_index = argv.index('fusion')
	if fusion_index == 0 or fusion_index == len(argv) - 1:
		print('Error: both arrays must have at least one number')
		sys.exit(1)

<<<<<<< Updated upstream
	for arg in argv[:fusion_index] + argv[fusion_index + 1:]:
=======

def is_valid_number(argv):
	for arg in argv:
>>>>>>> Stashed changes
		if not arg.isdigit():
			print('Error: all arrays must be numbers')
			sys.exit(1)

<<<<<<< Updated upstream
def parsing(argv):
	fusion_index = argv.index('fusion')
	array1 = [int(arg) for arg in argv[:fusion_index]]
	array2 = [int(arg) for arg in argv[fusion_index + 1:]]

	return array1, array2

def solving():
	error_handling(sys.argv[1:])
	array1, array2 = parsing(sys.argv[1:])

	merge_list = fused_sorted_array(array1, array2)
	print(" ".join(map(str, merge_list)))

solving()
=======

def parse_arguments(argv):
	is_valid_argument(argv)
	fusion_index = argv.index('fusion')
	array1 = argv[:fusion_index]
	array2 = argv[fusion_index + 1:]

	is_valid_number(array1 + array2)
	array1 = [int(arg) for arg in array1]
	array2 = [int(arg) for arg in array2]

	return array1, array2

def main():
	argv = sys.argv[1:]
	array1, array2 = parse_arguments(argv)
	merge_array = fused_sorted_array(array1, array2)
	print(" ".join(map(str, merge_array)))

if __name__ == "__main__":
	main()
>>>>>>> Stashed changes

