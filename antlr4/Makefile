build: PrototypeLexer.g4 PrototypeParser.g4
	antlr4 -visitor -Dlanguage=Python3 -o .antlr PrototypeLexer.g4 PrototypeParser.g4
	cp .antlr/*.py ../prototype/parser
