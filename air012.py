import sys

def quick_sort(my_array):
	if not my_array:
		return []
	else:
		pivot = my_array[len(my_array) // 2]  #on a choisi le milieu pour l'élément central. 
		smallest = [] 						  #tableau pour les elements inferieurs au pivot
		middle = [] 						  #tableau pour les elements égaux au pivo
		biggest = [] 						  #tableau pour les elements superieurs au pivot

		#on parcourt chaque elements de la liste et on les place dans les tableaux appropriés. 
		
		for x in my_array:
			if x < pivot:
				smallest.append(x)
			elif x == pivot:
				middle.append(x)
			else:
				biggest.append(x)

		return quick_sort(smallest) + middle + quick_sort(biggest) #on retourne la fonction avec les sous-tableaux inferieurs et superieurs et on concatene les trois sous-tableaux. 

def error_handling(argv):
	if len(argv) < 3:
		print('Error: not enough arguments')
		sys.exit(1)
	for arg in argv[1:]:
		if not arg.isdigit():
			print('Error: only numbers needed')
			sys.exit(1)

	return argv[1:]

def parse_arguments(argv):
	my_array = error_handling(sys.argv)
	return my_array

def solving():
	numbers = parse_arguments(sys.argv)
	result = quick_sort(numbers)
	print(" ".join(map(str, result)))

if __name__ == "__main__":
	solving()
