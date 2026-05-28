# Generated from cantor.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\5\4#\n\4\3\5\3\5\3\5")
        buf.write("\5\5(\n\5\3\6\3\6\3\6\5\6-\n\6\3\7\3\7\5\7\61\n\7\3\b")
        buf.write("\3\b\3\b\5\b\66\n\b\3\b\5\b9\n\b\3\b\7\b<\n\b\f\b\16\b")
        buf.write("?\13\b\3\b\3\b\5\bC\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tV\n\t\3\t\2")
        buf.write("\2\n\2\4\6\b\n\f\16\20\2\2\2`\2\25\3\2\2\2\4\35\3\2\2")
        buf.write("\2\6\"\3\2\2\2\b$\3\2\2\2\n)\3\2\2\2\f.\3\2\2\2\16\62")
        buf.write("\3\2\2\2\20U\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2\24\27")
        buf.write("\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2\2\27")
        buf.write("\25\3\2\2\2\30\31\7\2\2\3\31\3\3\2\2\2\32\36\5\6\4\2\33")
        buf.write("\36\5\16\b\2\34\36\7\17\2\2\35\32\3\2\2\2\35\33\3\2\2")
        buf.write("\2\35\34\3\2\2\2\36\5\3\2\2\2\37#\5\b\5\2 #\5\n\6\2!#")
        buf.write("\5\f\7\2\"\37\3\2\2\2\" \3\2\2\2\"!\3\2\2\2#\7\3\2\2\2")
        buf.write("$%\7\3\2\2%\'\7\16\2\2&(\7\17\2\2\'&\3\2\2\2\'(\3\2\2")
        buf.write("\2(\t\3\2\2\2)*\7\4\2\2*,\7\16\2\2+-\7\17\2\2,+\3\2\2")
        buf.write("\2,-\3\2\2\2-\13\3\2\2\2.\60\7\5\2\2/\61\7\17\2\2\60/")
        buf.write("\3\2\2\2\60\61\3\2\2\2\61\r\3\2\2\2\62\63\7\6\2\2\63\65")
        buf.write("\7\16\2\2\64\66\7\17\2\2\65\64\3\2\2\2\65\66\3\2\2\2\66")
        buf.write("8\3\2\2\2\679\7\f\2\28\67\3\2\2\289\3\2\2\29=\3\2\2\2")
        buf.write(":<\7\17\2\2;:\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>@")
        buf.write("\3\2\2\2?=\3\2\2\2@B\5\20\t\2AC\7\17\2\2BA\3\2\2\2BC\3")
        buf.write("\2\2\2C\17\3\2\2\2DE\7\7\2\2EF\7\16\2\2FV\7\16\2\2GH\7")
        buf.write("\b\2\2HI\7\16\2\2IV\7\16\2\2JK\7\t\2\2KL\7\16\2\2LM\7")
        buf.write("\16\2\2MV\7\16\2\2NO\7\n\2\2OV\7\16\2\2PQ\7\13\2\2QR\7")
        buf.write("\16\2\2RS\7\16\2\2SV\7\16\2\2TV\7\16\2\2UD\3\2\2\2UG\3")
        buf.write("\2\2\2UJ\3\2\2\2UN\3\2\2\2UP\3\2\2\2UT\3\2\2\2V\21\3\2")
        buf.write("\2\2\r\25\35\"\',\60\658=BU")
        return buf.getvalue()


