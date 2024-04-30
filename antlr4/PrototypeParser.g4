/*
 * The MIT License (MIT)
 * 
 * Copyright (c) 2014 by Bart Kiers (original author) and Alexandre Vitorelli (contributor -> ported
 * to CSharp) Copyright (c) 2017-2020 by Ivan Kochurkin (Positive Technologies): added ECMAScript 6
 * support, cleared and transformed to the universal grammar. Copyright (c) 2018 by Juan Alvarez
 * (contributor -> ported to Go) Copyright (c) 2019 by Student Main (contributor -> ES2020)
 * Copyright (c) 2024 by Guillermo Adrián Molina (converted to Prototype)
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
 * associated documentation files (the "Software"), to deal in the Software without restriction,
 * including without limitation the rights to use, copy, modify, merge, publish, distribute,
 * sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
 * NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 * DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

// $antlr-format alignTrailingComments true, columnLimit 150, minEmptyLines 1, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

parser grammar PrototypeParser;

options {
    language = Python3;
    tokenVocab = PrototypeLexer;
    superClass = PrototypeParserBase;
}

program
    : HashBangLine? sourceElements? EOF
    ;

sourceElement
    : statement
    ;

statement
    : block
    | variableStatement
    | importStatement
    | exportStatement
    | emptyStatement_
    | classDeclaration
    | functionDeclaration
    | expressionStatement
    | ifStatement
    | iterationStatement
    | continueStatement
    | breakStatement
    | returnStatement
    | yieldStatement
    | withStatement
    | labelledStatement
    | switchStatement
    | throwStatement
    | tryStatement
    | debuggerStatement
    ;

block
    : '{' statementList? '}'
    ;

statementList
    : statement+
    ;

importStatement
    : Import importFromBlock
    ;

importFromBlock
    : importDefault? (importNamespace | importModuleItems) importFrom eos
    | StringLiteral eos
    ;

importModuleItems
    : '{' (importAliasName ',')* (importAliasName ','?)? '}'
    ;

importAliasName
    : moduleExportName (As importedBinding)?
    ;

moduleExportName
    : identifierName
    | StringLiteral
    ;

// yield and await are permitted as BindingIdentifier in the grammar
importedBinding
    : Identifier
    | Yield
    | Await
    ;

importDefault
    : aliasName ','
    ;

importNamespace
    : ('*' | identifierName) (As identifierName)?
    ;

importFrom
    : From StringLiteral
    ;

aliasName
    : identifierName (As identifierName)?
    ;

exportStatement
    : Export Default? (exportFromBlock | declaration) eos # ExportDeclaration
    | Export Default singleExpression eos                 # ExportDefaultDeclaration
    ;

exportFromBlock
    : importNamespace importFrom eos
    | exportModuleItems importFrom? eos
    ;

exportModuleItems
    : '{' (exportAliasName ',')* (exportAliasName ','?)? '}'
    ;

exportAliasName
    : moduleExportName (As moduleExportName)?
    ;

declaration
    : variableStatement
    | classDeclaration
    | functionDeclaration
    ;

variableStatement
    : variableDeclarationList eos
    ;

variableDeclarationList
    : varModifier variableDeclaration (',' variableDeclaration)*
    ;

variableDeclaration
    : assignable ('=' singleExpression)? // ECMAScript 6: Array & Object Matching
    ;

emptyStatement_
    : SemiColon
    ;

expressionStatement
    : {self.notOpenBraceAndNotFunction()}? expressionSequence eos
    ;

ifStatement
    : If '(' expressionSequence ')' statement (Else statement)?
    ;

iterationStatement
    : Do statement While '(' expressionSequence ')' eos                                                                     # DoStatement
    | While '(' expressionSequence ')' statement                                                                            # WhileStatement
    | For '(' (expressionSequence | variableDeclarationList)? ';' expressionSequence? ';' expressionSequence? ')' statement # ForStatement
    | For '(' (singleExpression | variableDeclarationList) In expressionSequence ')' statement                              # ForInStatement
    | For Await? '(' (singleExpression | variableDeclarationList) Of expressionSequence ')' statement                       # ForOfStatement
    ;

varModifier // let, const - ECMAScript 6
    : Var
    | let_
    | Const
    ;

continueStatement
    : Continue ({self.notLineTerminator()}? identifier)? eos
    ;

breakStatement
    : Break ({self.notLineTerminator()}? identifier)? eos
    ;

returnStatement
    : Return ({self.notLineTerminator()}? expressionSequence)? eos
    ;

yieldStatement
    : (Yield | YieldStar) ({self.notLineTerminator()}? expressionSequence)? eos
    ;

withStatement
    : With '(' expressionSequence ')' statement
    ;

switchStatement
    : Switch '(' expressionSequence ')' caseBlock
    ;

caseBlock
    : '{' caseClauses? (defaultClause caseClauses?)? '}'
    ;

caseClauses
    : caseClause+
    ;

caseClause
    : Case expressionSequence ':' statementList?
    ;

defaultClause
    : Default ':' statementList?
    ;

labelledStatement
    : identifier ':' statement
    ;

throwStatement
    : Throw {self.notLineTerminator()}? expressionSequence eos
    ;

tryStatement
    : Try block (catchProduction finallyProduction? | finallyProduction)
    ;

catchProduction
    : Catch ('(' assignable? ')')? block
    ;

finallyProduction
    : Finally block
    ;

debuggerStatement
    : Debugger eos
    ;

functionDeclaration
    : Async? Function_ '*'? identifier '(' formalParameterList? ')' functionBody
    ;

classDeclaration
    : Class identifier classTail
    ;

classTail
    : (Extends singleExpression)? '{' classElement* '}'
    ;

classElement
    : (Static | {self.n("static")}? identifier)? methodDefinition
    | (Static | {self.n("static")}? identifier)? fieldDefinition
    | (Static | {self.n("static")}? identifier) block
    | emptyStatement_
    ;

methodDefinition
    : (Async {self.notLineTerminator()}?)? '*'? classElementName '(' formalParameterList? ')' functionBody
    | '*'? getter '(' ')' functionBody
    | '*'? setter '(' formalParameterList? ')' functionBody
    ;

fieldDefinition
    : classElementName initializer?
    ;

classElementName
    : propertyName
    | privateIdentifier
    ;

privateIdentifier
    : '#' identifierName
    ;

formalParameterList
    : formalParameterArg (',' formalParameterArg)* (',' lastFormalParameterArg)?
    | lastFormalParameterArg
    ;

formalParameterArg
    : assignable ('=' singleExpression)? // ECMAScript 6: Initialization
    ;

lastFormalParameterArg // ECMAScript 6: Rest Parameter
    : Ellipsis singleExpression
    ;

functionBody
    : '{' sourceElements? '}'
    ;

sourceElements
    : sourceElement+
    ;

arrayLiteral
    : ('[' elementList ']')
    ;

// Prototype supports arrasys like [,,1,2,,].
elementList
    : ','* arrayElement? (','+ arrayElement)* ','* // Yes, everything is optional
    ;

arrayElement
    : Ellipsis? singleExpression
    ;

propertyAssignment
    : propertyName ':' singleExpression                                  # PropertyExpressionAssignment
    | '[' singleExpression ']' ':' singleExpression                      # ComputedPropertyExpressionAssignment
    | Async? '*'? propertyName '(' formalParameterList? ')' functionBody # FunctionProperty
    | getter '(' ')' functionBody                                        # PropertyGetter
    | setter '(' formalParameterArg ')' functionBody                     # PropertySetter
    | Ellipsis? singleExpression                                         # PropertyShorthand
    ;

propertyName
    : identifierName
    | StringLiteral
    | numericLiteral
    | '[' singleExpression ']'
    ;

arguments
    : '(' (argument (',' argument)* ','?)? ')'
    ;

argument
    : Ellipsis? (singleExpression | identifier)
    ;

expressionSequence
    : singleExpression (',' singleExpression)*
    ;

singleExpression
    : anonymousFunction                                 # FunctionExpression
    | Class identifier? classTail                       # ClassExpression
    | singleExpression '?.' singleExpression            # OptionalChainExpression
    | singleExpression '?.'? '[' expressionSequence ']' # MemberIndexExpression
    | singleExpression '?'? '.' '#'? identifierName     # MemberDotExpression
    // Split to try `new Date()` first, then `new Date`.
    | New identifier arguments                                             # NewExpression
    | New singleExpression arguments                                       # NewExpression
    | New singleExpression                                                 # NewExpression
    | singleExpression arguments                                           # ArgumentsExpression
    | New '.' identifier                                                   # MetaExpression // new.target
    | singleExpression {self.notLineTerminator()}? op = '++'               # PostIncrementExpression
    | singleExpression {self.notLineTerminator()}? op = '--'               # PostDecreaseExpression
    | Delete singleExpression                                              # DeleteExpression
    | Void singleExpression                                                # VoidExpression
    | Typeof singleExpression                                              # TypeofExpression
    | op = '++' singleExpression                                           # PreIncrementExpression
    | op = '--' singleExpression                                           # PreDecreaseExpression
    | op = '+' singleExpression                                            # UnaryPlusExpression
    | op = '-' singleExpression                                            # UnaryMinusExpression
    | op = '~' singleExpression                                            # BitNotExpression
    | op = '!' singleExpression                                            # NotExpression
    | Await singleExpression                                               # AwaitExpression
    | <assoc = right> singleExpression '**' singleExpression               # PowerExpression
    | singleExpression op = ('*' | '/' | '%') singleExpression             # MultiplicativeExpression
    | singleExpression op = ('+' | '-') singleExpression                   # AdditiveExpression
    | singleExpression op = '??' singleExpression                          # CoalesceExpression
    | singleExpression op = ('<<' | '>>' | '>>>') singleExpression         # BitShiftExpression
    | singleExpression op = ('<' | '>' | '<=' | '>=') singleExpression     # RelationalExpression
    | singleExpression op = Instanceof singleExpression                    # InstanceofExpression
    | singleExpression op = In singleExpression                            # InExpression
    | singleExpression op = ('==' | '!=' | '===' | '!==') singleExpression # EqualityExpression
    | singleExpression op = '&' singleExpression                           # BitAndExpression
    | singleExpression op = '^' singleExpression                           # BitXOrExpression
    | singleExpression op = '|' singleExpression                           # BitOrExpression
    | singleExpression op = '&&' singleExpression                          # LogicalAndExpression
    | singleExpression op = '||' singleExpression                          # LogicalOrExpression
    | singleExpression '?' singleExpression ':' singleExpression           # TernaryExpression
    | <assoc = right> singleExpression '=' singleExpression                # AssignmentExpression
    | <assoc = right> singleExpression assignmentOperator singleExpression # AssignmentOperatorExpression
    | Import '(' singleExpression ')'                                      # ImportExpression
    | singleExpression templateStringLiteral                               # TemplateStringExpression // ECMAScript 6
    | yieldStatement                                                       # YieldExpression          // ECMAScript 6
    | This                                                                 # ThisExpression
    | identifier                                                           # IdentifierExpression
    | Super                                                                # SuperExpression
    | literal                                                              # LiteralExpression
    | arrayLiteral                                                         # ArrayLiteralExpression
    | objectLiteral                                                        # ObjectLiteralExpression
    | '(' expressionSequence ')'                                           # ParenthesizedExpression
    ;

initializer
    // TODO: must be `= AssignmentExpression` and we have such label alredy but it doesn't respect the specification.
    //  See https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-Initializer
    : '=' singleExpression
    ;

assignable
    : identifier
    | keyword
    | arrayLiteral
    | objectLiteral
    ;

objectLiteral
    : '{' (propertyAssignment (',' propertyAssignment)* ','?)? '}'
    ;

anonymousFunction
    : functionDeclaration                                             # NamedFunction
    | Async? Function_ '*'? '(' formalParameterList? ')' functionBody # AnonymousFunctionDecl
    | Async? arrowFunctionParameters '=>' arrowFunctionBody           # ArrowFunction
    ;

arrowFunctionParameters
    : propertyName
    | '(' formalParameterList? ')'
    ;

arrowFunctionBody
    : singleExpression
    | functionBody
    ;

assignmentOperator
    : '*='
    | '/='
    | '%='
    | '+='
    | '-='
    | '<<='
    | '>>='
    | '>>>='
    | '&='
    | '^='
    | '|='
    | '**='
    | '??='
    ;

literal
    : NullLiteral
    | BooleanLiteral
    | StringLiteral
    | templateStringLiteral
    | RegularExpressionLiteral
    | numericLiteral
    | bigintLiteral
    ;

templateStringLiteral
    : BackTick templateStringAtom* BackTick
    ;

templateStringAtom
    : TemplateStringAtom
    | TemplateStringStartExpression singleExpression TemplateCloseBrace
    ;

numericLiteral
    : DecimalLiteral
    | HexIntegerLiteral
    | OctalIntegerLiteral
    | OctalIntegerLiteral2
    | BinaryIntegerLiteral
    ;

bigintLiteral
    : BigDecimalIntegerLiteral
    | BigHexIntegerLiteral
    | BigOctalIntegerLiteral
    | BigBinaryIntegerLiteral
    ;

getter
    : {self.n("get")}? identifier classElementName
    ;

setter
    : {self.n("set")}? identifier classElementName
    ;

identifierName
    : identifier
    | reservedWord
    ;

identifier
    : Identifier
    | NonStrictLet
    | Async
    | As
    | From
    | Yield
    | Of
    ;

reservedWord
    : keyword
    | NullLiteral
    | BooleanLiteral
    ;

keyword
    : Break
    | Do
    | Instanceof
    | Typeof
    | Case
    | Else
    | New
    | Var
    | Catch
    | Finally
    | Return
    | Void
    | Continue
    | For
    | Switch
    | While
    | Debugger
    | Function_
    | This
    | With
    | Default
    | If
    | Throw
    | Delete
    | In
    | Try
    | Class
    | Enum
    | Extends
    | Super
    | Const
    | Export
    | Import
    | Implements
    | let_
    | Private
    | Public
    | Interface
    | Package
    | Protected
    | Static
    | Yield
    | YieldStar
    | Async
    | Await
    | From
    | As
    | Of
    ;

let_
    : NonStrictLet
    | StrictLet
    ;

eos
    : SemiColon
    | EOF
    | {self.lineTerminatorAhead()}?
    | {self.closeBrace()}?
    ;
