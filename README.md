# Intérprete de Cantor

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![ANTLR 4.9.x](https://img.shields.io/badge/ANTLR-4.9.x-red.svg)](https://www.antlr.org/)
[![License: Educational](https://img.shields.io/badge/license-educational-green.svg)](#licencia)

Intérprete del lenguaje **Cantor**, un lenguaje funcional mínimo basado en las
**funciones de emparejamiento de Cantor** y en la **teoría de funciones
recursivas** (funciones mu-recursivas). Desarrollado para la asignatura de
*Lenguajes de Programación* de la **Universitat Politècnica de Catalunya**.

En Cantor **todos los datos se codifican como números naturales**. Las listas y
las tuplas se representan mediante pares de Cantor anidados, y la lista vacía es
`0`. Los programas definen funciones recursivas con un conjunto reducido de
combinadores inspirados en el formalismo de Kleene.

---

## Características

- **Lenguaje mínimo de combinadores**: solo cinco formas de operación (`comp`,
  `pair`, `compair`, `mu`, `primrec`).
- **Emparejamiento de Cantor**: todas las estructuras de datos se codifican en
  un único número natural.
- **Mu-recursión**: potencia expresiva completa de las funciones recursivas
  generales.
- **Sistema de importaciones**: composición de programas mediante ficheros
  `.cantor`.
- **Comentarios de documentación**: anotaciones `[docs]` en las definiciones.
- **Suite de pruebas automática**: comparación de salidas esperadas.
- **Frontend basado en ANTLR**: gramática declarativa y parser generado.

---

## Requisitos

| Dependencia | Versión | Uso |
|---|---|---|
| Python | 3.10+ | Ejecución |
| antlr4-python3-runtime | 4.9.x | Runtime del parser (obligatorio) |
| ANTLR tool | 4.9.x | Regenerar el parser (opcional) |

Los ficheros generados por ANTLR (`cantorLexer.py`, `cantorParser.py` y
`cantorVisitor.py`) ya están incluidos en `src/`, así que para ejecutar el
intérprete solo hace falta el runtime de Python.

### Instalación del runtime

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install antlr4-python3-runtime==4.9.2
```

### Instalación de la herramienta ANTLR (opcional)

Solo es necesaria si quieres regenerar el parser tras modificar la gramática.

**Ubuntu / Debian:**

```bash
sudo apt install antlr4
```

**macOS (Homebrew):**

```bash
brew install antlr
```

**Otros sistemas:**

```bash
pip install antlr4-tools
```

---

## Puesta en marcha

```bash
git clone <repo-url>
cd lp
python3 -m venv .venv
source .venv/bin/activate
pip install antlr4-python3-runtime==4.9.2
```

Si cambias `src/cantor.g4`, regenera los ficheros del parser:

```bash
make
```

Este comando ejecuta `antlr4 -Dlanguage=Python3 -no-listener -visitor
cantor.g4` dentro de `src/`. Para eliminar los artefactos generados:

```bash
make clean
```

---

## Uso

Ejecuta cualquier programa `.cantor` pasando la entrada por `stdin`:

```bash
echo "3 5" | python3 src/cantor.py examples/suma.cantor
# 8
```

```bash
echo "5" | python3 src/cantor.py examples/factorial.cantor
# 120
```

```bash
echo "7 2" | python3 src/cantor.py examples/mod.cantor
# 1
```

```bash
echo "10" | python3 src/cantor.py examples/fibonacci.cantor
# 55
```

### Formato de entrada

Los números se separan por espacios en una sola línea y se codifican como pares
de Cantor anidados de derecha a izquierda:

```text
a b c   ->   pi(a, pi(b, c))
```

donde `pi(x, y) = ((x + y)(x + y + 1)) / 2 + y` es la función de
emparejamiento de Cantor.

Un único número `x` se pasa directamente como `x`.

### Salida

El intérprete imprime un único número natural: el resultado de aplicar la
función declarada como `main` a la entrada codificada.

---

## Programas de ejemplo

Todos los programas están en `examples/`:

| Programa | Función | Entrada | Salida |
|---|---|---|---|
| `suma.cantor` | `x + y` | `x y` | suma |
| `anterior.cantor` | `max(0, x - 1)` | `x` | predecesor |
| `signe.cantor` | `0 si x = 0, 1 en caso contrario` | `x` | signo |
| `booleans.cantor` | `not(x)` (también define `and` y `or`) | `x` | 0 / 1 |
| `relacionals.cantor` | `neq(x, y)` (también define `eq`, `lt` y `gt`) | `x y` | 0 / 1 |
| `add3.cantor` | `x + y + z` | `x y z` | suma |
| `factorial.cantor` | `x!` | `x` | factorial |
| `fibonacci.cantor` | `F(x)` | `x` | número de Fibonacci |
| `div.cantor` | `x // y` | `x y` | cociente |
| `mod.cantor` | `x mod y` | `x y` | resto |
| `cond.cantor` | condicional `if p then a else b` | `p a b` | `a` o `b` |
| `max2.cantor` | `max(x, y)` / `min(x, y)` | `x y` | máximo o mínimo |
| `maxMin.cantor` | `min(x, y)` (también define `max`) | `x y` | máximo o mínimo |
| `even.cantor` | `1 si x es par, 0 en caso contrario` | `x` | paridad |

---

## Referencia del lenguaje

### Gramática

La fuente está en `src/cantor.g4`:

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

### Directivas

| Directiva | Descripción |
|---|---|
| `main <nombre>` | Declara la función de entrada |
| `import <nombre>` | Importa las funciones de otro fichero `.cantor` (se resuelve respecto al fichero actual) |
| `extended` | Activa el modo extendido (necesario en `relacionals.cantor`, `booleans.cantor`, `cond.cantor`, etc.) |

### Operaciones

| Forma | Significado | Equivalente matemático |
|---|---|---|
| `comp f g` | Composición: `f(g(x))` | `f o g` |
| `pair f g` | Emparejamiento: `⟨f(x), g(x)⟩` | `⟨f, g⟩` |
| `compair f g h` | Composición con par: `f(⟨g(x), h(x)⟩)` | `f o ⟨g, h⟩` |
| `mu f` | Mu-recursión (minimización): menor `k` tal que `f(⟨x, k⟩) ≠ 0` | `mu k. f(⟨x, k⟩) ≠ 0` |
| `primrec f g h` | Recursión primitiva | `base = g(x)`, `paso = h(⟨acc, x⟩)` |
| `<nombre>` | Alias de una función | - |

### Funciones predefinidas

| Nombre | Firma | Descripción |
|---|---|---|
| `k_1` | `k_1(x) = 1` | Constante 1 |
| `id` | `id(x) = x` | Identidad |
| `add` | `add(⟨x, y⟩) = x + y` | Suma |
| `mul` | `mul(⟨x, y⟩) = x * y` | Multiplicación |
| `diff` | `diff(⟨x, y⟩) = max(0, x - y)` | Diferencia truncada |
| `fst` | `fst(⟨x, y⟩) = x` | Primera proyección |
| `snd` | `snd(⟨x, y⟩) = y` | Segunda proyección |

### Semántica de la recursión primitiva

La operación `primrec f g h` funciona así:

1. Si `f(i) ≠ 0` (caso base): resultado = `g(i)`.
2. Si `f(i) = 0` (caso recursivo): resultado = `h(⟨acumulador, i⟩)`.

El acumulador es el resultado del paso anterior (`i - 1`) y comienza en `g(0)`.

### Comentarios de documentación

Las definiciones pueden incluir documentación entre corchetes:

```cantor
define factorial
    [x!]
    primrec is_base k_1 step
```

El intérprete los ignora; sirven como documentación en línea.

---

## Pruebas

La suite incluye 51 casos en `tests/`. Cada entrada `<nombre>_<n>.inp` se
ejecuta contra `examples/<nombre>.cantor` y se compara con
`tests/<nombre>_<n>.out`:

```bash
python3 run_tests.py
```

Salida esperada:

```text
  OK  add3_1
  ...
51/51 tests passed
```

También puedes ejecutar un caso manualmente:

```bash
python3 src/cantor.py examples/suma.cantor < tests/suma_1.inp
diff <(python3 src/cantor.py examples/suma.cantor < tests/suma_1.inp) tests/suma_1.out
```

---

## Estructura del proyecto

```text
.
├── README.md              # Documentación
├── Makefile               # Regeneración del parser ANTLR
├── run_tests.py           # Runner de la suite de pruebas
├── .gitignore
├── src/
│   ├── cantor.py          # Intérprete (EvalVisitor, procesado de ficheros, CLI)
│   ├── functions.py       # Emparejamiento de Cantor y operaciones predefinidas
│   ├── cantor.g4          # Gramática ANTLR
│   ├── cantorLexer.py     # Lexer generado
│   ├── cantorParser.py    # Parser generado
│   └── cantorVisitor.py   # Visitor generado
├── examples/
│   └── *.cantor           # Programas de ejemplo
└── tests/
    ├── *.inp              # Entradas de prueba
    └── *.out              # Salidas esperadas
```

Todos los `.cantor` deben permanecer en el mismo directorio porque las
directivas `import` se resuelven respecto al fichero que las contiene.

---

## Cómo funciona

### Función de emparejamiento de Cantor

La función `pi : N × N -> N` es una biyección que codifica cualquier par de
números naturales como un único número natural:

```text
pi(x, y) = ((x + y)(x + y + 1)) / 2 + y
```

Su inversa `pi^-1(z) = (x, y)` reconstruye el par original. Anidando `pi`,
cualquier tupla `(a_1, a_2, ..., a_n)` se codifica como un solo número:
`pi(a_1, pi(a_2, ... pi(a_n-1, a_n)...))`.

### Modelo de evaluación

1. El parser generado por ANTLR lee un fichero `.cantor` y construye el AST.
2. `process_file()` resuelve las directivas `import` de forma recursiva y crea
   un mapa de nombres de función a nodos del AST.
3. `EvalVisitor` evalúa la función `main` sobre la entrada codificada:
   - **`comp f g`**: evalúa `g(x)` y pasa el resultado a `f`.
   - **`pair f g`**: evalúa `f(x)` y `g(x)`, y codifica el par con `pi`.
   - **`compair f g h`**: evalúa `g(x)` y `h(x)`, los empareja y pasa el par a `f`.
   - **`mu f`**: itera `k = 0, 1, 2, ...` hasta que `f(⟨x, k⟩) ≠ 0`.
   - **`primrec f g h`**: itera de `1` a `x` aplicando la lógica base/paso.

---

## Contribuir

Las contribuciones son bienvenidas. Para cambios importantes, abre antes un
issue para discutir el enfoque.

### Añadir un programa

1. Crea el fichero `.cantor` en `examples/`.
2. Declara la función de entrada con la directiva `main`.
3. Añade los casos de prueba en `tests/` con el formato `<nombre>_<n>.inp` y
   `<nombre>_<n>.out`.

---

## Autores

- **Kevin** - [kmore01](https://github.com/kmore01)

Proyecto desarrollado para la asignatura de *Lenguajes de Programación*
(2025–2026) en la **Universitat Politècnica de Catalunya**.

---

## Licencia

Proyecto con fines **educativos**. No se especifica una licencia.

---

## Agradecimientos

- Construido con [ANTLR](https://www.antlr.org/).
