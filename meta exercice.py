import runpy
import sys

scripts_list = {
    "air00.py": [["Bonjour les gars"], ["23"]],
    "air01.py": [["crevette"], ["salut tout le monde", "le"]],
    "air02.py": [["je", "teste", "des", "trucs"], ["10", "Je"]],
    "air03.py": [[1, 2, 3, 4, 5, 4, 3, 2, 1], ["bonjour", "monsieur", "bonjour"], ["bonjour"]],
    "air04.py": [["Hello milady,  bien ou quoi ??"], ["10", "11", "12"]],
    "air05.py": [[1, 2, 3, 4, 5, "+2"], [10, 20, 30, 40, 50, "-5"], ["bonjour"]],
    "air06.py": [["Michel", "Albert", "Thérèse", "Benoit", "t"], ["Michael", "23"]],
    "air07.py": [[1, 3, 4, 2], ["a", "b", "e", "c", "d"], [10, 20, 30, 40, 50, 60, 70, 25]],
    "air08.py": [["10", "20", "30", "fusion", "15", "25", "35"], ["fusion", "fusion"]],
    "air09.py": [["Michel", "Albert", "Thérèse", "Benoit"], ["1", "2", "3", "4"]],
    "air10.py": [["cat", "air10.txt"], ["cat", "a.txt"]],
    "air11.py": [[0, 5], ["a", "b"]],
    "air12.py": [[6, 5, 4, 3, 2, 1], ["a", "b", "c", "d", "e"]],
}

# ANSI colors pour affichage dans le terminal. 
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def check_and_print_result(script, idx, total_tests, result):
    if result:
        print(f"{script} ({idx}/{total_tests}) : {GREEN}success{RESET}")
        return True
    else:
        print(f"{script} ({idx}/{total_tests}) : {RED}failed{RESET}")
        return False

def error_handling(script, idx, total_tests, error):
    print(f"{script} ({idx}/{total_tests}) : {RED}error{RESET} - {error}")

def execute_scripts(scripts):
    total_tests = 0
    total_success = 0

    for script, test_cases in scripts.items():
        for idx, arguments in enumerate(test_cases, start=1):
            previous_args = sys.argv
            sys.argv = [script] + [str(arg) for arg in arguments] ## utilisation et redirection de sys.argv pour passer les arguments. 

            try:
                runpy.run_path(script, run_name='__main__')
                result = True
            except SystemExit as e:
                result = (e.code == 0)
            except Exception as e:
                result = False
                error_handling(script, idx, len(test_cases), e)

            if check_and_print_result(script, idx, len(test_cases), result):
                total_success += 1

            sys.argv = previous_args  # Reutilisation de sys.argv 
            total_tests += 1

    print(f"Total success: ({total_success}/{total_tests})")

if __name__ == "__main__":
    execute_scripts(scripts_list)
