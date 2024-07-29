import sys

def my_pyramid(element, rows):
    """
    Affiche une pyramide avec l'élément spécifié.

    Args:
        element (str): L'élément à utiliser pour construire la pyramide.
        rows (int): Le nombre de rangées de la pyramide.
    """
    max_width = (rows * 2 - 1) * (len(element) + 1) - 1
    for i in range(1, rows + 1):
        num_elements = 2 * i - 1
        line = (element + " ") * num_elements
        print(line.center(max_width).rstrip())

def error_handling(argv):
    """
    Valide les arguments de la ligne de commande et extrait l'élément et le nombre de rangées.

    Args:
        argv (list): La liste des arguments de la ligne de commande.

    Returns:
        str: L'élément spécifié.
        int: Le nombre de rangées de la pyramide.
    """
    if len(argv) != 3:
        print('Error: Expected two arguments')
        sys.exit(1)
    elif not argv[2].isdigit():
        print('Error: Second argument must be the number of rows')
        sys.exit(1)
    
    return argv[1], int(argv[2])

def parse_command_line_args(argv):
    """
    Parse les arguments de la ligne de commande.

    Args:
        argv (list): La liste des arguments de la ligne de commande.

    Returns:
        str: L'élément spécifié.
        int: Le nombre de rangées de la pyramide.
    """
    return error_handling(argv)

def solve_pyramid(element, rows):
    """
    Résout et affiche la pyramide avec l'élément spécifié.

    Args:
        element (str): L'élément à utiliser pour construire la pyramide.
        rows (int): Le nombre de rangées de la pyramide.
    """
    my_pyramid(element, rows)

if __name__ == "__main__":
    element, rows = parse_command_line_args(sys.argv)
    solve_pyramid(element, rows)
