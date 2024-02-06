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
import xxhash
from utils import file_fragment, dump, find_key_case_insensitive
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
        self.components=['module','class','func','sub','args','vars','ret']

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

    def add_component(self,component):
        if component not in self.components:
            self.components.append(component)

    def get_obj(self,scope):
        cur_obj=self.data['root']
        component=""

        part=""
        if len(scope)>0 and scope !="":
            path=scope.split(".")
            for part in path:
                found=None    
                for component in self.components:
                    if component in cur_obj:
                        if part in cur_obj[component]:
                            cur_obj=cur_obj[component][part]
                            found=True
                            break
                if found==None:
                    print(self.data)
                    print (f"Cant find {part}")
                    exit()
        return cur_obj

    def add_type(self,scope,layer,name,data=None):
        obj=self.get_obj(scope)
        
        # create layer if not found
        if  layer not in obj:
            obj[layer]={}

        # add defaults
        obj[layer][name]={'name':name,
                    'type':layer}
        # add data obj if there is any
        if data:
            obj.update(data)

    def add_module(self,scope,name,data=None):
        self.add_type(scope,'module',name,data)

    def add_class(self,scope,name,data=None):
        self.add_type(scope,'class',name,data)
    
    def add_func(self,scope,name,start=None,end=None,column=None,return_type=None,visibility=None,source=None,file=None):
        obj=self.get_obj(scope)
        if 'func' not in obj:
            obj['func']={}

        source_hash=xxhash.xxh64('xxhash', seed=314159).hexdigest()

        obj['func'][name]={'name':name,'start':start,'end':end,'col':column,'return_type':return_type,'visibility':visibility,'source':source,'scope':scope,'file':file,'hash':source_hash}

    def add_sub(self,scope,name,start=None,end=None,column=None,visibility=None,source=None,file=None):
        obj=self.get_obj(scope)
        if 'sub' not in obj:
            obj['sub']={}
        source_hash=xxhash.xxh64('xxhash', seed=314159).hexdigest()
        obj['sub'][name]={'name':name,'start':start,'end':end,'col':column,'visibility':visibility,'source':source,'scope':scope,'file':file,'hash':source_hash}

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

    # override init, so we can store some stuff
    def __init__(self,source):
        super().__init__()
        self.source=source
        self.depth=0
        self.tree=gardner()

    
    # Enter a parse tree produced by VisualBasic6Parser#startRule.\t\t
    #def enterStartRule(self, ctx:VisualBasic6Parser.StartRuleContext):
    #    self.depth += 1
    #    info("enter", ctx, self.depth)
