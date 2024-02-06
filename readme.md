# vb6 parser

## System prequisites

- antlr4
#
# Python prequisites

- antlr4-python3-runtime
- argparse

## Test code

- this pulls a repo which has lots of vb6 test code

```bash
make get-test-code
```

## Build

- this takes the 2 g4 vb6 language definition files and builds the python parser using antler

```bash
make vb6
``

## run

```bash
# --json for json output, Optional
# -- pprint for python prety print, Optional
python vb6/vb6.py <filename.py> <--json> <--pprint>

# this is the test run with test code
make test-single
make test-class
```

## import in python

```bash
from .vb6 import parse
data=parse(file)
print(data)
```

## G4 files

- These are the core of the parser, and are that the parser is based off of
- pulled from https://github.com/antlr/grammars-v4/tree/master
