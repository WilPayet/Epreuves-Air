import sys
<<<<<<< Updated upstream
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
	directory = '/Users/wilfridpayet/desktop/Class/TJM/Python/Epreuves Air'
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
=======
from pathlib import Path

def find_file(filename, search_directories):
	for directory in search_directories:
		directory_path = Path(directory)
		for filepath in directory_path.rglob(filename):
			if filepath.name == filename:
				return filepath
	return None


def get_file_content(filepath):
	try:
		return filepath.read_text()
	except Exception as e:
		print(f"Error reading file: {e}")
		sys.exit(1)

def is_valid_argument(argv):
	if len(argv) != 1:
		print('Error: argument has to be <filename.txt>')
		sys.exit(1)

def check_exists_file(filepath, filename):
	if filepath is None:
		print(f'Error: {filename} not found in directories')
		sys.exit(1)


def get_arguments(argv):
	filename = argv[0]
	search_directories = [Path.cwd(), Path.home()]
	filepath = find_file(filename, search_directories)
	return filepath, filename


def main():
	argv = sys.argv[1:]
	is_valid_argument(argv)
	filepath, filename = get_arguments(argv)
	check_exists_file(filepath, filename)
	content = get_file_content(filepath)
	print(content)

if __name__ == '__main__':
	main()
>>>>>>> Stashed changes
