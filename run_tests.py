import os
import sys

from cantor import EvalVisitor, process_file
from functions import encode_input


def main():
    ok = total = 0
    failed = []

    for fname in sorted(os.listdir('.')):
        if not fname.endswith('.inp'):
            continue

        base = fname[:-4]
        script = base.rsplit('_', 1)[0] + '.cantor'
        out_file = base + '.out'

        if not os.path.exists(out_file):
            continue

        with open(fname) as f:
            inp = f.read().strip()
        with open(out_file) as f:
            expected = f.read().strip()

        if not os.path.exists(script):
            continue

        try:
            fns, main_func = process_file(script)
            if main_func is None:
                print(f'NO_MAIN {base}')
                continue
            arg = encode_input(inp)
            evaluator = EvalVisitor(fns)
            result = str(evaluator.evaluate(main_func, arg))
        except Exception as e:
            result = f'ERR:{e}'

        total += 1
        if result == expected:
            ok += 1
            print(f'  OK  {base}')
        else:
            print(f'FAIL  {base}: got "{result}", expected "{expected}"')
            failed.append(base)

    print(f'\n{ok}/{total} tests passed')
    if failed:
        print(f'Failed ({len(failed)}): {", ".join(failed)}')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
