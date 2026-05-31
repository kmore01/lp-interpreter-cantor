# Cantor Interpreter

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![ANTLR 4.9](https://img.shields.io/badge/ANTLR-4.9-red.svg)](https://www.antlr.org/)
[![License: Educational](https://img.shields.io/badge/license-educational-green.svg)](LICENSE)

An interpreter for the **Cantor** language - a minimal functional programming language based on **Cantor pairing functions** and **recursive function theory** (μ-recursive functions). Built for the *Programming Languages* course at **Universitat Politècnica de Catalunya**.

In Cantor, **all data is encoded as natural numbers**. Lists and tuples are represented via nested Cantor pairs, and the empty list is `0`. Programs define recursive functions using a small set of combinators inspired by Kleene's formalism of recursive functions.

---

## Features

- **Tiny combinator-based language** - only 5 operation forms (`comp`, `pair`, `compair`, `mu`, `primrec`)
- **Cantor pairing** - all data structures encoded as single natural numbers
- **µ-recursion** - full expressive power of general recursive functions
- **Import system** - compose programs by importing other `.cantor` files
- **Documentation comments** - inline `[docs]` on function definitions
- **Manual testing** - each script can be tested via stdin pipes
- **ANTLR-based parsing** - clean, maintainable grammar-driven frontend

---

## Requirements

| Dependency | Version | Purpose |
|---|---|---|
| Python | 3.10+ | Runtime |
| ANTLR tool | 4.9.x | Grammar compilation (`antlr4`) |
| antlr4-python3-runtime | matching 4.9.x | Python runtime library |

### Installing ANTLR

**Ubuntu / Debian:**

```bash
sudo apt install antlr4
pip install antlr4-python3-runtime
```

**macOS (Homebrew):**

```bash
brew install antlr
pip install antlr4-python3-runtime
```

**Other systems (via pip):**

```bash
pip install antlr4-tools antlr4-python3-runtime
```

---

## Setup

```bash
git clone <repo-url>
cd lp-interpreter-cantor
make
```

This runs `antlr4 -Dlanguage=Python3 -no-listener -visitor cantor.g4`, generating:

- `cantorLexer.py` - lexer
- `cantorParser.py` - parser
- `cantorVisitor.py` - AST visitor

---

## Usage

Run any `.cantor` script by passing input through stdin:

```bash
echo "3 5" | python3 cantor.py suma.cantor
# Output: 8
```

```bash
echo "5" | python3 cantor.py factorial.cantor
# Output: 120
```

```bash
echo "7 2" | python3 cantor.py mod.cantor
# Output: 1
```

```bash
echo "10" | python3 cantor.py fibonacci.cantor
# Output: 55
```

### Input Format

Input numbers are space-separated on a single line. They are encoded as nested Cantor pairs from right to left:

```
a b c   →   π(a, π(b, c))
```

Where `π(x, y) = ((x + y)(x + y + 1))/2 + y` is the Cantor pairing function.

A single number `x` is passed directly as `x`.

### Output

The interpreter prints a single natural number - the result of applying the `main` function to the encoded input.

---

## Scripts

| Script | Function | Input | Output |
|---|---|---|---|
| `suma.cantor` | `x + y` | `x y` | sum |
| `anterior.cantor` | `max(0, x - 1)` | `x` | predecessor |
| `signe.cantor` | `0 if x = 0, 1 otherwise` | `x` | sign |
| `booleans.cantor` | boolean operations (not, and, or) | `op x y` | result |
| `relacionals.cantor` | relational operators (eq, lt, le, gt, ge) | `op x y` | 0 / 1 |
| `add3.cantor` | `x + y + z` | `x y z` | sum |
| `factorial.cantor` | `x!` | `x` | factorial |
| `fibonacci.cantor` | `F(x)` | `x` | Fibonacci number |
| `div.cantor` | `x // y` | `x y` | quotient |
| `mod.cantor` | `x mod y` | `x y` | remainder |
| `cond.cantor` | conditional `if p then a else b` | `p a b` | a or b |
| `max2.cantor` | `max(x, y)` / `min(x, y)` | `x y` | max or min |
| `maxMin.cantor` | `max` / `min` of three numbers | `x y z` | max or min |
| `even.cantor` | `1 if x even, 0 otherwise` | `x` | evenness |

---

## Language Reference

### Grammar

```antlr
grammar cantor;

prog: NL* main_directive NL* extended_directive? import_directive* line* EOF;

line
    : function_def
    | NL
    ;

main_directive: 'main' ID NL?;
import_directive: 'import' ID NL?;
extended_directive: 'extended' NL?;

function_def: 'define' ID NL? DOC? NL* operation NL?;

operation
    : 'comp' ID ID        # Comp
    | 'pair' ID ID        # Pair
    | 'compair' ID ID ID  # Compair
    | 'mu' ID             # Mu
    | 'primrec' ID ID ID  # Primrec
    | ID                  # Alias
    ;

DOC: '[' ~[\r\n\]]* ']';
COMMENT: '#' ~[\r\n]* -> skip;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NL: '\r'? '\n';
WS: [ \t]+ -> skip;
LEXICAL_ERROR : . ;
```

### Directives

| Directive | Description |
|---|---|
| `main <name>` | Declares the entry-point function |
| `import <name>` | Imports all functions from another `.cantor` file (resolved relative to current file) |
| `extended` | Enables extended mode (needed for `relacionals.cantor`, `booleans.cantor`, `cond.cantor`, etc.) |

### Operations

| Form | Meaning | Mathematical equivalent |
|---|---|---|
| `comp f g` | Composition: `f(g(x))` | `f ∘ g` |
| `pair f g` | Pairing: `⟨f(x), g(x)⟩` | `⟨f, g⟩` |
| `compair f g h` | Compose with pair: `f(⟨g(x), h(x)⟩)` | `f ∘ ⟨g, h⟩` |
| `mu f` | µ-recursion (minimalization): smallest `k` such that `f(⟨x, k⟩) ≠ 0` | `µk.f(⟨x, k⟩) ≠ 0` |
| `primrec f g h` | Primitive recursion | `base = g(x)`, `step = h(⟨acc, x⟩)` |
| `<name>` | Alias: single-function body | - |

### Built-in Functions

| Name | Signature | Description |
|---|---|---|
| `k_1` | `k_1(x) = 1` | Constant 1 |
| `id` | `id(x) = x` | Identity |
| `add` | `add(⟨x, y⟩) = x + y` | Addition |
| `mul` | `mul(⟨x, y⟩) = x * y` | Multiplication |
| `diff` | `diff(⟨x, y⟩) = max(0, x - y)` | Truncated difference |
| `fst` | `fst(⟨x, y⟩) = x` | First projection |
| `snd` | `snd(⟨x, y⟩) = y` | Second projection |

### Primitive Recursion Semantics

The `primrec f g h` operation works as follows:

1. If `f(i) ≠ 0` (base case): result = `g(i)`
2. If `f(i) = 0` (recursive case): result = `h(⟨accumulator, i⟩)`

The accumulator is the result from the previous step (`i - 1`), starting with `g(0)`.

### Documentation Comments

Function definitions can include documentation comments in square brackets:

```cantor
define factorial
    [x!]
    primrec is_base k_1 step
```

These are ignored by the interpreter but serve as inline documentation.

---

## Testing

Test each script by redirecting the `.inp` file as input and comparing with the `.out` file:

```bash
python3 cantor.py suma.cantor < suma_1.inp > output.txt
diff output.txt suma_1.out
```

No output from `diff` means the test passed.

---

## Project Structure

```
├── cantor.py              # Main interpreter (EvalVisitor, file processor, CLI)
├── functions.py           # Cantor pairing functions and built-in operations
├── cantor.g4              # ANTLR grammar definition
├── Makefile               # ANTLR grammar compilation
├── README.md              # This file
├── *.cantor               # Cantor language scripts
└── *.{inp,out}            # Test inputs (inp) and expected outputs (out)
```

---

## How It Works

### Cantor Pairing Function

The Cantor pairing function `π : ℕ × ℕ → ℕ` is a bijection that encodes any pair of natural numbers as a single natural number:

```
π(x, y) = ((x + y)(x + y + 1)) / 2 + y
```

Its inverse `π⁻¹(z) = (x, y)` reconstructs the original pair. By nesting `π`, any tuple `(a₁, a₂, ..., aₙ)` can be encoded as a single number: `π(a₁, π(a₂, ... π(aₙ₋₁, aₙ)...))`.

### Evaluation Model

1. The ANTLR-generated parser reads a `.cantor` file and produces an AST
2. `process_file()` resolves `import` directives recursively and builds a mapping of function names to their AST nodes
3. `EvalVisitor` evaluates the `main` function against the encoded input:
   - **`comp f g`** - evaluates `g(x)`, passes result to `f`
   - **`pair f g`** - evaluates `f(x)` and `g(x)`, encodes the pair via `π`
   - **`compair f g h`** - evaluates `g(x)` and `h(x)`, pairs them, passes to `f`
   - **`mu f`** - iterates `k = 0, 1, 2, ...` until `f(⟨x, k⟩) ≠ 0`
   - **`primrec f g h`** - iterates from `1` to `x`, applying base/step logic

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

### Adding a new script

1. Create your `.cantor` file in the main directory
2. Define a `main` function via the `main` directive
3. Add test cases in the main directory

---

## Authors

- **Kevin** - [kmore01](https://github.com/kmore01)

Built for the *Programming Languages* course (2025–2026) at **Universitat Politècnica de Catalunya**.

---

## License

This project is for **educational purposes**. No license specified.

---

## Acknowledgments

- Built with [ANTLR](https://www.antlr.org/) parser generator
