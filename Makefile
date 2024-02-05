#.phony: 


get-test-code:
	git clone https://github.com/peterson1/vb6-toolbox.git

	
vb6:
	cd vb6; antlr4 -Dlanguage=Python3 VisualBasic6Lexer.g4 VisualBasic6Parser.g4


test-single:
	python vb6/vb6.py "./vb6-toolbox/Dates/GmtDateTime.bas">test/output.txt


test-class:
	python vb6/vb6.py "./vb6-toolbox/Data Structures/CollectionWrapper.cls">test/output.txt