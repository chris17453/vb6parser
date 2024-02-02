#.phony: 

	
vb6:
	cd vb6; antlr4 -Dlanguage=Python3 VisualBasic6Lexer.g4 VisualBasic6Parser.g4


run:
#	python vb6/vb6.py "/home/nd/repos/vb6-toolbox/Data Structures/CollectionWrapper.cls"
	python vb6/vb6.py "/home/nd/repos/vb6-toolbox/Dates/GmtDateTime.bas">l