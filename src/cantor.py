import sys
import os
from functions import pi, unpi, encode_input, k_1, id, add, mul, diff, fst, snd

from antlr4 import *
from cantorLexer import cantorLexer
from cantorParser import cantorParser
from cantorVisitor import cantorVisitor

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


class EvalVisitor(cantorVisitor):
    def __init__(self, func_defs):
        self.func_defs = func_defs
        self.arg = 0

    def evaluate(self, func_name, arg):
        if func_name in builtins:
            return builtins[func_name](arg)
        if func_name not in self.func_defs:
            print_error(f"Unknown function: {func_name}")
        ctx = self.func_defs[func_name]
        old_arg = self.arg
        self.arg = arg
        result = self.visit(ctx)
        self.arg = old_arg
        return result

    def visitComp(self, ctx):
        g_val = self.evaluate(ctx.ID(1).getText(), self.arg)
        return self.evaluate(ctx.ID(0).getText(), g_val)

    def visitPair(self, ctx):
        f_val = self.evaluate(ctx.ID(0).getText(), self.arg)
        g_val = self.evaluate(ctx.ID(1).getText(), self.arg)
        return pi(f_val, g_val)

    def visitCompair(self, ctx):
        g_val = self.evaluate(ctx.ID(1).getText(), self.arg)
        h_val = self.evaluate(ctx.ID(2).getText(), self.arg)
        return self.evaluate(ctx.ID(0).getText(), pi(g_val, h_val))

    def visitMu(self, ctx):
        f_name = ctx.ID().getText()
        k = 0
        while True:
            if self.evaluate(f_name, pi(self.arg, k)) != 0:
                return k
            k += 1

    def visitPrimrec(self, ctx):
        f_pred = ctx.ID(0).getText()
        g_base = ctx.ID(1).getText()
        h_step = ctx.ID(2).getText()

        s_val = self.evaluate(g_base, 0)
        for i in range(1, self.arg + 1):
            if self.evaluate(f_pred, i) != 0:
                s_val = self.evaluate(g_base, i)
            else:
                s_val = self.evaluate(h_step, pi(s_val, pi(i, 0)))
        return s_val

    def visitAlias(self, ctx):
        return self.evaluate(ctx.ID().getText(), self.arg)


def process_file(filepath, processed=None):
    if processed is None:
        processed = set()

    abspath = os.path.abspath(filepath)
    if abspath in processed:
        return {}, None

    processed.add(abspath)

    try:
        input_stream = FileStream(filepath, encoding='utf-8')
        lexer = cantorLexer(input_stream)
        lexer.removeErrorListeners()
        token_stream = CommonTokenStream(lexer)
        parser = cantorParser(token_stream)
        tree = parser.prog()

        num_errors = parser.getNumberOfSyntaxErrors()
        if num_errors > 0:
            print_error(f"Error: There are {num_errors} sintax errors on the file '{filepath}'.")

    except Exception as e:
        print_error(f"Error: {e} in {filepath}")

    func_defs = {}
    main_func = None
    dir_base = os.path.dirname(abspath)

    # Get main directive
    md = tree.main_directive()
    if md is not None:
        main_func = md.ID().getText()

    # Get import directives
    for id_ in tree.import_directive():
        imp = id_.ID().getText()
        import_path = os.path.join(dir_base, imp + '.cantor')
        imported_defs, _ = process_file(import_path, processed)
        func_defs.update(imported_defs)

    # Get function definitions from lines
    for line in tree.line():
        fd = line.function_def()
        if fd is not None:
            name = fd.ID().getText()
            func_defs[name] = fd.operation()

    return func_defs, main_func


def main():
    if len(sys.argv) < 2:
        usage()

    try:
        script_path = sys.argv[1]
        func_defs, main_func = process_file(script_path)

        if main_func is None:
            print_error("Error: no main function defined")

        user_input = sys.stdin.read().strip()
        arg = encode_input(user_input)
        evaluator = EvalVisitor(func_defs)
        result = evaluator.evaluate(main_func, arg)
        print(result)
    except Exception as e:
        print_error(f"Error: {e}")


if __name__ == '__main__':
    main()
