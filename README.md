[![Unix Build Status](https://travis-ci.org/maxmalysh/prototype-interpreter.svg)](https://travis-ci.org/maxmalysh/prototype-interpreter)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/github/maxmalysh/prototype-interpreter?svg=true)](https://ci.appveyor.com/project/maxmalysh/prototype-interpreter)
[![Coverage Status](https://coveralls.io/repos/maxmalysh/prototype-interpreter/badge.svg?branch=master&service=github)](https://coveralls.io/github/maxmalysh/prototype-interpreter?branch=master)

# Prototype Interpreter

## About
Prototype is an interpreter of a small Python subset I have written as a coursework. 

## Installation
This project uses ANTLR4 as a parser generator. To run the interpreter, you will need to install ANTLR4 Python3 runtime and ANTLR itself.

Please note, that 4.5.2 runtime has [a bug which results in a dramatic performance dropdown][3].
At the moment this text was written, pypi had an older version, so it's recommended to install ANTLR4 runtime manually.

Step-by-step instruction:

1. Install [ANTLR4][1]
2. Install ANTLR4 Python3 runtime: 
    1. `git clone https://github.com/antlr/antlr4` 
    2. `cd antlr4/runtime/Python3`
    3. `python3 setup.py install` 
    
    It's also possible to use pip, package name is `antlr4-python3-runtime`. Be aware of the bug described above.
3. Generate parser
    1. cd `prototype-interpreter/prototype`
    2. `antlr4 -visitor parser/Prototype.g4`
4. Install prototype: `pip3 install .`
5. Try to launch some tests: `python3 setup.py test`
    

[1]: http://www.antlr.org
[2]: https://github.com/antlr/antlr4
[3]: http://stackoverflow.com/questions/31455500/slow-antlr4-generated-parser-in-python-but-fast-in-java