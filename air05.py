import sys

def apply_operator(numbers, operator):
    if isinstance(operator, int):
        result = []
        for num in numbers:
            result.append(num + operator)
        return result
    elif isinstance(operator, str) and len(operator) > 1:
        if operator[0] in ['+', '-'] and operator[1:].isdigit():
            op = int(operator)
            result = []
            for num in numbers:
                result.append(num + op)
            return result
    return numbers

<<<<<<< Updated upstream
def handle_error(args):
    if len(args) < 2:
        print('Error: Not enough arguments.')
        sys.exit(1)
    elif not (args[-1].isdigit() or (args[-1][-1] in ['+', '-'] and args[-1][:-1].isdigit())):
        if args[-1][-1] in ['+', '-']:
            if args[-1][:-1].isdigit():
                return args[:-1], args[-1][-1], int(args[-1][:-1])
        elif args[-1][0] in ['+', '-']:
            if args[-1][1:].isdigit():
                return args[:-1], args[-1][0], int(args[-1][1:])
    elif args[-2] not in ['+', '-']:
        print('Error: Second to last argument must be "+" or "-".')
        sys.exit(1)
    elif not all(arg.isdigit() for arg in args[:-1]):
        print('Error: All other arguments must be integers.')
        sys.exit(1)
    else:
        return args[:-1], args[-1], 0 

def parse_arguments(args):
    handle_error(args)
=======
def validate_arguments(args):
    if len(args) < 2:
        print('Error: Not enough arguments.')
        sys.exit(1)

    if not all(arg.isdigit() for arg in args[:-1]):
        print('Error: All arguments except the last one must be integers.')
        sys.exit(1)

    last_args = args[-1]
    if not (last_args.isdigit() or (last_args[0] in ['+', '-'] and last_args[1:].isdigit())):
        print('Error: Operator must be valid integer with sign.')
        sys.exit(1)

def parse_arguments(args):
    validate_arguments(args)
>>>>>>> Stashed changes
    numbers = [int(arg) for arg in args[:-1]]
    operator = args[-1]
    return numbers, operator

<<<<<<< Updated upstream
def solving():
=======
def main():
>>>>>>> Stashed changes
    args = sys.argv[1:]
    numbers, operator = parse_arguments(args)
    result = apply_operator(numbers, operator)
    print(' '.join(map(str, result)))

<<<<<<< Updated upstream
solving()
=======
if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
