# Cantor Interpreter

An interpreter for the **Cantor** language, a minimal functional programming language based on **Cantor pairing functions** and **recursive function theory**. Built for the *Programming Languages* course at Universitat de Barcelona.

## Description

Cantor is a tiny language where all data is encoded as natural numbers using the **Cantor pairing function**. Lists and tuples are represented via nested pairs, and the empty list is represented as `0`. Programs define recursive functions using a small set of combinators:

- **`comp`** — function composition
- **`pair`** — pairing two functions
- **`compair`** — compose with pair (shortcut for `comp f (pair g h)`)
- **`mu`** — minimalization (µ-recursion)
- **`primrec`** — primitive recursion

Scripts have a `.cantor` extension, read input from stdin, and write the result to stdout.

## Requirements

- **Python 3.10+**
- **ANTLR 4.9.2** (for grammar-based parsing)
  - Java runtime (for the ANTLR tool)
  - Python runtime: `antlr4-python3-runtime`

### Installing ANTLR

**Ubuntu / Debian:**

```bash
sudo apt install antlr4
pip install antlr4-python3-runtime
```

**Other systems:**

```bash
pip install antlr4-tools antlr4-python3-runtime
```

## Setup

Clone the repository and generate the ANTLR parser:

```bash
git clone <repo-url>
cd lp
make
```

This runs `antlr4 -Dlanguage=Python3 -visitor cantor.g4` and produces `cantorLexer.py`, `cantorParser.py`, and `cantorVisitor.py`.

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

### Input Format

Input numbers are space-separated on a single line. They are encoded as nested Cantor pairs:

```
a b c   →   π(a, π(b, c))
```

### Output

The interpreter prints a single natural number — the result of applying the `main` function to the encoded input.

## Scripts

| Script | Function | Input | Output |
|---|---|---|---|
| `suma.cantor` | `x + y` | `x y` | sum |
| `anterior.cantor` | `max(0, x-1)` | `x` | predecessor |
| `signe.cantor` | `0 if x=0, 1 otherwise` | `x` | sign |
| `booleans.cantor` | boolean operations | `op x y` | result |
| `relacionals.cantor` | relational operators | `op x y` | 0/1 |
| `add3.cantor` | `x + y + z` | `x y z` | sum |
| `factorial.cantor` | `x!` | `x` | factorial |
| `fibonacci.cantor` | `F(x)` | `x` | Fibonacci number |
| `div.cantor` | `x // y` | `x y` | quotient |
| `mod.cantor` | `x mod y` | `x y` | remainder |
| `cond.cantor` | conditional `if p then a else b` | `p a b` | a or b |
| `max2.cantor` | `max(x, y)` / `min(x, y)` | `x y` | max/min |
| `maxMin.cantor` | `max` / `min` of three numbers | `x y z` | max/min |
| `even.cantor` | `1 if x even, 0 otherwise` | `x` | evenness |

## Language Reference

### Grammar

```antlr
prog: line* EOF;

line
    : directive
    | function_def
    ;

directive
    : 'main' ID
    | 'import' ID
    | 'extended'
    ;

function_def: 'define' ID DOC? operation;

operation
    : 'comp' ID ID          # CompOp
    | 'pair' ID ID          # PairOp
    | 'compair' ID ID ID    # CompairOp
    | 'mu' ID               # MuOp
    | 'primrec' ID ID ID    # PrimrecOp
    | ID                    # AliasOp
    ;
```

### Directives

- **`main <name>`** — declares the entry point function
- **`import <name>`** — imports all functions from another `.cantor` file
- **`extended`** — enables extended mode (reserved)

### Operations

| Operation | Meaning |
|---|---|
| `comp f g` | `f ∘ g` : `f(g(x))` |
| `pair f g` | `⟨f(x), g(x)⟩` |
| `compair f g h` | `f(⟨g(x), h(x)⟩)` (equiv. `comp f (pair g h)`) |
| `mu f` | minimal `k` such that `f(⟨x, k⟩) ≠ 0` |
| `primrec f g h` | primitive recursion |
| `<name>` | alias (single-function body) |

### Built-in Functions

| Name | Function |
|---|---|
| `k_1` | constant 1: `k_1(x) = 1` |
| `id` | identity: `id(x) = x` |
| `add` | addition: `add(⟨x, y⟩) = x + y` |
| `mul` | multiplication: `mul(⟨x, y⟩) = x * y` |
| `diff` | truncated difference: `diff(⟨x, y⟩) = max(0, x - y)` |
| `fst` | first projection: `fst(⟨x, y⟩) = x` |
| `snd` | second projection: `snd(⟨x, y⟩) = y` |

## Running Tests

```bash
python3 run_tests.py
```

This runs all test cases from the `tests/` directory. Each test consists of an `.inp` file (input) and a corresponding `.out` file (expected output).

## Project Structure

```
├── cantor.py          # Main interpreter
├── functions.py       # Pairing functions and built-ins
├── cantor.g4          # ANTLR grammar
├── cantorLexer.py     # Generated lexer
├── cantorParser.py    # Generated parser
├── cantorVisitor.py   # Generated visitor
├── Makefile           # ANTLR generation
├── run_tests.py       # Test runner
├── *.cantor           # Language scripts
└── tests/
    ├── *.inp          # Test inputs
    ├── *.out          # Expected outputs
    └── *.cantor       # Self-contained test scripts
```

## Authors

- **Cristian** — [kmore](https://github.com/kmore)

Built for the *Programming Languages* course (2025–2026) at **Universitat de Barcelona**.

## License

This project is for educational purposes. No license specified.
