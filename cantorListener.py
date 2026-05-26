# Generated from cantor.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cantorParser import cantorParser
else:
    from cantorParser import cantorParser

# This class defines a complete listener for a parse tree produced by cantorParser.
class cantorListener(ParseTreeListener):

    # Enter a parse tree produced by cantorParser#prog.
    def enterProg(self, ctx:cantorParser.ProgContext):
        pass

    # Exit a parse tree produced by cantorParser#prog.
    def exitProg(self, ctx:cantorParser.ProgContext):
        pass


    # Enter a parse tree produced by cantorParser#line.
    def enterLine(self, ctx:cantorParser.LineContext):
        pass

    # Exit a parse tree produced by cantorParser#line.
    def exitLine(self, ctx:cantorParser.LineContext):
        pass


    # Enter a parse tree produced by cantorParser#directive.
    def enterDirective(self, ctx:cantorParser.DirectiveContext):
        pass

    # Exit a parse tree produced by cantorParser#directive.
    def exitDirective(self, ctx:cantorParser.DirectiveContext):
        pass


    # Enter a parse tree produced by cantorParser#main_directive.
    def enterMain_directive(self, ctx:cantorParser.Main_directiveContext):
        pass

    # Exit a parse tree produced by cantorParser#main_directive.
    def exitMain_directive(self, ctx:cantorParser.Main_directiveContext):
        pass


    # Enter a parse tree produced by cantorParser#import_directive.
    def enterImport_directive(self, ctx:cantorParser.Import_directiveContext):
        pass

    # Exit a parse tree produced by cantorParser#import_directive.
    def exitImport_directive(self, ctx:cantorParser.Import_directiveContext):
        pass


    # Enter a parse tree produced by cantorParser#extended_directive.
    def enterExtended_directive(self, ctx:cantorParser.Extended_directiveContext):
        pass

    # Exit a parse tree produced by cantorParser#extended_directive.
    def exitExtended_directive(self, ctx:cantorParser.Extended_directiveContext):
        pass


    # Enter a parse tree produced by cantorParser#function_def.
    def enterFunction_def(self, ctx:cantorParser.Function_defContext):
        pass

    # Exit a parse tree produced by cantorParser#function_def.
    def exitFunction_def(self, ctx:cantorParser.Function_defContext):
        pass


    # Enter a parse tree produced by cantorParser#CompOp.
    def enterCompOp(self, ctx:cantorParser.CompOpContext):
        pass

    # Exit a parse tree produced by cantorParser#CompOp.
    def exitCompOp(self, ctx:cantorParser.CompOpContext):
        pass


    # Enter a parse tree produced by cantorParser#PairOp.
    def enterPairOp(self, ctx:cantorParser.PairOpContext):
        pass

    # Exit a parse tree produced by cantorParser#PairOp.
    def exitPairOp(self, ctx:cantorParser.PairOpContext):
        pass


    # Enter a parse tree produced by cantorParser#CompairOp.
    def enterCompairOp(self, ctx:cantorParser.CompairOpContext):
        pass

    # Exit a parse tree produced by cantorParser#CompairOp.
    def exitCompairOp(self, ctx:cantorParser.CompairOpContext):
        pass


    # Enter a parse tree produced by cantorParser#MuOp.
    def enterMuOp(self, ctx:cantorParser.MuOpContext):
        pass

    # Exit a parse tree produced by cantorParser#MuOp.
    def exitMuOp(self, ctx:cantorParser.MuOpContext):
        pass


    # Enter a parse tree produced by cantorParser#PrimrecOp.
    def enterPrimrecOp(self, ctx:cantorParser.PrimrecOpContext):
        pass

    # Exit a parse tree produced by cantorParser#PrimrecOp.
    def exitPrimrecOp(self, ctx:cantorParser.PrimrecOpContext):
        pass


    # Enter a parse tree produced by cantorParser#AliasOp.
    def enterAliasOp(self, ctx:cantorParser.AliasOpContext):
        pass

    # Exit a parse tree produced by cantorParser#AliasOp.
    def exitAliasOp(self, ctx:cantorParser.AliasOpContext):
        pass



del cantorParser