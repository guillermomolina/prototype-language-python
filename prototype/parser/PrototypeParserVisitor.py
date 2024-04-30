# Generated from PrototypeParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrototypeParser import PrototypeParser
else:
    from PrototypeParser import PrototypeParser

# This class defines a complete generic visitor for a parse tree produced by PrototypeParser.

class PrototypeParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrototypeParser#program.
    def visitProgram(self, ctx:PrototypeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#sourceElement.
    def visitSourceElement(self, ctx:PrototypeParser.SourceElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#statement.
    def visitStatement(self, ctx:PrototypeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#block.
    def visitBlock(self, ctx:PrototypeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#statementList.
    def visitStatementList(self, ctx:PrototypeParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#importStatement.
    def visitImportStatement(self, ctx:PrototypeParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#importFromBlock.
    def visitImportFromBlock(self, ctx:PrototypeParser.ImportFromBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#importModuleItems.
    def visitImportModuleItems(self, ctx:PrototypeParser.ImportModuleItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#importAliasName.
    def visitImportAliasName(self, ctx:PrototypeParser.ImportAliasNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#moduleExportName.
    def visitModuleExportName(self, ctx:PrototypeParser.ModuleExportNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#importedBinding.
    def visitImportedBinding(self, ctx:PrototypeParser.ImportedBindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#importDefault.
    def visitImportDefault(self, ctx:PrototypeParser.ImportDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#importNamespace.
    def visitImportNamespace(self, ctx:PrototypeParser.ImportNamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#importFrom.
    def visitImportFrom(self, ctx:PrototypeParser.ImportFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#aliasName.
    def visitAliasName(self, ctx:PrototypeParser.AliasNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ExportDeclaration.
    def visitExportDeclaration(self, ctx:PrototypeParser.ExportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ExportDefaultDeclaration.
    def visitExportDefaultDeclaration(self, ctx:PrototypeParser.ExportDefaultDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#exportFromBlock.
    def visitExportFromBlock(self, ctx:PrototypeParser.ExportFromBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#exportModuleItems.
    def visitExportModuleItems(self, ctx:PrototypeParser.ExportModuleItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#exportAliasName.
    def visitExportAliasName(self, ctx:PrototypeParser.ExportAliasNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#declaration.
    def visitDeclaration(self, ctx:PrototypeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#variableStatement.
    def visitVariableStatement(self, ctx:PrototypeParser.VariableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx:PrototypeParser.VariableDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:PrototypeParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#emptyStatement_.
    def visitEmptyStatement_(self, ctx:PrototypeParser.EmptyStatement_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#expressionStatement.
    def visitExpressionStatement(self, ctx:PrototypeParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ifStatement.
    def visitIfStatement(self, ctx:PrototypeParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#DoStatement.
    def visitDoStatement(self, ctx:PrototypeParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#WhileStatement.
    def visitWhileStatement(self, ctx:PrototypeParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ForStatement.
    def visitForStatement(self, ctx:PrototypeParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ForInStatement.
    def visitForInStatement(self, ctx:PrototypeParser.ForInStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ForOfStatement.
    def visitForOfStatement(self, ctx:PrototypeParser.ForOfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#varModifier.
    def visitVarModifier(self, ctx:PrototypeParser.VarModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#continueStatement.
    def visitContinueStatement(self, ctx:PrototypeParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#breakStatement.
    def visitBreakStatement(self, ctx:PrototypeParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#returnStatement.
    def visitReturnStatement(self, ctx:PrototypeParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#yieldStatement.
    def visitYieldStatement(self, ctx:PrototypeParser.YieldStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#withStatement.
    def visitWithStatement(self, ctx:PrototypeParser.WithStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#switchStatement.
    def visitSwitchStatement(self, ctx:PrototypeParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#caseBlock.
    def visitCaseBlock(self, ctx:PrototypeParser.CaseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#caseClauses.
    def visitCaseClauses(self, ctx:PrototypeParser.CaseClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#caseClause.
    def visitCaseClause(self, ctx:PrototypeParser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#defaultClause.
    def visitDefaultClause(self, ctx:PrototypeParser.DefaultClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#labelledStatement.
    def visitLabelledStatement(self, ctx:PrototypeParser.LabelledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#throwStatement.
    def visitThrowStatement(self, ctx:PrototypeParser.ThrowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#tryStatement.
    def visitTryStatement(self, ctx:PrototypeParser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#catchProduction.
    def visitCatchProduction(self, ctx:PrototypeParser.CatchProductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#finallyProduction.
    def visitFinallyProduction(self, ctx:PrototypeParser.FinallyProductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#debuggerStatement.
    def visitDebuggerStatement(self, ctx:PrototypeParser.DebuggerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:PrototypeParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#classDeclaration.
    def visitClassDeclaration(self, ctx:PrototypeParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#classTail.
    def visitClassTail(self, ctx:PrototypeParser.ClassTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#classElement.
    def visitClassElement(self, ctx:PrototypeParser.ClassElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#methodDefinition.
    def visitMethodDefinition(self, ctx:PrototypeParser.MethodDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#fieldDefinition.
    def visitFieldDefinition(self, ctx:PrototypeParser.FieldDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#classElementName.
    def visitClassElementName(self, ctx:PrototypeParser.ClassElementNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#privateIdentifier.
    def visitPrivateIdentifier(self, ctx:PrototypeParser.PrivateIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#formalParameterList.
    def visitFormalParameterList(self, ctx:PrototypeParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#formalParameterArg.
    def visitFormalParameterArg(self, ctx:PrototypeParser.FormalParameterArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#lastFormalParameterArg.
    def visitLastFormalParameterArg(self, ctx:PrototypeParser.LastFormalParameterArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#functionBody.
    def visitFunctionBody(self, ctx:PrototypeParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#sourceElements.
    def visitSourceElements(self, ctx:PrototypeParser.SourceElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:PrototypeParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#elementList.
    def visitElementList(self, ctx:PrototypeParser.ElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#arrayElement.
    def visitArrayElement(self, ctx:PrototypeParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#PropertyExpressionAssignment.
    def visitPropertyExpressionAssignment(self, ctx:PrototypeParser.PropertyExpressionAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ComputedPropertyExpressionAssignment.
    def visitComputedPropertyExpressionAssignment(self, ctx:PrototypeParser.ComputedPropertyExpressionAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#FunctionProperty.
    def visitFunctionProperty(self, ctx:PrototypeParser.FunctionPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#PropertyGetter.
    def visitPropertyGetter(self, ctx:PrototypeParser.PropertyGetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#PropertySetter.
    def visitPropertySetter(self, ctx:PrototypeParser.PropertySetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#PropertyShorthand.
    def visitPropertyShorthand(self, ctx:PrototypeParser.PropertyShorthandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#propertyName.
    def visitPropertyName(self, ctx:PrototypeParser.PropertyNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#arguments.
    def visitArguments(self, ctx:PrototypeParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#argument.
    def visitArgument(self, ctx:PrototypeParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#expressionSequence.
    def visitExpressionSequence(self, ctx:PrototypeParser.ExpressionSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#TemplateStringExpression.
    def visitTemplateStringExpression(self, ctx:PrototypeParser.TemplateStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#TernaryExpression.
    def visitTernaryExpression(self, ctx:PrototypeParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx:PrototypeParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#PowerExpression.
    def visitPowerExpression(self, ctx:PrototypeParser.PowerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#PreIncrementExpression.
    def visitPreIncrementExpression(self, ctx:PrototypeParser.PreIncrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ObjectLiteralExpression.
    def visitObjectLiteralExpression(self, ctx:PrototypeParser.ObjectLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#MetaExpression.
    def visitMetaExpression(self, ctx:PrototypeParser.MetaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#InExpression.
    def visitInExpression(self, ctx:PrototypeParser.InExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx:PrototypeParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#OptionalChainExpression.
    def visitOptionalChainExpression(self, ctx:PrototypeParser.OptionalChainExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#NotExpression.
    def visitNotExpression(self, ctx:PrototypeParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#PreDecreaseExpression.
    def visitPreDecreaseExpression(self, ctx:PrototypeParser.PreDecreaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx:PrototypeParser.ArgumentsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#AwaitExpression.
    def visitAwaitExpression(self, ctx:PrototypeParser.AwaitExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ThisExpression.
    def visitThisExpression(self, ctx:PrototypeParser.ThisExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#FunctionExpression.
    def visitFunctionExpression(self, ctx:PrototypeParser.FunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#UnaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:PrototypeParser.UnaryMinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:PrototypeParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#PostDecreaseExpression.
    def visitPostDecreaseExpression(self, ctx:PrototypeParser.PostDecreaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#TypeofExpression.
    def visitTypeofExpression(self, ctx:PrototypeParser.TypeofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#InstanceofExpression.
    def visitInstanceofExpression(self, ctx:PrototypeParser.InstanceofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#UnaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx:PrototypeParser.UnaryPlusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#DeleteExpression.
    def visitDeleteExpression(self, ctx:PrototypeParser.DeleteExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ImportExpression.
    def visitImportExpression(self, ctx:PrototypeParser.ImportExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#EqualityExpression.
    def visitEqualityExpression(self, ctx:PrototypeParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#BitXOrExpression.
    def visitBitXOrExpression(self, ctx:PrototypeParser.BitXOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#SuperExpression.
    def visitSuperExpression(self, ctx:PrototypeParser.SuperExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:PrototypeParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#BitShiftExpression.
    def visitBitShiftExpression(self, ctx:PrototypeParser.BitShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:PrototypeParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx:PrototypeParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#RelationalExpression.
    def visitRelationalExpression(self, ctx:PrototypeParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#PostIncrementExpression.
    def visitPostIncrementExpression(self, ctx:PrototypeParser.PostIncrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#YieldExpression.
    def visitYieldExpression(self, ctx:PrototypeParser.YieldExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#BitNotExpression.
    def visitBitNotExpression(self, ctx:PrototypeParser.BitNotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#NewExpression.
    def visitNewExpression(self, ctx:PrototypeParser.NewExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#LiteralExpression.
    def visitLiteralExpression(self, ctx:PrototypeParser.LiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx:PrototypeParser.ArrayLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx:PrototypeParser.MemberDotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ClassExpression.
    def visitClassExpression(self, ctx:PrototypeParser.ClassExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#MemberIndexExpression.
    def visitMemberIndexExpression(self, ctx:PrototypeParser.MemberIndexExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:PrototypeParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#BitAndExpression.
    def visitBitAndExpression(self, ctx:PrototypeParser.BitAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#BitOrExpression.
    def visitBitOrExpression(self, ctx:PrototypeParser.BitOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#AssignmentOperatorExpression.
    def visitAssignmentOperatorExpression(self, ctx:PrototypeParser.AssignmentOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#VoidExpression.
    def visitVoidExpression(self, ctx:PrototypeParser.VoidExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#CoalesceExpression.
    def visitCoalesceExpression(self, ctx:PrototypeParser.CoalesceExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#initializer.
    def visitInitializer(self, ctx:PrototypeParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#assignable.
    def visitAssignable(self, ctx:PrototypeParser.AssignableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#objectLiteral.
    def visitObjectLiteral(self, ctx:PrototypeParser.ObjectLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#NamedFunction.
    def visitNamedFunction(self, ctx:PrototypeParser.NamedFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#AnonymousFunctionDecl.
    def visitAnonymousFunctionDecl(self, ctx:PrototypeParser.AnonymousFunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#ArrowFunction.
    def visitArrowFunction(self, ctx:PrototypeParser.ArrowFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#arrowFunctionParameters.
    def visitArrowFunctionParameters(self, ctx:PrototypeParser.ArrowFunctionParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#arrowFunctionBody.
    def visitArrowFunctionBody(self, ctx:PrototypeParser.ArrowFunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:PrototypeParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#literal.
    def visitLiteral(self, ctx:PrototypeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#templateStringLiteral.
    def visitTemplateStringLiteral(self, ctx:PrototypeParser.TemplateStringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#templateStringAtom.
    def visitTemplateStringAtom(self, ctx:PrototypeParser.TemplateStringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#numericLiteral.
    def visitNumericLiteral(self, ctx:PrototypeParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#bigintLiteral.
    def visitBigintLiteral(self, ctx:PrototypeParser.BigintLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#getter.
    def visitGetter(self, ctx:PrototypeParser.GetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#setter.
    def visitSetter(self, ctx:PrototypeParser.SetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#identifierName.
    def visitIdentifierName(self, ctx:PrototypeParser.IdentifierNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#identifier.
    def visitIdentifier(self, ctx:PrototypeParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#reservedWord.
    def visitReservedWord(self, ctx:PrototypeParser.ReservedWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#keyword.
    def visitKeyword(self, ctx:PrototypeParser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#let_.
    def visitLet_(self, ctx:PrototypeParser.Let_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrototypeParser#eos.
    def visitEos(self, ctx:PrototypeParser.EosContext):
        return self.visitChildren(ctx)



del PrototypeParser