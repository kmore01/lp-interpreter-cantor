all: grammar

grammar: src/cantor.g4
	cd src && antlr4 -Dlanguage=Python3 -no-listener -visitor cantor.g4

clean:
	rm -f src/cantorLexer.py src/cantorParser.py src/cantorVisitor.py src/cantorListener.py src/*.interp src/*.tokens