#
    ## Exit a parse tree produced by VisualBasic6Parser#startRule.
    #def exitStartRule(self, ctx:VisualBasic6Parser.StartRuleContext):
    #    self.depth -= 1
    #    info("exit", ctx, self.depth)


    # Enter a parse tree produced by VisualBasic6Parser#module.
    def enterModule(self, ctx:VisualBasic6Parser.ModuleContext):
        self.depth += 1
        info("entremodule", ctx, self.depth)
        attributes={}
        header={}
        config={}
        options={}

        mh=ctx.moduleHeader()
        if mh:
            mh_version=mh.VERSION()
            mh_class=mh.CLASS()
            mh_version_no=mh.doubleLiteral()
            if mh_version:
                mh_version=mh_version.getText()
            if mh_class:
                mh_class=mh_class.getText()
                header['class']=mh_class
            if mh_version_no:
                mh_version_no=mh_version_no.getText()
                header['version']=mh_version_no

        mc=ctx.moduleConfig()
        if mc:
            config_elements=mc.moduleConfigElement()
            for element in config_elements:
                element_id=element.ambiguousIdentifier().getText()
                element_literal=element.literal().getText()
                config[element_id]=element_literal

            #print(f"Class: {mh_class} - Version: {mh_version} {mh_version_no}")

        mattr=ctx.moduleAttributes()
        if mattr:
            attribs=mattr.attributeStmt()
            #dump(ctx)
            # had to get wonky here. I couldnt find the name splot from the value anywhere..
            if attribs:
                for attrib in attribs:
                    attr=attrib.getText()
                    attr_value=attrib.literal()
                    tokens=attr.split('=')
                    attr_name=tokens[0][9:].strip()
                    attr_value=attr_value[0].getText()
                    attributes[attr_name]=attr_value
                    #print(f"{attr_name}={attr_value}")
        moption=ctx.moduleOptions()
        if moption:
            moptions=moption.moduleOption()
            for option in moptions:
                options[option.getText()]=option.getText()


        data={'attributes':attributes,'header':header,'config':config,'options':options}
        attrib_name_key=find_key_case_insensitive(attributes,'VB_Name')
        if attrib_name_key:
            vb_name=attributes[attrib_name_key].strip("\"'")
            # you never leave this scope.. its cool its the module you're in
            scope=self.tree.get_scope()
            if mh and mh_class.lower()=="class":
                self.tree.add_class(scope,vb_name,data)
            else:
                self.tree.add_module(scope,vb_name,data)
            # decend into the scope
            self.tree.add_scope(vb_name)



    # Exit a parse tree produced by VisualBasic6Parser#module.
    def exitModule(self, ctx:VisualBasic6Parser.ModuleContext):
        self.depth -= 1
       # name=self.tree.scope.pop()        
        info("exit", ctx, self.depth)



    # Enter a parse tree produced by VisualBasic6Parser#functionStmt.
    def enterFunctionStmt(self, ctx:VisualBasic6Parser.FunctionStmtContext):
        self.depth += 1
        ambiguousIdentifier = ctx.ambiguousIdentifier()
        #dump(ctx)
        
        start_line = ctx.start.line
        end_line = ctx.stop.line
        return_type=ctx.asTypeClause().getText()
        return_type=return_type.replace("As ",'').strip()
        
        visibility=ctx.visibility()
        if visibility:
            visibility=visibility.getText()


        if ambiguousIdentifier !=None:
            source=file_fragment(self.source,start=start_line,end=end_line)
            ambiguousIdentifier = ambiguousIdentifier.getText()
            scope=self.tree.get_scope()
            self.tree.add_scope(ambiguousIdentifier)
            self.tree.add_func(scope,ambiguousIdentifier,start=start_line,end=end_line,return_type=return_type,visibility=visibility,source=source,file=self.source)
            scope=self.tree.get_scope()
            ## VB RETURN VARS are the same name as the function name
            self.tree.add_ret(scope,ambiguousIdentifier)
            return_type=return_type

        args=ctx.argList().arg()
        # Iterate over the arguments
        for arg in args:
            #arg = args.arg(i)
            ambiguousIdentifier = arg.ambiguousIdentifier()
            OPTIONAL = arg.OPTIONAL()
            PARAMARRAY = arg.PARAMARRAY()
            typeHint = arg.typeHint()
            asTypeClause = arg.asTypeClause()

            argDefaultValue = arg.argDefaultValue()
            BYVAL = arg.BYVAL()
            BYREF = arg.BYREF()

            if ambiguousIdentifier !=None:
                ambiguousIdentifier = ambiguousIdentifier.getText()
            if OPTIONAL !=None:
                OPTIONAL = OPTIONAL.getText()
                if OPTIONAL=='Optional':
                    OPTIONAL=True
                else: OPTIONAL=None
            if PARAMARRAY !=None:
                PARAMARRAY = PARAMARRAY.getText()
            if typeHint !=None:
                typeHint = typeHint.getText()
            if asTypeClause !=None:
                asTypeClause = asTypeClause.getText()
                asTypeClause = asTypeClause.replace("As ",'').strip()
            if argDefaultValue !=None:
                argDefaultValue = argDefaultValue.getText()
                argDefaultValue = argDefaultValue.replace("=",'').strip()
            if BYVAL !=None:
                BYVAL = BYVAL.getText()
            if BYREF !=None:
                BYREF = BYREF.getText()

            #print(" PARAMARRAY: ",PARAMARRAY)
            #print(" BYVAL: ",BYVAL)
            #print(" BYREF: ",BYREF)
            if argDefaultValue:
                has_default=True
            else:
                has_default=None
            scope=self.tree.get_scope()
            self.tree.add_arg(scope,ambiguousIdentifier,default=argDefaultValue,has_default=has_default,optional=OPTIONAL,as_type=asTypeClause,type_hint=typeHint)
        
    # Exit a parse tree produced by VisualBasic6Parser#functionStmt.
    def exitFunctionStmt(self, ctx:VisualBasic6Parser.FunctionStmtContext):
        self.depth -= 1
        name=self.tree.scope.pop()        
     



    # Enter a parse tree produced by VisualBasic6Parser#subStmt.
    def enterSubStmt(self, ctx:VisualBasic6Parser.SubStmtContext):
        self.depth += 1
        ambiguousIdentifier = ctx.ambiguousIdentifier()
        
        start_line = ctx.start.line
        end_line = ctx.stop.line
        visibility=ctx.visibility()
        if visibility:
            visibility=visibility.getText()

        if ambiguousIdentifier !=None:
            source=file_fragment(self.source,start=start_line,end=end_line)

            ambiguousIdentifier = ambiguousIdentifier.getText()
            scope=self.tree.get_scope()
            self.tree.add_scope(ambiguousIdentifier)
            self.tree.add_sub(scope,ambiguousIdentifier,start=start_line,end=end_line,visibility=visibility,source=source,file=self.source)
    
        


        args=ctx.argList().arg()
        # Iterate over the arguments
        for arg in args:
            #arg = args.arg(i)
            ambiguousIdentifier = arg.ambiguousIdentifier()
            OPTIONAL = arg.OPTIONAL()
            PARAMARRAY = arg.PARAMARRAY()
            typeHint = arg.typeHint()
            asTypeClause = arg.asTypeClause()

            argDefaultValue = arg.argDefaultValue()
            BYVAL = arg.BYVAL()
            BYREF = arg.BYREF()

            if ambiguousIdentifier !=None:
                ambiguousIdentifier = ambiguousIdentifier.getText()
            if OPTIONAL !=None:
                OPTIONAL = OPTIONAL.getText()
                if OPTIONAL=='Optional':
                    OPTIONAL=True
                else: OPTIONAL=None
            if PARAMARRAY !=None:
                PARAMARRAY = PARAMARRAY.getText()
            if typeHint !=None:
                typeHint = typeHint.getText()
            if asTypeClause !=None:
                asTypeClause = asTypeClause.getText()
                asTypeClause = asTypeClause.replace("As ",'').strip()
            if argDefaultValue !=None:
                argDefaultValue = argDefaultValue.getText()
                argDefaultValue = argDefaultValue.replace("=",'').strip()
            if BYVAL !=None:
                BYVAL = BYVAL.getText()
            if BYREF !=None:
                BYREF = BYREF.getText()

            #print(" PARAMARRAY: ",PARAMARRAY)
            #print(" BYVAL: ",BYVAL)
            #print(" BYREF: ",BYREF)
            if argDefaultValue:
                has_default=True
            else:
                has_default=None
            scope=self.tree.get_scope()
            self.tree.add_arg(scope,ambiguousIdentifier,default=argDefaultValue,has_default=has_default,optional=OPTIONAL,as_type=asTypeClause,type_hint=typeHint)


    # Exit a parse tree produced by VisualBasic6Parser#subStmt.
    def exitSubStmt(self, ctx:VisualBasic6Parser.SubStmtContext):
        self.depth -= 1
        name=self.tree.scope.pop()        




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
    listener = MyListener(source=args.file)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    pprint(listener.tree.data,width=160,compact=False)


if __name__ == "__main__":
    main()