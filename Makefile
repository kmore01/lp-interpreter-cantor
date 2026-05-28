all: gramatica

gramatica: cantor.g4
	antlr4 -Dlanguage=Python3 -no-listener -visitor cantor.g4

clean:
	rm -f cantorLexer.py cantorParser.py cantorVisitor.py cantorListener.py *.interp *.tokens