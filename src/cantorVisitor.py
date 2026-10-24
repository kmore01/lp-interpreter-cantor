# Generated from cantor.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cantorParser import cantorParser
else:
    from cantorParser import cantorParser

# This class defines a complete generic visitor for a parse tree produced by cantorParser.

class cantorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cantorParser#prog.
    def visitProg(self, ctx:cantorParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cantorParser#line.
    def visitLine(self, ctx:cantorParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cantorParser#main_directive.
    def visitMain_directive(self, ctx:cantorParser.Main_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cantorParser#import_directive.
    def visitImport_directive(self, ctx:cantorParser.Import_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cantorParser#extended_directive.
    def visitExtended_directive(self, ctx:cantorParser.Extended_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cantorParser#function_def.
    def visitFunction_def(self, ctx:cantorParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cantorParser#Comp.
    def visitComp(self, ctx:cantorParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cantorParser#Pair.
    def visitPair(self, ctx:cantorParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cantorParser#Compair.
    def visitCompair(self, ctx:cantorParser.CompairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cantorParser#Mu.
    def visitMu(self, ctx:cantorParser.MuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cantorParser#Primrec.
    def visitPrimrec(self, ctx:cantorParser.PrimrecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cantorParser#Alias.
    def visitAlias(self, ctx:cantorParser.AliasContext):
        return self.visitChildren(ctx)



del cantorParser