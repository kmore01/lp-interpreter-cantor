import sys
import os
from functions import pi, encode_input, k_1, id, add, mul, diff, fst, snd

from antlr4 import *
from cantorLexer import cantorLexer
from cantorParser import cantorParser

builtins = {
    'k_1': k_1,
    'id': id,
    'add': add,
    'mul': mul,
    'diff': diff,
    'fst': fst,
    'snd': snd,
}

def usage():
    print("Usage: python3 cantor.py <script.cantor>")
    sys.exit(1)

def print_error(message):
    print(message)
    sys.exit(1)

class CantorFunctionCollector(ParseTreeVisitor):
    def __init__(self):
        self.functions = {}
        self.main_func = None
        self.imports = []

    def visitMain_directive(self, ctx):
        self.main_func = ctx.ID().getText()

    def visitImport_directive(self, ctx):
        self.imports.append(ctx.ID().getText())

    def visitFunction_def(self, ctx):
        name = ctx.ID().getText()
        op = ctx.operation()

        if isinstance(op, cantorParser.CompOpContext):
            args = ('comp', op.ID(0).getText(), op.ID(1).getText())
        elif isinstance(op, cantorParser.PairOpContext):
            args = ('pair', op.ID(0).getText(), op.ID(1).getText())
        elif isinstance(op, cantorParser.CompairOpContext):
            args = ('compair', op.ID(0).getText(), op.ID(1).getText(), op.ID(2).getText())
        elif isinstance(op, cantorParser.MuOpContext):
            args = ('mu', op.ID().getText())
        elif isinstance(op, cantorParser.PrimrecOpContext):
            args = ('primrec', op.ID(0).getText(), op.ID(1).getText(), op.ID(2).getText())
        elif isinstance(op, cantorParser.AliasOpContext):
            args = (op.ID().getText(),)

        self.functions[name] = args

def process_file(filepath, processed=None):
    if processed is None:
        processed = set()

    abspath = os.path.abspath(filepath)
    if abspath in processed:
        return {}, None

    processed.add(abspath)

    try:
        with open(filepath) as f:
            text = f.read()

        lexer = cantorLexer(InputStream(text))
        stream = CommonTokenStream(lexer)
        parser = cantorParser(stream)
        tree = parser.prog()
    except Exception:
        print_error(f"Error: could not parse {filepath}")

    visitor = CantorFunctionCollector()
    visitor.visit(tree)

    dir_base = os.path.dirname(abspath)
    all_functions = {}
    for imp in visitor.imports:
        import_path = os.path.join(dir_base, imp + '.cantor')
        imported_funcs, _ = process_file(import_path, processed)
        all_functions.update(imported_funcs)

    all_functions.update(visitor.functions)
    return all_functions, visitor.main_func

def evaluate(func_name, arg, functions):
    if func_name in builtins:
        return builtins[func_name](arg)

    if func_name not in functions:
        print_error(f"Unknown function: {func_name}")

    args = functions[func_name]

    if len(args) == 1:
        if args[0] in builtins:
            return builtins[args[0]](arg)
        elif args[0] in functions:
            return evaluate(args[0], arg, functions)

    if args[0] == 'comp':
        return evaluate(args[1], evaluate(args[2], arg, functions), functions)
    elif args[0] == 'pair':
        return pi(evaluate(args[1], arg, functions), evaluate(args[2], arg, functions))
    elif args[0] == 'compair':
        return evaluate(args[1], pi(evaluate(args[2], arg, functions),
                                    evaluate(args[3], arg, functions)),
                                    functions)
    elif args[0] == 'mu':
        k = 0
        while True:
            if evaluate(args[1], pi(arg, k), functions) != 0:
                return k
            k += 1
    elif args[0] == 'primrec':
        f_pred = args[1]
        g_base = args[2]
        h_step = args[3]
        
        s_val = evaluate(g_base, 0, functions)
        s_tuple = s_val
        for i in range(1, arg + 1):
            if evaluate(f_pred, i, functions) != 0:
                s_val = evaluate(g_base, i, functions)
            else:
                s_val = evaluate(h_step, pi(s_val, pi(i, 0)), functions)
            s_tuple = pi(s_val, s_tuple)
        return s_val
    else:
        print_error(f"Unknown operation: {args[0]}")

def main():
    if len(sys.argv) < 2:
        usage()

    try:
        script_path = sys.argv[1]
        functions, main_func = process_file(script_path)

        if main_func is None:
            print_error("Error: no main function defined")

        user_input = sys.stdin.read().strip()
        arg = encode_input(user_input)
        result = evaluate(main_func, arg, functions)
        print(result)
    except Exception as e:
        print_error(f"Error: {e}")

if __name__ == '__main__':
    main()
