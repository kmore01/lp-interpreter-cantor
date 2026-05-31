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
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\3\2\7\2\31\n")
        buf.write("\2\f\2\16\2\34\13\2\3\2\5\2\37\n\2\3\2\7\2\"\n\2\f\2\16")
        buf.write("\2%\13\2\3\2\7\2(\n\2\f\2\16\2+\13\2\3\2\3\2\3\3\3\3\5")
        buf.write("\3\61\n\3\3\4\3\4\3\4\5\4\66\n\4\3\5\3\5\3\5\5\5;\n\5")
        buf.write("\3\6\3\6\5\6?\n\6\3\7\3\7\3\7\5\7D\n\7\3\7\5\7G\n\7\3")
        buf.write("\7\7\7J\n\7\f\7\16\7M\13\7\3\7\3\7\5\7Q\n\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\5\bd\n\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2p\2\23\3\2")
        buf.write("\2\2\4\60\3\2\2\2\6\62\3\2\2\2\b\67\3\2\2\2\n<\3\2\2\2")
        buf.write("\f@\3\2\2\2\16c\3\2\2\2\20\22\7\17\2\2\21\20\3\2\2\2\22")
        buf.write("\25\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\26\3\2\2\2")
        buf.write("\25\23\3\2\2\2\26\32\5\6\4\2\27\31\7\17\2\2\30\27\3\2")
        buf.write("\2\2\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\36\3")
        buf.write("\2\2\2\34\32\3\2\2\2\35\37\5\n\6\2\36\35\3\2\2\2\36\37")
        buf.write("\3\2\2\2\37#\3\2\2\2 \"\5\b\5\2! \3\2\2\2\"%\3\2\2\2#")
        buf.write("!\3\2\2\2#$\3\2\2\2$)\3\2\2\2%#\3\2\2\2&(\5\4\3\2\'&\3")
        buf.write("\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*,\3\2\2\2+)\3\2")
        buf.write("\2\2,-\7\2\2\3-\3\3\2\2\2.\61\5\f\7\2/\61\7\17\2\2\60")
        buf.write(".\3\2\2\2\60/\3\2\2\2\61\5\3\2\2\2\62\63\7\3\2\2\63\65")
        buf.write("\7\16\2\2\64\66\7\17\2\2\65\64\3\2\2\2\65\66\3\2\2\2\66")
        buf.write("\7\3\2\2\2\678\7\4\2\28:\7\16\2\29;\7\17\2\2:9\3\2\2\2")
        buf.write(":;\3\2\2\2;\t\3\2\2\2<>\7\5\2\2=?\7\17\2\2>=\3\2\2\2>")
        buf.write("?\3\2\2\2?\13\3\2\2\2@A\7\6\2\2AC\7\16\2\2BD\7\17\2\2")
        buf.write("CB\3\2\2\2CD\3\2\2\2DF\3\2\2\2EG\7\f\2\2FE\3\2\2\2FG\3")
        buf.write("\2\2\2GK\3\2\2\2HJ\7\17\2\2IH\3\2\2\2JM\3\2\2\2KI\3\2")
        buf.write("\2\2KL\3\2\2\2LN\3\2\2\2MK\3\2\2\2NP\5\16\b\2OQ\7\17\2")
        buf.write("\2PO\3\2\2\2PQ\3\2\2\2Q\r\3\2\2\2RS\7\7\2\2ST\7\16\2\2")
        buf.write("Td\7\16\2\2UV\7\b\2\2VW\7\16\2\2Wd\7\16\2\2XY\7\t\2\2")
        buf.write("YZ\7\16\2\2Z[\7\16\2\2[d\7\16\2\2\\]\7\n\2\2]d\7\16\2")
        buf.write("\2^_\7\13\2\2_`\7\16\2\2`a\7\16\2\2ad\7\16\2\2bd\7\16")
        buf.write("\2\2cR\3\2\2\2cU\3\2\2\2cX\3\2\2\2c\\\3\2\2\2c^\3\2\2")
        buf.write("\2cb\3\2\2\2d\17\3\2\2\2\20\23\32\36#)\60\65:>CFKPc")
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
    RULE_main_directive = 2
    RULE_import_directive = 3
    RULE_extended_directive = 4
    RULE_function_def = 5
    RULE_operation = 6

    ruleNames =  [ "prog", "line", "main_directive", "import_directive", 
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

        def main_directive(self):
            return self.getTypedRuleContext(cantorParser.Main_directiveContext,0)


        def EOF(self):
            return self.getToken(cantorParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(cantorParser.NL)
            else:
                return self.getToken(cantorParser.NL, i)

        def extended_directive(self):
            return self.getTypedRuleContext(cantorParser.Extended_directiveContext,0)


        def import_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cantorParser.Import_directiveContext)
            else:
                return self.getTypedRuleContext(cantorParser.Import_directiveContext,i)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cantorParser.LineContext)
            else:
                return self.getTypedRuleContext(cantorParser.LineContext,i)


        def getRuleIndex(self):
            return cantorParser.RULE_prog

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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cantorParser.NL:
                self.state = 14
                self.match(cantorParser.NL)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.main_directive()
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 21
                    self.match(cantorParser.NL) 
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cantorParser.T__2:
                self.state = 27
                self.extended_directive()


            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cantorParser.T__1:
                self.state = 30
                self.import_directive()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cantorParser.T__3 or _la==cantorParser.NL:
                self.state = 36
                self.line()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
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

        def function_def(self):
            return self.getTypedRuleContext(cantorParser.Function_defContext,0)


        def NL(self):
            return self.getToken(cantorParser.NL, 0)

        def getRuleIndex(self):
            return cantorParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = cantorParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cantorParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.function_def()
                pass
            elif token in [cantorParser.NL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_directive" ):
                return visitor.visitMain_directive(self)
            else:
                return visitor.visitChildren(self)




    def main_directive(self):

        localctx = cantorParser.Main_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(cantorParser.T__0)
            self.state = 49
            self.match(cantorParser.ID)
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 50
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_directive" ):
                return visitor.visitImport_directive(self)
            else:
                return visitor.visitChildren(self)




    def import_directive(self):

        localctx = cantorParser.Import_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_import_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(cantorParser.T__1)
            self.state = 54
            self.match(cantorParser.ID)
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 55
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtended_directive" ):
                return visitor.visitExtended_directive(self)
            else:
                return visitor.visitChildren(self)




    def extended_directive(self):

        localctx = cantorParser.Extended_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_extended_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(cantorParser.T__2)
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 59
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_def" ):
                return visitor.visitFunction_def(self)
            else:
                return visitor.visitChildren(self)




    def function_def(self):

        localctx = cantorParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(cantorParser.T__3)
            self.state = 63
            self.match(cantorParser.ID)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 64
                self.match(cantorParser.NL)


            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cantorParser.DOC:
                self.state = 67
                self.match(cantorParser.DOC)


            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cantorParser.NL:
                self.state = 70
                self.match(cantorParser.NL)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.operation()
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 77
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimrec" ):
                return visitor.visitPrimrec(self)
            else:
                return visitor.visitChildren(self)



    def operation(self):

        localctx = cantorParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operation)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cantorParser.T__4]:
                localctx = cantorParser.CompContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(cantorParser.T__4)
                self.state = 81
                self.match(cantorParser.ID)
                self.state = 82
                self.match(cantorParser.ID)
                pass
            elif token in [cantorParser.T__5]:
                localctx = cantorParser.PairContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(cantorParser.T__5)
                self.state = 84
                self.match(cantorParser.ID)
                self.state = 85
                self.match(cantorParser.ID)
                pass
            elif token in [cantorParser.T__6]:
                localctx = cantorParser.CompairContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.match(cantorParser.T__6)
                self.state = 87
                self.match(cantorParser.ID)
                self.state = 88
                self.match(cantorParser.ID)
                self.state = 89
                self.match(cantorParser.ID)
                pass
            elif token in [cantorParser.T__7]:
                localctx = cantorParser.MuContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.match(cantorParser.T__7)
                self.state = 91
                self.match(cantorParser.ID)
                pass
            elif token in [cantorParser.T__8]:
                localctx = cantorParser.PrimrecContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.match(cantorParser.T__8)
                self.state = 93
                self.match(cantorParser.ID)
                self.state = 94
                self.match(cantorParser.ID)
                self.state = 95
                self.match(cantorParser.ID)
                pass
            elif token in [cantorParser.ID]:
                localctx = cantorParser.AliasContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 96
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