class cantorParser ( Parser ):

    grammarFileName = "cantor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'import'", "'extended'", "'define'", 
                     "'comp'", "'pair'", "'compair'", "'mu'", "'primrec'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "DOC", "COMMENT", "ID", 
                      "NL", "WS", "LEXICAL_ERROR" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_directive = 2
    RULE_main_directive = 3
    RULE_import_directive = 4
    RULE_extended_directive = 5
    RULE_function_def = 6
    RULE_operation = 7

    ruleNames =  [ "prog", "line", "directive", "main_directive", "import_directive", 
                   "extended_directive", "function_def", "operation" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    DOC=10
    COMMENT=11
    ID=12
    NL=13
    WS=14
    LEXICAL_ERROR=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(cantorParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cantorParser.LineContext)
            else:
                return self.getTypedRuleContext(cantorParser.LineContext,i)


        def getRuleIndex(self):
            return cantorParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = cantorParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cantorParser.T__0) | (1 << cantorParser.T__1) | (1 << cantorParser.T__2) | (1 << cantorParser.T__3) | (1 << cantorParser.NL))) != 0):
                self.state = 16
                self.line()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(cantorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def directive(self):
            return self.getTypedRuleContext(cantorParser.DirectiveContext,0)


        def function_def(self):
            return self.getTypedRuleContext(cantorParser.Function_defContext,0)


        def NL(self):
            return self.getToken(cantorParser.NL, 0)

        def getRuleIndex(self):
            return cantorParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = cantorParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cantorParser.T__0, cantorParser.T__1, cantorParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.directive()
                pass
            elif token in [cantorParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.function_def()
                pass
            elif token in [cantorParser.NL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.match(cantorParser.NL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_directive(self):
            return self.getTypedRuleContext(cantorParser.Main_directiveContext,0)


        def import_directive(self):
            return self.getTypedRuleContext(cantorParser.Import_directiveContext,0)


        def extended_directive(self):
            return self.getTypedRuleContext(cantorParser.Extended_directiveContext,0)


        def getRuleIndex(self):
            return cantorParser.RULE_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective" ):
                listener.enterDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective" ):
                listener.exitDirective(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective" ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = cantorParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_directive)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cantorParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.main_directive()
                pass
            elif token in [cantorParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.import_directive()
                pass
            elif token in [cantorParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.extended_directive()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Main_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(cantorParser.ID, 0)

        def NL(self):
            return self.getToken(cantorParser.NL, 0)

        def getRuleIndex(self):
            return cantorParser.RULE_main_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_directive" ):
                listener.enterMain_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_directive" ):
                listener.exitMain_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_directive" ):
                return visitor.visitMain_directive(self)
            else:
                return visitor.visitChildren(self)




    def main_directive(self):

        localctx = cantorParser.Main_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_main_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(cantorParser.T__0)
            self.state = 35
            self.match(cantorParser.ID)
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 36
                self.match(cantorParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Import_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(cantorParser.ID, 0)

        def NL(self):
            return self.getToken(cantorParser.NL, 0)

        def getRuleIndex(self):
            return cantorParser.RULE_import_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_directive" ):
                listener.enterImport_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_directive" ):
                listener.exitImport_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_directive" ):
                return visitor.visitImport_directive(self)
            else:
                return visitor.visitChildren(self)




    def import_directive(self):

        localctx = cantorParser.Import_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_import_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(cantorParser.T__1)
            self.state = 40
            self.match(cantorParser.ID)
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 41
                self.match(cantorParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Extended_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(cantorParser.NL, 0)

        def getRuleIndex(self):
            return cantorParser.RULE_extended_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtended_directive" ):
                listener.enterExtended_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtended_directive" ):
                listener.exitExtended_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtended_directive" ):
                return visitor.visitExtended_directive(self)
            else:
                return visitor.visitChildren(self)




    def extended_directive(self):

        localctx = cantorParser.Extended_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_extended_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(cantorParser.T__2)
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 45
                self.match(cantorParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(cantorParser.ID, 0)

        def operation(self):
            return self.getTypedRuleContext(cantorParser.OperationContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(cantorParser.NL)
            else:
                return self.getToken(cantorParser.NL, i)

        def DOC(self):
            return self.getToken(cantorParser.DOC, 0)

        def getRuleIndex(self):
            return cantorParser.RULE_function_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_def" ):
                listener.enterFunction_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_def" ):
                listener.exitFunction_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_def" ):
                return visitor.visitFunction_def(self)
            else:
                return visitor.visitChildren(self)




    def function_def(self):

        localctx = cantorParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(cantorParser.T__3)
            self.state = 49
            self.match(cantorParser.ID)
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 50
                self.match(cantorParser.NL)


            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cantorParser.DOC:
                self.state = 53
                self.match(cantorParser.DOC)


            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cantorParser.NL:
                self.state = 56
                self.match(cantorParser.NL)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.operation()
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 63
                self.match(cantorParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cantorParser.RULE_operation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CompairContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cantorParser.OperationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(cantorParser.ID)
            else:
                return self.getToken(cantorParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompair" ):
                listener.enterCompair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompair" ):
                listener.exitCompair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompair" ):
                return visitor.visitCompair(self)
            else:
                return visitor.visitChildren(self)


    class AliasContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cantorParser.OperationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(cantorParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlias" ):
                listener.enterAlias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlias" ):
                listener.exitAlias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlias" ):
                return visitor.visitAlias(self)
            else:
                return visitor.visitChildren(self)


    class MuContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cantorParser.OperationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(cantorParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMu" ):
                listener.enterMu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMu" ):
                listener.exitMu(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMu" ):
                return visitor.visitMu(self)
            else:
                return visitor.visitChildren(self)


    class CompContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cantorParser.OperationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(cantorParser.ID)
            else:
                return self.getToken(cantorParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)


    class PairContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cantorParser.OperationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(cantorParser.ID)
            else:
                return self.getToken(cantorParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)


    class PrimrecContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cantorParser.OperationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(cantorParser.ID)
            else:
                return self.getToken(cantorParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimrec" ):
                listener.enterPrimrec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimrec" ):
                listener.exitPrimrec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimrec" ):
                return visitor.visitPrimrec(self)
            else:
                return visitor.visitChildren(self)



    def operation(self):

        localctx = cantorParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operation)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cantorParser.T__4]:
                localctx = cantorParser.CompContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(cantorParser.T__4)
                self.state = 67
                self.match(cantorParser.ID)
                self.state = 68
                self.match(cantorParser.ID)
                pass
            elif token in [cantorParser.T__5]:
                localctx = cantorParser.PairContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(cantorParser.T__5)
                self.state = 70
                self.match(cantorParser.ID)
                self.state = 71
                self.match(cantorParser.ID)
                pass
            elif token in [cantorParser.T__6]:
                localctx = cantorParser.CompairContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.match(cantorParser.T__6)
                self.state = 73
                self.match(cantorParser.ID)
                self.state = 74
                self.match(cantorParser.ID)
                self.state = 75
                self.match(cantorParser.ID)
                pass
            elif token in [cantorParser.T__7]:
                localctx = cantorParser.MuContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.match(cantorParser.T__7)
                self.state = 77
                self.match(cantorParser.ID)
                pass
            elif token in [cantorParser.T__8]:
                localctx = cantorParser.PrimrecContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.match(cantorParser.T__8)
                self.state = 79
                self.match(cantorParser.ID)
                self.state = 80
                self.match(cantorParser.ID)
                self.state = 81
                self.match(cantorParser.ID)
                pass
            elif token in [cantorParser.ID]:
                localctx = cantorParser.AliasContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 82
                self.match(cantorParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





