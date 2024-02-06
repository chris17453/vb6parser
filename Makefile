.PHONY: vb6


get-test-code:
	git clone https://github.com/peterson1/vb6-toolbox.git

	
vb6:
# antlr4 has some wildly fucked up directory options...
	@mkdir vb6/temp -p
	@cp definitions/* vb6/temp
	@cd vb6/temp; antlr4 -Dlanguage=Python3  VisualBasic6Lexer.g4 VisualBasic6Parser.g4 
	@cp vb6/temp/*.py vb6
	@rm vb6/temp/* -f
	@rmdir vb6/temp


test-single:
	python vb6/vb6.py "./vb6-toolbox/Dates/GmtDateTime.bas">test/output-single.txt


test-class:
	python vb6/vb6.py "./vb6-toolbox/Data Structures/CollectionWrapper.cls">test/output-class.txt