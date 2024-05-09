import logging
from pathlib import Path
import sys
import argparse
import time
from enum import Enum

import antlr4
from antlr4.tree.Trees import Trees

from prototype.version import __version__
from prototype.ast.builder.Builder import CustomVisitor
from prototype.parser.CST import CstFlattened, CstFiltered
from prototype.parser.Errors import CustomErrorStrategy, CustomErrorListener
from prototype.parser.CustomLexer import CustomLexer
from prototype.parser.PrototypeParser import PrototypeParser
from prototype.shell.shell import InteractiveShell

log = logging.getLogger(__name__)

log_levels = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warn': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


class InputType(Enum):
    File = 1
    SingleInput = 2
    ExpressionNode = 3


parserRuleFor = {
    InputType.File: PrototypeParser.program,
    InputType.SingleInput: PrototypeParser.program,
    InputType.ExpressionNode: PrototypeParser.program,
}

visitorRuleFor = {
    InputType.File: CustomVisitor.visitProgram,
    InputType.SingleInput: CustomVisitor.visitProgram,
    InputType.ExpressionNode: CustomVisitor.visitProgram,
}


class EvalArguments:
    def __init__(self, cst=False, parse_tree=False, parse_only=False, print_timings=False):
        self.cst = cst
        self.parse_tree = parse_tree
        self.parse_only = parse_only
        self.print_timings = print_timings


def prototype_eval(sourcecode: str, firstRule=InputType.ExpressionNode, options=None):
    if options is None:
        options = EvalArguments()

    totalTime = time.time()
    input_stream = antlr4.InputStream(sourcecode)

    # Instantiate an run generated lexer
    lexer = CustomLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)

    # Instantiate and run generated parser
    parser = PrototypeParser(tokens)
    parser._errHandler = CustomErrorStrategy()

    error_listener = CustomErrorListener()
    parser.addErrorListener(error_listener)

    # Traverse the parse tree
    parseTime = time.time()
    try:
        parse_tree = parserRuleFor[firstRule](parser)
    except Exception as e:
        return -1
    parseTime = time.time() - parseTime

    if error_listener.errors_encountered != 0:
        return -1

    # Print parse trees if need (full or flattened)
    if options.parse_tree:
        parseTreeString = Trees.toStringTree(parse_tree, recog=parser)
        print(parseTreeString)

    if options.cst:
        cst = CstFiltered(tree=parse_tree)
        print(cst)

    # Build an Node
    astBuildTime = time.time()

    visitor = CustomVisitor()
    ast = visitorRuleFor[firstRule](visitor, parse_tree)

    astBuildTime = time.time() - astBuildTime

    if ast is None:
        return -1

    if options.parse_only:
        return 0

    # Evaluate the Node we've built
    evalTime = time.time()
    try:
        evalResult = ast.eval()
    except BaseException as e:
        print(e.__class__.__name__ + ": " + str(e))
        return -1

    evalTime = time.time() - evalTime

    totalTime = time.time() - totalTime

    if options.print_timings:
        timings = [
            ('Parsing',         parseTime),
            ('Building an Node', astBuildTime),
            ('Evaluating',      evalTime),
            ('Total time',      totalTime),
            ('Etc', totalTime-parseTime-astBuildTime-evalTime)
        ]
        print("#"*80)
        for timing in timings:
            print((timing[0]+": %.3f ms") % (timing[1]*1000))

    if firstRule == InputType.ExpressionNode:
        return evalResult

    return 0


def import_stdlib():
    stdlib_path = Path(Path(__file__).parent, 'stdlib')
    for file in stdlib_path.iterdir():
        if file.is_file():
            try:
                with file.open('r') as f:
                    log.debug(f"Loading stdlib file: {file.name}")
                    content = f.read() + '\n'
                    prototype_eval(content, InputType.File)
            except FileNotFoundError:
                log.error(f"Error opening file: {file.name}")


def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument('filename', type=str, nargs='?',
                           help='Path to the script file.')
    argParser.add_argument('-c', dest='eval_input', type=str,
                           help='Program passed in as string')
    argParser.add_argument('--cst', dest='cst', action='store_true',
                           help='Show flattened concreted syntax tree for the input (parse tree)')
    argParser.add_argument('--tokens',  dest='parse_tree',  action='store_true',
                           help='Show string representation of a parse tree for the input')
    argParser.add_argument('--parse', dest='parse_only', action='store_true',
                           help='Parse input without evaluating it.')
    argParser.add_argument('--timings', dest='print_timings', action='store_true',
                           help='Print time spend during parsing, building an Node and evaluating.')
    argParser.add_argument('-q', dest='ignore_greeting', action='store_true',
                           help="Don't print version and copyright messages on interactive startup")
    argParser.add_argument('-i', dest='force_promt', action='store_true',
                           help='forces a prompt even if stdin does not appear to be a terminal')
    argParser.add_argument('-V', '--version',
                           help='Print version information and quit',
                           action='version',
                           version='%(prog)s version ' + __version__)
    argParser.add_argument('-l', '--log-level',
                           help='Set the logging level ("debug"|"info"|"warn"|"error"|"fatal")',
                           choices=log_levels.keys(),
                           metavar='LOG_LEVEL',
                           default='info')
    #
    # Parse arguments
    #
    argParser.set_defaults(cst=False, parse_tree=False,
                           tokens=False, parse=False, timings=False)
    options = argParser.parse_args()
    logging.basicConfig(level=log_levels[options.log_level])

    import_stdlib()
    #
    # Check whether terminal is attached
    #
    isatty = True if sys.stdin.isatty() else False

    if options.filename is None and (isatty or options.force_promt) and not options.eval_input:
        shell = InteractiveShell(options)

        if not options.ignore_greeting:
            shell.print_greeting()

        shell.loop()

    if options.eval_input is not None:
        firstRule = InputType.SingleInput
        content = options.eval_input
    else:
        firstRule = InputType.File

        if isatty:
            with open(options.filename) as file_contents:
                log.debug(f"Loading file: {options.filename}")
                content = file_contents.read()
        else:
            content = ''.join(sys.stdin.readlines())

    content += '\n'
    try:
        retvalue = prototype_eval(content, firstRule, options)
        exit(retvalue)
    except Exception as e:
        log.error(str(e))
        exit(-1)


if __name__ == '__main__':
    main()
