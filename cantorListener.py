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


    # Enter a parse tree produced by cantorParser#Comp.
    def enterComp(self, ctx:cantorParser.CompContext):
        pass

    # Exit a parse tree produced by cantorParser#Comp.
    def exitComp(self, ctx:cantorParser.CompContext):
        pass


    # Enter a parse tree produced by cantorParser#Pair.
    def enterPair(self, ctx:cantorParser.PairContext):
        pass

    # Exit a parse tree produced by cantorParser#Pair.
    def exitPair(self, ctx:cantorParser.PairContext):
        pass


    # Enter a parse tree produced by cantorParser#Compair.
    def enterCompair(self, ctx:cantorParser.CompairContext):
        pass

    # Exit a parse tree produced by cantorParser#Compair.
    def exitCompair(self, ctx:cantorParser.CompairContext):
        pass


    # Enter a parse tree produced by cantorParser#Mu.
    def enterMu(self, ctx:cantorParser.MuContext):
        pass

    # Exit a parse tree produced by cantorParser#Mu.
    def exitMu(self, ctx:cantorParser.MuContext):
        pass


    # Enter a parse tree produced by cantorParser#Primrec.
    def enterPrimrec(self, ctx:cantorParser.PrimrecContext):
        pass

    # Exit a parse tree produced by cantorParser#Primrec.
    def exitPrimrec(self, ctx:cantorParser.PrimrecContext):
        pass


    # Enter a parse tree produced by cantorParser#Alias.
    def enterAlias(self, ctx:cantorParser.AliasContext):
        pass

    # Exit a parse tree produced by cantorParser#Alias.
    def exitAlias(self, ctx:cantorParser.AliasContext):
        pass



del cantorParser