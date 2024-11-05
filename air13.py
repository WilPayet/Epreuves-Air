import subprocess

<<<<<<< Updated upstream
scripts_list = {
    "air00.py": [["Bonjour les gars"], ["23"]],
    "air01.py": [["crevette"], ["salut tout le monde", "le"]],
    "air02.py": [["je" "teste" "des" "trucs" " "], ["10", "Je"]],
    "air03.py": [[1, 2, 3, 4, 5, 4, 3, 2, 1], ["bonjour", "monsieur", "bonjour"], ["bonjour"]],
    "air04.py": [["Hello milady,  bien ou quoi ??"], ["10", "11", "12"]],
    "air05.py": [[1, 2, 3, 4, 5, "+2"], ["10", "20", "30", "40", "50", "-5"], ["bonjour"]],
    "air06.py": [["Michel", "Albert", "Thérèse", "Benoit", "t"], ["Michael", "23"]],
    "air07.py": [[1, 3, 4, 2], ["a", "b", "e", "c", "d"], ["10", "20", "30", "40", "50", "60", "70", "25"]],
    "air08.py": [["10", "20", "30", "fusion", "15", "25", "35"], ["fusion", "fusion"]],
    "air09.py": [["Michel", "Albert", "Thérèse", "Benoit"], ["1", "2", "3", "4"]],
    "air10.py": [["air10.txt"], ["cat air10.txt"], ["a.txt"]],
    "air11.py": [[0, 5], ["a", "b"]],
    "air12.py": [[6, 5, 4, 3, 2, 1], ["a", "b", "c", "d", "e"]],
=======
## utilisation de tuples et de tableaux pour encadrer les arguments et les sorties attendues. 
scripts_list = {
    "air00.py": [(["Bonjour les gars"], "Bonjour\nles\ngars"), 
                 ([], "Error: One argument is required")],
    "air01.py": [(["crevette"], "Error: Exactly Two arguments are required"), 
                 (["salut tout le monde", "le"], "salut tout \n monde")],
    "air02.py": [(["je", "teste", "des", "trucs", " "], "je teste des trucs"), 
                 ([10, "Je"], 'Error: Not enough arguments')],
    "air03.py": [([1, 2, 3, 4, 5, 4, 3, 2, 1], "5 \n"), 
                 (["bonjour", "monsieur", "bonjour"], "monsieur \n"), 
                 (["b", "b", "o", "o", "n", "n", "j", "j", "o", "o", "u", "u", "r", "r"], 'Error: Nothing unique in here.')],
    "air04.py": [(["Hello milady,  bien ou quoi ??"], "Helo milady, bien ou quoi ?"), 
                 ([10, 11, 12], 'Error: Only one argument is required')],
    "air05.py": [([1, 2, 3, 4, 5, "+2"], "3 4 5 6 7"), 
                 ([10, 20, 30, 40, 50, "-5"], "5 15 25 35 45"), 
                 (["bonjour"], 'Error: Not enough arguments.')],
    "air06.py": [(["Michel", "Albert", "Thérèse", "Benoit", "t"], "Michel"),
                 (["Michael"], 'Error: not enough arguments provided'),
                 (["Paris", "Rabat", "St-Denis", "Tokyo", "io"], "Rabat")],
    "air07.py": [([1, 3, 4, 2], "1 2 3 4"),
                 (["a", "b", "e", "c", "d"],'Error: arguments have to be numbers'), 
                 ([10, 20, 30, 50, 40, 60, 70, 25], "10 20 25 30 40 50 60 70")],
    "air08.py": [(["10", "20", "30", "fusion", "15", "25", "35"], "10 15 20 25 30 35"),
                 (["fusion", "fusion"], 'Error: both arrays must have at least one number')],
    "air09.py": [(["Michel", "Albert", "Thérèse", "Benoit"], "Albert Thérèse Benoit Michel"),
                 (["1", "2", "3", "4"], 'Error: all arguments must be words (letters only)')],
    "air10.py": [
    (["air10.txt"], 
     "Je danse le MIA, \n"
     "pas de pacotilles \n"
     "Chemise ouverte, chaîne en or qui brille. \n"
     "Des gestes lents, ils prenaient leur temps pour enchaîner \n"
     "Les passes qu'ils avaient élaborées dans leur quartier \n"
     "C'était vraiment trop beau Un mec assurait, \n"
     "tout le monde criait 'ah oui minot !!'\n"),
    (["lexique.txt"], 
     "Pwd: voir l'arborescence\n"
     "Ls: liste; ls -la: liste détaillée (avec les fichiers cachés)\n"
     "Cd: change directory, changer de répertoire\n"
     "Cd ..: revenir au chemin précédent\n"
     "Mkdir: créer un dossier \n"
     "Touch : crée un fichier (avec extension) \n"
     "Mv: bouger un fichier <mv \"fichier à bouger\" \"le dossier où je veux bouger\"/> \n"
     "Cp: copier-coller un fichier (cp \"fichier\" \"dossier\"/) \n"
     "Cp -r: copier-coller un dossier <Si dans le même répertoire cp (-r) fichier (dossier) renommer le fichier (dossier)> \n"
     "Rm: supprimer un fichier \n"
     "Rm -r: supprime un dossier \n"
     "Command -c: liste des différentes commandes disponible \n"
     "Man : manuel (navigue avec flèches, quitter avec q) décrit les commandes disponibles \n"
     "Cat: lire le contenu d'un fichier \n"
     "Less: lire le contenu du fichier dans un autre format (cf man) \n"
     "File: renseigne le type de donnée du fichier\n"),
    (["a.txt"], 'Error: a.txt not found in directories')],
    "air11.py": [([0, 5], "0\n0 0 0\n0 0 0 0 0\n0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0"),
                 (["a", "b"], 'Error: Second argument must be the number of rows')],
    "air12.py": [([6, 5, 4, 3, 2, 1], "1 2 3 4 5 6"),
                 (["a", "b", "c", "d", "e"], 'Error: only numbers needed')]
>>>>>>> Stashed changes
}

# ANSI colors for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

<<<<<<< Updated upstream
def check_and_print_result(script, idx, total_tests, result):
    if result:
=======
def check_and_print_result(script, idx, total_tests, result, expected_output):
    if result and result.returncode == 0 and result.stdout.strip() == expected_output.strip():
>>>>>>> Stashed changes
        print(f"{script} ({idx}/{total_tests}) : {GREEN}success{RESET}")
        return True
    else:
        print(f"{script} ({idx}/{total_tests}) : {RED}failed{RESET}")
<<<<<<< Updated upstream
=======
        if result:
            print(f"Expected: {expected_output.strip()}")
            print(f"Got: {result.stdout.strip()}")
>>>>>>> Stashed changes
        return False

def execute_scripts(scripts):
    total_tests = 0
    total_success = 0

    for script, test_cases in scripts.items():
<<<<<<< Updated upstream
        for idx, arguments in enumerate(test_cases, start=1):
=======
        for idx, (arguments, expected_output) in enumerate(test_cases, start=1):
>>>>>>> Stashed changes
            try:
                result = subprocess.run(
                    ["python3", script] + [str(arg) for arg in arguments],
                    capture_output=True,
                    text=True
                )
<<<<<<< Updated upstream
                success = (result.returncode == 0)
                if check_and_print_result(script, idx, len(test_cases), success):
                    total_success += 1
            except Exception as e:
                print(f"Error in {script}: {e}")
                check_and_print_result(script, idx, len(test_cases), False)
=======
                
                if check_and_print_result(script, idx, len(test_cases), result, expected_output):
                    total_success += 1
            except Exception as e:
                print(f"Error in {script}: {e}")
                check_and_print_result(script, idx, len(test_cases), None, expected_output)
>>>>>>> Stashed changes
            total_tests += 1

    print(f"Total success: ({total_success}/{total_tests})")

if __name__ == "__main__":
    execute_scripts(scripts_list)
