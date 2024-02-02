#***********************************************************************************************************************
# 
# ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓███████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓███████▓▒░▒▓████████▓▒░▒▓███████▓▒░  
# ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
#  ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
#  ░▒▓█▓▒▒▓█▓▒░░▒▓███████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  
#   ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
#   ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
#    ░▒▓██▓▒░  ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
#                                                                                                                       
# Author: Chris Watkins
# Date: 01-30-2024 
#***********************************************************************************************************************                                                     
from antlr4 import *
import argparse 
import inspect 
from pprint import pprint
# Import generated lexer and parser
from VisualBasic6Lexer import VisualBasic6Lexer
from VisualBasic6Parser import VisualBasic6Parser
from VisualBasic6ParserListener import VisualBasic6ParserListener

def get_function_name():
    # get the frame object of the function
    frame = inspect.currentframe()
    return frame.f_code.co_name

def dump(obj):
    for attr in dir(obj):
        # Skip built-in attributes
        if attr.startswith('__') and attr.endswith('__'):
            continue

        try:
            value = getattr(obj, attr)
            print(f"obj.{attr} = {repr(value)}")
            print("-------------------------------------------")
        except Exception as e:
            print(f"Error accessing obj.{attr}: {e}")

    print("===========================================")

def info(layer,ctx,depth):
    pad=' '*depth
    if layer=="enter":
        prefix="{"
    else:
        return
        prefix="}"
    start=ctx.start.tokenIndex
    stop=ctx.stop.tokenIndex,
    rule=ctx.getRuleIndex()
    scope=""
    name=""
    try:
        scope=ctx.get_scope()
    except:
        pass
    try:
        name=ctx.get_function_name()
    except:
        pass
    print("*************")
    print(f"{pad}{prefix} {scope} - {name} token:{start} - {stop} : Rule:{rule}")
    print("Text:",ctx.getText())    



class gardner:
    def __init__(self):
        self.data={'root':{}}
        self.scope=[]
        self.fragment={}
        self.rescope=None
        self.scope_type=None
        self.scope_depth=None

    def expect(self,scope_type,depth):
        if scope_type=="func":
            self.rescope=True
        self.scope_depth=depth
        self.scope_type=scope_type
    
    def add_scope(self,name):
        self.scope.append(name)

    def get_scope(self,append=None):
        if append:
            scope=self.scope.copy()
            scope.append(append)
            return ".".join(scope)
        return ".".join(self.scope)
         
 
    def get_obj(self,scope):
        cur_obj=self.data['root']
        if len(scope)>0 and scope !="":
            path=scope.split(".")
        
            for part in path:
                    if 'vars' in cur_obj and part in cur_obj['vars']:
                        cur_obj=cur_obj['vars'][part]
                    elif 'ret' in cur_obj and part in cur_obj['ret']:
                        cur_obj=cur_obj['ret'][part]
                    elif 'args' in cur_obj and part in cur_obj['args']:
                        cur_obj=cur_obj['args'][part]
                    elif 'func' in cur_obj and part in cur_obj['func']:
                        cur_obj=cur_obj['func'][part]
                    elif 'class' in cur_obj and part in cur_obj['class']:
                        cur_obj=cur_obj['class'][part]
                    else:
                        print(self.data)
                        print (f"Cant find {part}")
                        exit()

        return cur_obj

    def add_class(self,scope,name):
        obj=self.get_obj(scope)
        if 'class' not in obj:
            obj['class']={}

        obj['class'][name]={'name':name,
                    'type':'class'}
    
    def add_func(self,scope,name,start=None,end=None,column=None):
        obj=self.get_obj(scope)
        if 'func' not in obj:
            obj['func']={}

        obj['func'][name]={'name':name,'start':start,'end':end,'col':column}

    def add_var(self,scope,name):
        obj=self.get_obj(scope)
        if 'vars' not in obj:
            obj['vars']={}

        obj['vars'][name]={'name':name}


    def add_ret(self,scope,value):
        obj=self.get_obj(scope)
        if 'ret' not in obj:
            obj['ret']=[]

        obj['ret'].append(value)

    def add_arg(self,scope,arg,default=None,has_default=False,as_type=None,optional=None,type_hint=None):
        obj=self.get_obj(scope)
        item={'name':arg,'has_default':has_default,'scope':scope,'optional':optional,'as_type':as_type,'type_hint':type_hint}
        if has_default==True:
            item['default']=default
        if 'args' not in obj:
            obj['args']={}

        obj['args'][arg]=item


