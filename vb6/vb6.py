
from antlr4 import *
import argparse 

# Import generated lexer and parser
from VisualBasic6Lexer import VisualBasic6Lexer
from VisualBasic6Parser import VisualBasic6Parser
from VisualBasic6ParserListener import VisualBasic6ParserListener


# Create a custom listener by subclassing the generated base listener
class MyListener(VisualBasic6ParserListener):

    def enterFunctionStmt(self, ctx):
        print("FUNC:", ctx.getText())

    def enterModuleHeader(self,ctx):
        print("Module:", ctx.getText())

    def enterModuleConfig(self,ctx):
        print("Module Config:", ctx.getText())



def read_file(file_path):
    """Reads the content of a file and returns it as a string.
    
    Args:
        file_path (str): The path to the file to be read.
    
    Returns:
        str: The content of the file as a string.
    
    Raises:
        FileNotFoundError: If the file does not exist at the provided path.
        Exception: If any other error occurs while reading the file.
    
    Notes:
        This function uses the built-in `open()` function to read the content of a file.
        It returns an error message if the file is not found or an error occurs during reading.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"




def main():
    parser = argparse.ArgumentParser(description="Parse VB6 code and extract class, function, and variable information.")
    parser.add_argument("file", help="Path to the input VB6 code file")
    args = parser.parse_args()

    # Create a lexer and parser for your input code
    input_code = read_file(args.file)
    input_stream = InputStream(input_code)
    lexer = VisualBasic6Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = VisualBasic6Parser(stream)

    # Parse the code
    tree = parser.startRule()


    # Create a listener instance and walk the parse tree
    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == "__main__":
    main()