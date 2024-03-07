import xxhash

import json
from utils import file_fragment, read_file


class gardner:
    def __init__(self,file):
        self.file=file
        # load full text
        self.text=read_file(self.file)
        self.lines=self.text.split("\n")
        self.source_length=len(self.lines)
        self.whitespace_blocks=[]
        self.uncovered_blocks=[]
        self.comment_blocks=[]
        self.data={'root':{}}
        self.scope=[]
        self.fragment={}
        self.rescope=None
        self.scope_type=None
        self.scope_depth=None
        self.components=['module','class','func','sub','args','vars','ret']
        self.source_data=[]



    def get_block_at(self,line):
        if line>=self.source_length or line<0:
            return None
            
    def find_uncovered_blocks(self):
        # Parse the JSON data

        # Sort ranges by start line
        self.source_data.sort(key=lambda x: x['start'])

        # List to store the uncovered blocks
        uncovered_blocks = []

        # Initialize the previous end to 0
        prev_end = 0

        # Add uncovered blocks between ranges
        for entry in self.source_data:
            start, end = entry['start'], entry['end']
            if prev_end < start - 1:
                uncovered_blocks.append({"start": prev_end + 1, "end": start - 1})
            prev_end = end

        # Add any remaining blocks after the last covered range
        if prev_end < self.source_length:
            uncovered_blocks.append({"start": prev_end + 1, "end": self.source_length})

        self.uncovered_blocks=uncovered_blocks


    def classify_and_split_blocks(self):
        split_blocks = []

        for block in self.uncovered_blocks:
            current_block_type = None
            current_block_start = block['start']
            
            for line_number in range(block['start'], block['end'] + 1):
                line_content = self.lines[line_number - 1].strip()  # Adjusting for 0-based index
                line_type = self.get_line_type(line_content)

                if current_block_type is None:
                    current_block_type = line_type

                if line_type != current_block_type or line_number == block['end']:
                    if line_number == block['end'] and line_type == current_block_type:
                        split_blocks.append({'start': current_block_start, 'end': line_number, 'type': current_block_type})
                    else:
                        split_blocks.append({'start': current_block_start, 'end': line_number - 1, 'type': current_block_type})
                        current_block_start = line_number
                        current_block_type = line_type

                    if line_number == block['end'] and line_type != current_block_type:
                        split_blocks.append({'start': line_number, 'end': line_number, 'type': line_type})

        return split_blocks

    def get_line_type(self, line_content):
        if line_content == '':
            return 'whitespace'
        elif line_content.upper().startswith(('REM', "'")):
            return 'comment'
        else:
            return 'unknown'

    

    def find_comment_blocks(self):
        comment_blocks = []
        inside_comment_block = False
        block_start = None

        for line_number, line in enumerate(self.lines, 1):
            # Check if the line is a comment
            is_comment = line.strip().startswith("'") or line.strip().upper().startswith("REM")

            if is_comment and not inside_comment_block:
                # Start of a new comment block
                block_start = line_number
                inside_comment_block = True
            elif not is_comment and inside_comment_block:
                # End of the current comment block
                comment_blocks.append((block_start, line_number - 1))
                inside_comment_block = False

        # Check if it ends while still inside a comment block
        if inside_comment_block:
            comment_blocks.append((block_start, line_number))

        self.comment_blocks=comment_blocks


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
            obj[layer].update(data)

    def add_module(self,scope,name,data=None):
        self.add_type(scope,'module',name,data)

    def add_class(self,scope,name,data=None):
        self.add_type(scope,'class',name,data)
    
    def add_func(self,scope,name,start=None,end=None,column=None,return_type=None,visibility=None):
        obj=self.get_obj(scope)
        if 'func' not in obj:
            obj['func']={}
        source=file_fragment(self.file,start,end)
        source_hash=xxhash.xxh64('xxhash', seed=314159).hexdigest()
        self.source_data.append({'start':start,'end':end,'scope':".".join([scope,name])})
        obj['func'][name]={'name':name,'start':start,'end':end,'col':column,'return_type':return_type,'visibility':visibility,'source':source,'scope':scope,'file':self.file,'hash':source_hash}

    def add_sub(self,scope,name,start=None,end=None,column=None,visibility=None):
        obj=self.get_obj(scope)
        if 'sub' not in obj:
            obj['sub']={}
        source=file_fragment(self.file,start,end)
        source_hash=xxhash.xxh64('xxhash', seed=314159).hexdigest()
        self.source_data.append({'start':start,'end':end,'scope':".".join([scope,name])})
        obj['sub'][name]={'name':name,'start':start,'end':end,'col':column,'visibility':visibility,'source':source,'scope':scope,'file':self.file,'hash':source_hash}

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
