# Generated from PrototypeParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrototypeParser import PrototypeParser
else:
    from PrototypeParser import PrototypeParser

# This class defines a complete listener for a parse tree produced by PrototypeParser.
class PrototypeParserListener(ParseTreeListener):

    # Enter a parse tree produced by PrototypeParser#program.
    def enterProgram(self, ctx:PrototypeParser.ProgramContext):
        pass

    # Exit a parse tree produced by PrototypeParser#program.
    def exitProgram(self, ctx:PrototypeParser.ProgramContext):
        pass


    # Enter a parse tree produced by PrototypeParser#sourceElement.
    def enterSourceElement(self, ctx:PrototypeParser.SourceElementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#sourceElement.
    def exitSourceElement(self, ctx:PrototypeParser.SourceElementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#statement.
    def enterStatement(self, ctx:PrototypeParser.StatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#statement.
    def exitStatement(self, ctx:PrototypeParser.StatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#block.
    def enterBlock(self, ctx:PrototypeParser.BlockContext):
        pass

    # Exit a parse tree produced by PrototypeParser#block.
    def exitBlock(self, ctx:PrototypeParser.BlockContext):
        pass


    # Enter a parse tree produced by PrototypeParser#statementList.
    def enterStatementList(self, ctx:PrototypeParser.StatementListContext):
        pass

    # Exit a parse tree produced by PrototypeParser#statementList.
    def exitStatementList(self, ctx:PrototypeParser.StatementListContext):
        pass


    # Enter a parse tree produced by PrototypeParser#importStatement.
    def enterImportStatement(self, ctx:PrototypeParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#importStatement.
    def exitImportStatement(self, ctx:PrototypeParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#importFromBlock.
    def enterImportFromBlock(self, ctx:PrototypeParser.ImportFromBlockContext):
        pass

    # Exit a parse tree produced by PrototypeParser#importFromBlock.
    def exitImportFromBlock(self, ctx:PrototypeParser.ImportFromBlockContext):
        pass


    # Enter a parse tree produced by PrototypeParser#importModuleItems.
    def enterImportModuleItems(self, ctx:PrototypeParser.ImportModuleItemsContext):
        pass

    # Exit a parse tree produced by PrototypeParser#importModuleItems.
    def exitImportModuleItems(self, ctx:PrototypeParser.ImportModuleItemsContext):
        pass


    # Enter a parse tree produced by PrototypeParser#importAliasName.
    def enterImportAliasName(self, ctx:PrototypeParser.ImportAliasNameContext):
        pass

    # Exit a parse tree produced by PrototypeParser#importAliasName.
    def exitImportAliasName(self, ctx:PrototypeParser.ImportAliasNameContext):
        pass


    # Enter a parse tree produced by PrototypeParser#moduleExportName.
    def enterModuleExportName(self, ctx:PrototypeParser.ModuleExportNameContext):
        pass

    # Exit a parse tree produced by PrototypeParser#moduleExportName.
    def exitModuleExportName(self, ctx:PrototypeParser.ModuleExportNameContext):
        pass


    # Enter a parse tree produced by PrototypeParser#importedBinding.
    def enterImportedBinding(self, ctx:PrototypeParser.ImportedBindingContext):
        pass

    # Exit a parse tree produced by PrototypeParser#importedBinding.
    def exitImportedBinding(self, ctx:PrototypeParser.ImportedBindingContext):
        pass


    # Enter a parse tree produced by PrototypeParser#importDefault.
    def enterImportDefault(self, ctx:PrototypeParser.ImportDefaultContext):
        pass

    # Exit a parse tree produced by PrototypeParser#importDefault.
    def exitImportDefault(self, ctx:PrototypeParser.ImportDefaultContext):
        pass


    # Enter a parse tree produced by PrototypeParser#importNamespace.
    def enterImportNamespace(self, ctx:PrototypeParser.ImportNamespaceContext):
        pass

    # Exit a parse tree produced by PrototypeParser#importNamespace.
    def exitImportNamespace(self, ctx:PrototypeParser.ImportNamespaceContext):
        pass


    # Enter a parse tree produced by PrototypeParser#importFrom.
    def enterImportFrom(self, ctx:PrototypeParser.ImportFromContext):
        pass

    # Exit a parse tree produced by PrototypeParser#importFrom.
    def exitImportFrom(self, ctx:PrototypeParser.ImportFromContext):
        pass


    # Enter a parse tree produced by PrototypeParser#aliasName.
    def enterAliasName(self, ctx:PrototypeParser.AliasNameContext):
        pass

    # Exit a parse tree produced by PrototypeParser#aliasName.
    def exitAliasName(self, ctx:PrototypeParser.AliasNameContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ExportDeclaration.
    def enterExportDeclaration(self, ctx:PrototypeParser.ExportDeclarationContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ExportDeclaration.
    def exitExportDeclaration(self, ctx:PrototypeParser.ExportDeclarationContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ExportDefaultDeclaration.
    def enterExportDefaultDeclaration(self, ctx:PrototypeParser.ExportDefaultDeclarationContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ExportDefaultDeclaration.
    def exitExportDefaultDeclaration(self, ctx:PrototypeParser.ExportDefaultDeclarationContext):
        pass


    # Enter a parse tree produced by PrototypeParser#exportFromBlock.
    def enterExportFromBlock(self, ctx:PrototypeParser.ExportFromBlockContext):
        pass

    # Exit a parse tree produced by PrototypeParser#exportFromBlock.
    def exitExportFromBlock(self, ctx:PrototypeParser.ExportFromBlockContext):
        pass


    # Enter a parse tree produced by PrototypeParser#exportModuleItems.
    def enterExportModuleItems(self, ctx:PrototypeParser.ExportModuleItemsContext):
        pass

    # Exit a parse tree produced by PrototypeParser#exportModuleItems.
    def exitExportModuleItems(self, ctx:PrototypeParser.ExportModuleItemsContext):
        pass


    # Enter a parse tree produced by PrototypeParser#exportAliasName.
    def enterExportAliasName(self, ctx:PrototypeParser.ExportAliasNameContext):
        pass

    # Exit a parse tree produced by PrototypeParser#exportAliasName.
    def exitExportAliasName(self, ctx:PrototypeParser.ExportAliasNameContext):
        pass


    # Enter a parse tree produced by PrototypeParser#declaration.
    def enterDeclaration(self, ctx:PrototypeParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PrototypeParser#declaration.
    def exitDeclaration(self, ctx:PrototypeParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PrototypeParser#variableStatement.
    def enterVariableStatement(self, ctx:PrototypeParser.VariableStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#variableStatement.
    def exitVariableStatement(self, ctx:PrototypeParser.VariableStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#variableDeclarationList.
    def enterVariableDeclarationList(self, ctx:PrototypeParser.VariableDeclarationListContext):
        pass

    # Exit a parse tree produced by PrototypeParser#variableDeclarationList.
    def exitVariableDeclarationList(self, ctx:PrototypeParser.VariableDeclarationListContext):
        pass


    # Enter a parse tree produced by PrototypeParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:PrototypeParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by PrototypeParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:PrototypeParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by PrototypeParser#emptyStatement_.
    def enterEmptyStatement_(self, ctx:PrototypeParser.EmptyStatement_Context):
        pass

    # Exit a parse tree produced by PrototypeParser#emptyStatement_.
    def exitEmptyStatement_(self, ctx:PrototypeParser.EmptyStatement_Context):
        pass


    # Enter a parse tree produced by PrototypeParser#expressionStatement.
    def enterExpressionStatement(self, ctx:PrototypeParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#expressionStatement.
    def exitExpressionStatement(self, ctx:PrototypeParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ifStatement.
    def enterIfStatement(self, ctx:PrototypeParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ifStatement.
    def exitIfStatement(self, ctx:PrototypeParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#DoStatement.
    def enterDoStatement(self, ctx:PrototypeParser.DoStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#DoStatement.
    def exitDoStatement(self, ctx:PrototypeParser.DoStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#WhileStatement.
    def enterWhileStatement(self, ctx:PrototypeParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#WhileStatement.
    def exitWhileStatement(self, ctx:PrototypeParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ForStatement.
    def enterForStatement(self, ctx:PrototypeParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ForStatement.
    def exitForStatement(self, ctx:PrototypeParser.ForStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ForInStatement.
    def enterForInStatement(self, ctx:PrototypeParser.ForInStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ForInStatement.
    def exitForInStatement(self, ctx:PrototypeParser.ForInStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ForOfStatement.
    def enterForOfStatement(self, ctx:PrototypeParser.ForOfStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ForOfStatement.
    def exitForOfStatement(self, ctx:PrototypeParser.ForOfStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#varModifier.
    def enterVarModifier(self, ctx:PrototypeParser.VarModifierContext):
        pass

    # Exit a parse tree produced by PrototypeParser#varModifier.
    def exitVarModifier(self, ctx:PrototypeParser.VarModifierContext):
        pass


    # Enter a parse tree produced by PrototypeParser#continueStatement.
    def enterContinueStatement(self, ctx:PrototypeParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#continueStatement.
    def exitContinueStatement(self, ctx:PrototypeParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#breakStatement.
    def enterBreakStatement(self, ctx:PrototypeParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#breakStatement.
    def exitBreakStatement(self, ctx:PrototypeParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#returnStatement.
    def enterReturnStatement(self, ctx:PrototypeParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#returnStatement.
    def exitReturnStatement(self, ctx:PrototypeParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#yieldStatement.
    def enterYieldStatement(self, ctx:PrototypeParser.YieldStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#yieldStatement.
    def exitYieldStatement(self, ctx:PrototypeParser.YieldStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#withStatement.
    def enterWithStatement(self, ctx:PrototypeParser.WithStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#withStatement.
    def exitWithStatement(self, ctx:PrototypeParser.WithStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#switchStatement.
    def enterSwitchStatement(self, ctx:PrototypeParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#switchStatement.
    def exitSwitchStatement(self, ctx:PrototypeParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#caseBlock.
    def enterCaseBlock(self, ctx:PrototypeParser.CaseBlockContext):
        pass

    # Exit a parse tree produced by PrototypeParser#caseBlock.
    def exitCaseBlock(self, ctx:PrototypeParser.CaseBlockContext):
        pass


    # Enter a parse tree produced by PrototypeParser#caseClauses.
    def enterCaseClauses(self, ctx:PrototypeParser.CaseClausesContext):
        pass

    # Exit a parse tree produced by PrototypeParser#caseClauses.
    def exitCaseClauses(self, ctx:PrototypeParser.CaseClausesContext):
        pass


    # Enter a parse tree produced by PrototypeParser#caseClause.
    def enterCaseClause(self, ctx:PrototypeParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by PrototypeParser#caseClause.
    def exitCaseClause(self, ctx:PrototypeParser.CaseClauseContext):
        pass


    # Enter a parse tree produced by PrototypeParser#defaultClause.
    def enterDefaultClause(self, ctx:PrototypeParser.DefaultClauseContext):
        pass

    # Exit a parse tree produced by PrototypeParser#defaultClause.
    def exitDefaultClause(self, ctx:PrototypeParser.DefaultClauseContext):
        pass


    # Enter a parse tree produced by PrototypeParser#labelledStatement.
    def enterLabelledStatement(self, ctx:PrototypeParser.LabelledStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#labelledStatement.
    def exitLabelledStatement(self, ctx:PrototypeParser.LabelledStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#throwStatement.
    def enterThrowStatement(self, ctx:PrototypeParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#throwStatement.
    def exitThrowStatement(self, ctx:PrototypeParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#tryStatement.
    def enterTryStatement(self, ctx:PrototypeParser.TryStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#tryStatement.
    def exitTryStatement(self, ctx:PrototypeParser.TryStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#catchProduction.
    def enterCatchProduction(self, ctx:PrototypeParser.CatchProductionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#catchProduction.
    def exitCatchProduction(self, ctx:PrototypeParser.CatchProductionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#finallyProduction.
    def enterFinallyProduction(self, ctx:PrototypeParser.FinallyProductionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#finallyProduction.
    def exitFinallyProduction(self, ctx:PrototypeParser.FinallyProductionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#debuggerStatement.
    def enterDebuggerStatement(self, ctx:PrototypeParser.DebuggerStatementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#debuggerStatement.
    def exitDebuggerStatement(self, ctx:PrototypeParser.DebuggerStatementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:PrototypeParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by PrototypeParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:PrototypeParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by PrototypeParser#classDeclaration.
    def enterClassDeclaration(self, ctx:PrototypeParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by PrototypeParser#classDeclaration.
    def exitClassDeclaration(self, ctx:PrototypeParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by PrototypeParser#classTail.
    def enterClassTail(self, ctx:PrototypeParser.ClassTailContext):
        pass

    # Exit a parse tree produced by PrototypeParser#classTail.
    def exitClassTail(self, ctx:PrototypeParser.ClassTailContext):
        pass


    # Enter a parse tree produced by PrototypeParser#classElement.
    def enterClassElement(self, ctx:PrototypeParser.ClassElementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#classElement.
    def exitClassElement(self, ctx:PrototypeParser.ClassElementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#methodDefinition.
    def enterMethodDefinition(self, ctx:PrototypeParser.MethodDefinitionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#methodDefinition.
    def exitMethodDefinition(self, ctx:PrototypeParser.MethodDefinitionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#fieldDefinition.
    def enterFieldDefinition(self, ctx:PrototypeParser.FieldDefinitionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#fieldDefinition.
    def exitFieldDefinition(self, ctx:PrototypeParser.FieldDefinitionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#classElementName.
    def enterClassElementName(self, ctx:PrototypeParser.ClassElementNameContext):
        pass

    # Exit a parse tree produced by PrototypeParser#classElementName.
    def exitClassElementName(self, ctx:PrototypeParser.ClassElementNameContext):
        pass


    # Enter a parse tree produced by PrototypeParser#privateIdentifier.
    def enterPrivateIdentifier(self, ctx:PrototypeParser.PrivateIdentifierContext):
        pass

    # Exit a parse tree produced by PrototypeParser#privateIdentifier.
    def exitPrivateIdentifier(self, ctx:PrototypeParser.PrivateIdentifierContext):
        pass


    # Enter a parse tree produced by PrototypeParser#formalParameterList.
    def enterFormalParameterList(self, ctx:PrototypeParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by PrototypeParser#formalParameterList.
    def exitFormalParameterList(self, ctx:PrototypeParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by PrototypeParser#formalParameterArg.
    def enterFormalParameterArg(self, ctx:PrototypeParser.FormalParameterArgContext):
        pass

    # Exit a parse tree produced by PrototypeParser#formalParameterArg.
    def exitFormalParameterArg(self, ctx:PrototypeParser.FormalParameterArgContext):
        pass


    # Enter a parse tree produced by PrototypeParser#lastFormalParameterArg.
    def enterLastFormalParameterArg(self, ctx:PrototypeParser.LastFormalParameterArgContext):
        pass

    # Exit a parse tree produced by PrototypeParser#lastFormalParameterArg.
    def exitLastFormalParameterArg(self, ctx:PrototypeParser.LastFormalParameterArgContext):
        pass


    # Enter a parse tree produced by PrototypeParser#functionBody.
    def enterFunctionBody(self, ctx:PrototypeParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by PrototypeParser#functionBody.
    def exitFunctionBody(self, ctx:PrototypeParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by PrototypeParser#sourceElements.
    def enterSourceElements(self, ctx:PrototypeParser.SourceElementsContext):
        pass

    # Exit a parse tree produced by PrototypeParser#sourceElements.
    def exitSourceElements(self, ctx:PrototypeParser.SourceElementsContext):
        pass


    # Enter a parse tree produced by PrototypeParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:PrototypeParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by PrototypeParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:PrototypeParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by PrototypeParser#elementList.
    def enterElementList(self, ctx:PrototypeParser.ElementListContext):
        pass

    # Exit a parse tree produced by PrototypeParser#elementList.
    def exitElementList(self, ctx:PrototypeParser.ElementListContext):
        pass


    # Enter a parse tree produced by PrototypeParser#arrayElement.
    def enterArrayElement(self, ctx:PrototypeParser.ArrayElementContext):
        pass

    # Exit a parse tree produced by PrototypeParser#arrayElement.
    def exitArrayElement(self, ctx:PrototypeParser.ArrayElementContext):
        pass


    # Enter a parse tree produced by PrototypeParser#PropertyExpressionAssignment.
    def enterPropertyExpressionAssignment(self, ctx:PrototypeParser.PropertyExpressionAssignmentContext):
        pass

    # Exit a parse tree produced by PrototypeParser#PropertyExpressionAssignment.
    def exitPropertyExpressionAssignment(self, ctx:PrototypeParser.PropertyExpressionAssignmentContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ComputedPropertyExpressionAssignment.
    def enterComputedPropertyExpressionAssignment(self, ctx:PrototypeParser.ComputedPropertyExpressionAssignmentContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ComputedPropertyExpressionAssignment.
    def exitComputedPropertyExpressionAssignment(self, ctx:PrototypeParser.ComputedPropertyExpressionAssignmentContext):
        pass


    # Enter a parse tree produced by PrototypeParser#FunctionProperty.
    def enterFunctionProperty(self, ctx:PrototypeParser.FunctionPropertyContext):
        pass

    # Exit a parse tree produced by PrototypeParser#FunctionProperty.
    def exitFunctionProperty(self, ctx:PrototypeParser.FunctionPropertyContext):
        pass


    # Enter a parse tree produced by PrototypeParser#PropertyGetter.
    def enterPropertyGetter(self, ctx:PrototypeParser.PropertyGetterContext):
        pass

    # Exit a parse tree produced by PrototypeParser#PropertyGetter.
    def exitPropertyGetter(self, ctx:PrototypeParser.PropertyGetterContext):
        pass


    # Enter a parse tree produced by PrototypeParser#PropertySetter.
    def enterPropertySetter(self, ctx:PrototypeParser.PropertySetterContext):
        pass

    # Exit a parse tree produced by PrototypeParser#PropertySetter.
    def exitPropertySetter(self, ctx:PrototypeParser.PropertySetterContext):
        pass


    # Enter a parse tree produced by PrototypeParser#PropertyShorthand.
    def enterPropertyShorthand(self, ctx:PrototypeParser.PropertyShorthandContext):
        pass

    # Exit a parse tree produced by PrototypeParser#PropertyShorthand.
    def exitPropertyShorthand(self, ctx:PrototypeParser.PropertyShorthandContext):
        pass


    # Enter a parse tree produced by PrototypeParser#propertyName.
    def enterPropertyName(self, ctx:PrototypeParser.PropertyNameContext):
        pass

    # Exit a parse tree produced by PrototypeParser#propertyName.
    def exitPropertyName(self, ctx:PrototypeParser.PropertyNameContext):
        pass


    # Enter a parse tree produced by PrototypeParser#arguments.
    def enterArguments(self, ctx:PrototypeParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by PrototypeParser#arguments.
    def exitArguments(self, ctx:PrototypeParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by PrototypeParser#argument.
    def enterArgument(self, ctx:PrototypeParser.ArgumentContext):
        pass

    # Exit a parse tree produced by PrototypeParser#argument.
    def exitArgument(self, ctx:PrototypeParser.ArgumentContext):
        pass


    # Enter a parse tree produced by PrototypeParser#expressionSequence.
    def enterExpressionSequence(self, ctx:PrototypeParser.ExpressionSequenceContext):
        pass

    # Exit a parse tree produced by PrototypeParser#expressionSequence.
    def exitExpressionSequence(self, ctx:PrototypeParser.ExpressionSequenceContext):
        pass


    # Enter a parse tree produced by PrototypeParser#TemplateStringExpression.
    def enterTemplateStringExpression(self, ctx:PrototypeParser.TemplateStringExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#TemplateStringExpression.
    def exitTemplateStringExpression(self, ctx:PrototypeParser.TemplateStringExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#TernaryExpression.
    def enterTernaryExpression(self, ctx:PrototypeParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#TernaryExpression.
    def exitTernaryExpression(self, ctx:PrototypeParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#LogicalAndExpression.
    def enterLogicalAndExpression(self, ctx:PrototypeParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#LogicalAndExpression.
    def exitLogicalAndExpression(self, ctx:PrototypeParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#PowerExpression.
    def enterPowerExpression(self, ctx:PrototypeParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#PowerExpression.
    def exitPowerExpression(self, ctx:PrototypeParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#PreIncrementExpression.
    def enterPreIncrementExpression(self, ctx:PrototypeParser.PreIncrementExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#PreIncrementExpression.
    def exitPreIncrementExpression(self, ctx:PrototypeParser.PreIncrementExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ObjectLiteralExpression.
    def enterObjectLiteralExpression(self, ctx:PrototypeParser.ObjectLiteralExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ObjectLiteralExpression.
    def exitObjectLiteralExpression(self, ctx:PrototypeParser.ObjectLiteralExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#MetaExpression.
    def enterMetaExpression(self, ctx:PrototypeParser.MetaExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#MetaExpression.
    def exitMetaExpression(self, ctx:PrototypeParser.MetaExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#InExpression.
    def enterInExpression(self, ctx:PrototypeParser.InExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#InExpression.
    def exitInExpression(self, ctx:PrototypeParser.InExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#LogicalOrExpression.
    def enterLogicalOrExpression(self, ctx:PrototypeParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#LogicalOrExpression.
    def exitLogicalOrExpression(self, ctx:PrototypeParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#OptionalChainExpression.
    def enterOptionalChainExpression(self, ctx:PrototypeParser.OptionalChainExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#OptionalChainExpression.
    def exitOptionalChainExpression(self, ctx:PrototypeParser.OptionalChainExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#NotExpression.
    def enterNotExpression(self, ctx:PrototypeParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#NotExpression.
    def exitNotExpression(self, ctx:PrototypeParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#PreDecreaseExpression.
    def enterPreDecreaseExpression(self, ctx:PrototypeParser.PreDecreaseExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#PreDecreaseExpression.
    def exitPreDecreaseExpression(self, ctx:PrototypeParser.PreDecreaseExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ArgumentsExpression.
    def enterArgumentsExpression(self, ctx:PrototypeParser.ArgumentsExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ArgumentsExpression.
    def exitArgumentsExpression(self, ctx:PrototypeParser.ArgumentsExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#AwaitExpression.
    def enterAwaitExpression(self, ctx:PrototypeParser.AwaitExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#AwaitExpression.
    def exitAwaitExpression(self, ctx:PrototypeParser.AwaitExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ThisExpression.
    def enterThisExpression(self, ctx:PrototypeParser.ThisExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ThisExpression.
    def exitThisExpression(self, ctx:PrototypeParser.ThisExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#FunctionExpression.
    def enterFunctionExpression(self, ctx:PrototypeParser.FunctionExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#FunctionExpression.
    def exitFunctionExpression(self, ctx:PrototypeParser.FunctionExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#UnaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx:PrototypeParser.UnaryMinusExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#UnaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx:PrototypeParser.UnaryMinusExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx:PrototypeParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx:PrototypeParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#PostDecreaseExpression.
    def enterPostDecreaseExpression(self, ctx:PrototypeParser.PostDecreaseExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#PostDecreaseExpression.
    def exitPostDecreaseExpression(self, ctx:PrototypeParser.PostDecreaseExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#TypeofExpression.
    def enterTypeofExpression(self, ctx:PrototypeParser.TypeofExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#TypeofExpression.
    def exitTypeofExpression(self, ctx:PrototypeParser.TypeofExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#InstanceofExpression.
    def enterInstanceofExpression(self, ctx:PrototypeParser.InstanceofExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#InstanceofExpression.
    def exitInstanceofExpression(self, ctx:PrototypeParser.InstanceofExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#UnaryPlusExpression.
    def enterUnaryPlusExpression(self, ctx:PrototypeParser.UnaryPlusExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#UnaryPlusExpression.
    def exitUnaryPlusExpression(self, ctx:PrototypeParser.UnaryPlusExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#DeleteExpression.
    def enterDeleteExpression(self, ctx:PrototypeParser.DeleteExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#DeleteExpression.
    def exitDeleteExpression(self, ctx:PrototypeParser.DeleteExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ImportExpression.
    def enterImportExpression(self, ctx:PrototypeParser.ImportExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ImportExpression.
    def exitImportExpression(self, ctx:PrototypeParser.ImportExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#EqualityExpression.
    def enterEqualityExpression(self, ctx:PrototypeParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#EqualityExpression.
    def exitEqualityExpression(self, ctx:PrototypeParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#BitXOrExpression.
    def enterBitXOrExpression(self, ctx:PrototypeParser.BitXOrExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#BitXOrExpression.
    def exitBitXOrExpression(self, ctx:PrototypeParser.BitXOrExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#SuperExpression.
    def enterSuperExpression(self, ctx:PrototypeParser.SuperExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#SuperExpression.
    def exitSuperExpression(self, ctx:PrototypeParser.SuperExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#MultiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:PrototypeParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#MultiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:PrototypeParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#BitShiftExpression.
    def enterBitShiftExpression(self, ctx:PrototypeParser.BitShiftExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#BitShiftExpression.
    def exitBitShiftExpression(self, ctx:PrototypeParser.BitShiftExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:PrototypeParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:PrototypeParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#AdditiveExpression.
    def enterAdditiveExpression(self, ctx:PrototypeParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#AdditiveExpression.
    def exitAdditiveExpression(self, ctx:PrototypeParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#RelationalExpression.
    def enterRelationalExpression(self, ctx:PrototypeParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#RelationalExpression.
    def exitRelationalExpression(self, ctx:PrototypeParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#PostIncrementExpression.
    def enterPostIncrementExpression(self, ctx:PrototypeParser.PostIncrementExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#PostIncrementExpression.
    def exitPostIncrementExpression(self, ctx:PrototypeParser.PostIncrementExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#YieldExpression.
    def enterYieldExpression(self, ctx:PrototypeParser.YieldExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#YieldExpression.
    def exitYieldExpression(self, ctx:PrototypeParser.YieldExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#BitNotExpression.
    def enterBitNotExpression(self, ctx:PrototypeParser.BitNotExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#BitNotExpression.
    def exitBitNotExpression(self, ctx:PrototypeParser.BitNotExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#NewExpression.
    def enterNewExpression(self, ctx:PrototypeParser.NewExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#NewExpression.
    def exitNewExpression(self, ctx:PrototypeParser.NewExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#LiteralExpression.
    def enterLiteralExpression(self, ctx:PrototypeParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#LiteralExpression.
    def exitLiteralExpression(self, ctx:PrototypeParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ArrayLiteralExpression.
    def enterArrayLiteralExpression(self, ctx:PrototypeParser.ArrayLiteralExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ArrayLiteralExpression.
    def exitArrayLiteralExpression(self, ctx:PrototypeParser.ArrayLiteralExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#MemberDotExpression.
    def enterMemberDotExpression(self, ctx:PrototypeParser.MemberDotExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#MemberDotExpression.
    def exitMemberDotExpression(self, ctx:PrototypeParser.MemberDotExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ClassExpression.
    def enterClassExpression(self, ctx:PrototypeParser.ClassExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ClassExpression.
    def exitClassExpression(self, ctx:PrototypeParser.ClassExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#MemberIndexExpression.
    def enterMemberIndexExpression(self, ctx:PrototypeParser.MemberIndexExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#MemberIndexExpression.
    def exitMemberIndexExpression(self, ctx:PrototypeParser.MemberIndexExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#IdentifierExpression.
    def enterIdentifierExpression(self, ctx:PrototypeParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#IdentifierExpression.
    def exitIdentifierExpression(self, ctx:PrototypeParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#BitAndExpression.
    def enterBitAndExpression(self, ctx:PrototypeParser.BitAndExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#BitAndExpression.
    def exitBitAndExpression(self, ctx:PrototypeParser.BitAndExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#BitOrExpression.
    def enterBitOrExpression(self, ctx:PrototypeParser.BitOrExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#BitOrExpression.
    def exitBitOrExpression(self, ctx:PrototypeParser.BitOrExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#AssignmentOperatorExpression.
    def enterAssignmentOperatorExpression(self, ctx:PrototypeParser.AssignmentOperatorExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#AssignmentOperatorExpression.
    def exitAssignmentOperatorExpression(self, ctx:PrototypeParser.AssignmentOperatorExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#VoidExpression.
    def enterVoidExpression(self, ctx:PrototypeParser.VoidExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#VoidExpression.
    def exitVoidExpression(self, ctx:PrototypeParser.VoidExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#CoalesceExpression.
    def enterCoalesceExpression(self, ctx:PrototypeParser.CoalesceExpressionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#CoalesceExpression.
    def exitCoalesceExpression(self, ctx:PrototypeParser.CoalesceExpressionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#initializer.
    def enterInitializer(self, ctx:PrototypeParser.InitializerContext):
        pass

    # Exit a parse tree produced by PrototypeParser#initializer.
    def exitInitializer(self, ctx:PrototypeParser.InitializerContext):
        pass


    # Enter a parse tree produced by PrototypeParser#assignable.
    def enterAssignable(self, ctx:PrototypeParser.AssignableContext):
        pass

    # Exit a parse tree produced by PrototypeParser#assignable.
    def exitAssignable(self, ctx:PrototypeParser.AssignableContext):
        pass


    # Enter a parse tree produced by PrototypeParser#objectLiteral.
    def enterObjectLiteral(self, ctx:PrototypeParser.ObjectLiteralContext):
        pass

    # Exit a parse tree produced by PrototypeParser#objectLiteral.
    def exitObjectLiteral(self, ctx:PrototypeParser.ObjectLiteralContext):
        pass


    # Enter a parse tree produced by PrototypeParser#NamedFunction.
    def enterNamedFunction(self, ctx:PrototypeParser.NamedFunctionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#NamedFunction.
    def exitNamedFunction(self, ctx:PrototypeParser.NamedFunctionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#AnonymousFunctionDecl.
    def enterAnonymousFunctionDecl(self, ctx:PrototypeParser.AnonymousFunctionDeclContext):
        pass

    # Exit a parse tree produced by PrototypeParser#AnonymousFunctionDecl.
    def exitAnonymousFunctionDecl(self, ctx:PrototypeParser.AnonymousFunctionDeclContext):
        pass


    # Enter a parse tree produced by PrototypeParser#ArrowFunction.
    def enterArrowFunction(self, ctx:PrototypeParser.ArrowFunctionContext):
        pass

    # Exit a parse tree produced by PrototypeParser#ArrowFunction.
    def exitArrowFunction(self, ctx:PrototypeParser.ArrowFunctionContext):
        pass


    # Enter a parse tree produced by PrototypeParser#arrowFunctionParameters.
    def enterArrowFunctionParameters(self, ctx:PrototypeParser.ArrowFunctionParametersContext):
        pass

    # Exit a parse tree produced by PrototypeParser#arrowFunctionParameters.
    def exitArrowFunctionParameters(self, ctx:PrototypeParser.ArrowFunctionParametersContext):
        pass


    # Enter a parse tree produced by PrototypeParser#arrowFunctionBody.
    def enterArrowFunctionBody(self, ctx:PrototypeParser.ArrowFunctionBodyContext):
        pass

    # Exit a parse tree produced by PrototypeParser#arrowFunctionBody.
    def exitArrowFunctionBody(self, ctx:PrototypeParser.ArrowFunctionBodyContext):
        pass


    # Enter a parse tree produced by PrototypeParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:PrototypeParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by PrototypeParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:PrototypeParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by PrototypeParser#literal.
    def enterLiteral(self, ctx:PrototypeParser.LiteralContext):
        pass

    # Exit a parse tree produced by PrototypeParser#literal.
    def exitLiteral(self, ctx:PrototypeParser.LiteralContext):
        pass


    # Enter a parse tree produced by PrototypeParser#templateStringLiteral.
    def enterTemplateStringLiteral(self, ctx:PrototypeParser.TemplateStringLiteralContext):
        pass

    # Exit a parse tree produced by PrototypeParser#templateStringLiteral.
    def exitTemplateStringLiteral(self, ctx:PrototypeParser.TemplateStringLiteralContext):
        pass


    # Enter a parse tree produced by PrototypeParser#templateStringAtom.
    def enterTemplateStringAtom(self, ctx:PrototypeParser.TemplateStringAtomContext):
        pass

    # Exit a parse tree produced by PrototypeParser#templateStringAtom.
    def exitTemplateStringAtom(self, ctx:PrototypeParser.TemplateStringAtomContext):
        pass


    # Enter a parse tree produced by PrototypeParser#numericLiteral.
    def enterNumericLiteral(self, ctx:PrototypeParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by PrototypeParser#numericLiteral.
    def exitNumericLiteral(self, ctx:PrototypeParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by PrototypeParser#bigintLiteral.
    def enterBigintLiteral(self, ctx:PrototypeParser.BigintLiteralContext):
        pass

    # Exit a parse tree produced by PrototypeParser#bigintLiteral.
    def exitBigintLiteral(self, ctx:PrototypeParser.BigintLiteralContext):
        pass


    # Enter a parse tree produced by PrototypeParser#getter.
    def enterGetter(self, ctx:PrototypeParser.GetterContext):
        pass

    # Exit a parse tree produced by PrototypeParser#getter.
    def exitGetter(self, ctx:PrototypeParser.GetterContext):
        pass


    # Enter a parse tree produced by PrototypeParser#setter.
    def enterSetter(self, ctx:PrototypeParser.SetterContext):
        pass

    # Exit a parse tree produced by PrototypeParser#setter.
    def exitSetter(self, ctx:PrototypeParser.SetterContext):
        pass


    # Enter a parse tree produced by PrototypeParser#identifierName.
    def enterIdentifierName(self, ctx:PrototypeParser.IdentifierNameContext):
        pass

    # Exit a parse tree produced by PrototypeParser#identifierName.
    def exitIdentifierName(self, ctx:PrototypeParser.IdentifierNameContext):
        pass


    # Enter a parse tree produced by PrototypeParser#identifier.
    def enterIdentifier(self, ctx:PrototypeParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PrototypeParser#identifier.
    def exitIdentifier(self, ctx:PrototypeParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PrototypeParser#reservedWord.
    def enterReservedWord(self, ctx:PrototypeParser.ReservedWordContext):
        pass

    # Exit a parse tree produced by PrototypeParser#reservedWord.
    def exitReservedWord(self, ctx:PrototypeParser.ReservedWordContext):
        pass


    # Enter a parse tree produced by PrototypeParser#keyword.
    def enterKeyword(self, ctx:PrototypeParser.KeywordContext):
        pass

    # Exit a parse tree produced by PrototypeParser#keyword.
    def exitKeyword(self, ctx:PrototypeParser.KeywordContext):
        pass


    # Enter a parse tree produced by PrototypeParser#let_.
    def enterLet_(self, ctx:PrototypeParser.Let_Context):
        pass

    # Exit a parse tree produced by PrototypeParser#let_.
    def exitLet_(self, ctx:PrototypeParser.Let_Context):
        pass


    # Enter a parse tree produced by PrototypeParser#eos.
    def enterEos(self, ctx:PrototypeParser.EosContext):
        pass

    # Exit a parse tree produced by PrototypeParser#eos.
    def exitEos(self, ctx:PrototypeParser.EosContext):
        pass


