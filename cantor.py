import sys
import os
from functions import pi, encode_input, k_1, id, add, mul, diff, fst, snd

builtins = {
    'k_1': k_1,
    'id': id,
    'add': add,
    'mul': mul,
    'diff': diff,
    'fst': fst,
    'snd': snd,
}

# Function to print how to use the program
def usage():
    print("Usage: python3 cantor.py <script.cantor>")
    sys.exit(1)

# Function that prints an error message 
def print_error(message):
    print(message)
    sys.exit(1)

# Function to process files (.cantor) 
def process_file(filepath, processed=None):
    if processed is None:
        processed = set()

    abspath = os.path.abspath(filepath)
    if abspath in processed:
        return {}, None

    processed.add(abspath)

    with open(filepath) as f:
        lines = f.readlines()

    functions = {}
    main_func = None
    dir_base = os.path.dirname(abspath)

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Skip comments
        if not line or line.startswith('#') or line.startswith('['):
            i += 1
            continue
        
        # Separate the line into two words
        parts = line.split(maxsplit=1)
        if not parts:
            i += 1
            continue

        if parts[0] == 'main':
            main_func = parts[1]

        elif parts[0] == 'extended':
            pass

        elif parts[0] == 'import':
            import_name = parts[1]
            import_path = os.path.join(dir_base, import_name + '.cantor')
            imported_funcs, _ = process_file(import_path, processed)
            functions.update(imported_funcs)

        elif parts[0] == 'define':
            name = parts[1]
            i += 1
            while i < len(lines):
                line = lines[i].strip()
                if not line or line.startswith('#') or line.startswith('['):
                    i += 1
                else:
                    break
            if i < len(lines):
                body = lines[i].strip().split()
                # Save all the tuple
                functions[name] = tuple(body)

        i += 1

    return functions, main_func

# Function to evaluate the inputs
def evaluate(func_name, arg, functions):
    if func_name in builtins:
        return builtins[func_name](arg)

    if func_name not in functions:
        print_error(f"Unknown function: {func_name}")

    args = functions[func_name]

    if args[0] == 'comp':
        return evaluate(args[1], evaluate(args[2], arg, functions), functions)
    elif args[0] == 'pair':
        return pi(evaluate(args[1], arg, functions), evaluate(args[2], arg, functions))
    # compair f g h = comp f (pair g h)
    elif args[0] == 'compair':
        return evaluate(args[1], pi(evaluate(args[2], arg, functions), 
                                    evaluate(args[3], arg, functions)),
                                    functions)
    # mu f = [k | f(<x.k>) != 0 and k is minimal]
    elif args[0] == 'mu':
        k = 0
        while True:
            if evaluate(args[1], pi(arg, k), functions) != 0:
                return k
            k += 1
    # primrec f g h: compute s(x) computing s(0)...s(x)
    elif args[0] == 'primrec':
        f_pred = args[1] # is_base_case? predicate
        g_base = args[2] # base_case function
        h_step = args[3] # recursive_case function

        s_val = evaluate(g_base, 0, functions) # s(0)
        s_tuple = s_val
        for i in range(1, arg + 1):
            # Base case
            if evaluate(f_pred, i, functions) != 0:
                s_val = evaluate(g_base, i, functions)
            # Recursive case
            else:
                s_val = evaluate(h_step, pi(s_val, pi(i, 0)), functions)
            s_tuple = pi(s_val, s_tuple)
        return s_val # !!!
    elif args[0] == 'cond':
    # cond p a b: if p(arg) != 0 then a(arg) else b(arg)
        p_func = args[1]
        a_func = args[2]
        b_func = args[3]
        if evaluate(p_func, arg, functions) != 0:
            return evaluate(a_func, arg, functions)
        else:
            return evaluate(b_func, arg, functions)
    else:
        print_error(f"Unknown operation: {args[0]}")

# Main program
def main():
    if len(sys.argv) < 2:
        usage()

    script_path = sys.argv[1]
    functions, main_func = process_file(script_path)

    if main_func is None:
        print_error("Error: no main function defined")

    input = sys.stdin.read().strip()
    arg = encode_input(input)
    result = evaluate(main_func, arg, functions)
    print(result)

if __name__ == '__main__':
    main()