# Create a custom listener by subclassing the generated base listener
class MyListener(VisualBasic6ParserListener):
    depth=0
    tree=gardner()

    
    # Enter a parse tree produced by VisualBasic6Parser#startRule.\t\t
    #def enterStartRule(self, ctx:VisualBasic6Parser.StartRuleContext):
    #    self.depth += 1
    #    info("enter", ctx, self.depth)
#
    ## Exit a parse tree produced by VisualBasic6Parser#startRule.
    #def exitStartRule(self, ctx:VisualBasic6Parser.StartRuleContext):
    #    self.depth -= 1
    #    info("exit", ctx, self.depth)

    # Enter a parse tree produced by VisualBasic6Parser#functionStmt.
    def enterFunctionStmt(self, ctx:VisualBasic6Parser.FunctionStmtContext):
        self.depth += 1
        ambiguousIdentifier = ctx.ambiguousIdentifier()
        if ambiguousIdentifier !=None:
            ambiguousIdentifier = ambiguousIdentifier.getText()
            scope=self.tree.get_scope()
            self.tree.add_scope(ambiguousIdentifier)
            self.tree.add_func(scope,ambiguousIdentifier)
        else:
            print("$$$IDK")
        info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#functionStmt.
    def exitFunctionStmt(self, ctx:VisualBasic6Parser.FunctionStmtContext):
        self.depth -= 1
        try:
            name=self.tree.scope.pop()        
            info("exit", ctx, self.depth)
        except:
            print("WOW")


    # Enter a parse tree produced by VisualBasic6Parser#arg.
    def enterArg(self, ctx:VisualBasic6Parser.ArgContext):
        self.depth += 1


        ambiguousIdentifier = ctx.ambiguousIdentifier()
        OPTIONAL = ctx.OPTIONAL()
        PARAMARRAY = ctx.PARAMARRAY()
        typeHint = ctx.typeHint()
        asTypeClause = ctx.asTypeClause()
        argDefaultValue = ctx.argDefaultValue()
        BYVAL = ctx.BYVAL()
        BYREF = ctx.BYREF()

        if ambiguousIdentifier !=None:
            ambiguousIdentifier = ambiguousIdentifier.getText()
        if OPTIONAL !=None:
            OPTIONAL = OPTIONAL.getText()
        if PARAMARRAY !=None:
            PARAMARRAY = PARAMARRAY.getText()
        if typeHint !=None:
            typeHint = typeHint.getText()
        if asTypeClause !=None:
            asTypeClause = asTypeClause.getText()
        if argDefaultValue !=None:
            argDefaultValue = argDefaultValue.getText()
        if BYVAL !=None:
            BYVAL = BYVAL.getText()
        if BYREF !=None:
            BYREF = BYREF.getText()

        print(" PARAMARRAY: ",PARAMARRAY)
        print(" BYVAL: ",BYVAL)
        print(" BYREF: ",BYREF)
        if argDefaultValue:
            has_default=True
        else:
            has_default=None
        scope=self.tree.get_scope()
        self.tree.add_arg(scope,ambiguousIdentifier,default=argDefaultValue,has_default=has_default,optional=OPTIONAL,as_type=asTypeClause,type_hint=typeHint)


        #info("enter", ctx, self.depth)

    # Exit a parse tree produced by VisualBasic6Parser#arg.
    def exitArg(self, ctx:VisualBasic6Parser.ArgContext):
        self.depth -= 1
        info("exit", ctx, self.depth)



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
    pprint(listener.tree.data)


if __name__ == "__main__":
    main()