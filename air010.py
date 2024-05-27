import sys
import os

def find_file(filename, directory):
	for dirpath, dirnames, filenames in os.walk(directory):
		if filename in filenames:
			return os.path.join(dirpath, filename)
	return None


def get_file(filepath):
	with open(filepath, 'r') as f:
		content = f.read()
		return content

def handle_error(argv):
	if len(argv) != 1:
		print('Error: argument has to be filename.txt')
		sys.exit(1)

def get_arguments(argv):
	filename = argv[0]
	directory = '/Users/wilfridpayet/desktop/Class/TJM/Python'
	filepath = find_file(filename, directory)
	return filepath, filename, directory

def solving():
	argv = sys.argv[1:]
	handle_error(argv)
	filepath, filename, directory = get_arguments(argv)

	if filepath is None:
		print(f'Error: {filename} not found in directory')
		sys.exit(1)

	result = get_file(filepath)
	print(result)

solving()