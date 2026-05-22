ANTLR = antlr4

all: cantorLexer.py cantorParser.py cantorVisitor.py

cantorLexer.py cantorParser.py cantorVisitor.py: cantor.g4
	$(ANTLR) -Dlanguage=Python3 -visitor cantor.g4

.PHONY: clean
clean:
	rm -f cantorLexer.py cantorParser.py cantorVisitor.py cantorListener.py *.interp *.tokens
