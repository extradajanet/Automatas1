# Generated from PytoJava.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("`\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2\32\n\2")
        buf.write("\r\2\16\2\33\3\3\3\3\3\3\3\3\5\3\"\n\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\7\4+\n\4\f\4\16\4.\13\4\3\5\6\5\61\n\5\r")
        buf.write("\5\16\5\62\3\6\3\6\3\6\5\68\n\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\5\tF\n\t\3\n\3\n\3\n\7\nK\n")
        buf.write("\n\f\n\16\nN\13\n\3\13\3\13\3\13\7\13S\n\13\f\13\16\13")
        buf.write("V\13\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f^\n\f\3\f\2\2\r\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\2\2\2_\2\31\3\2\2\2\4\35\3\2\2")
        buf.write("\2\6\'\3\2\2\2\b\60\3\2\2\2\n\67\3\2\2\2\f9\3\2\2\2\16")
        buf.write("<\3\2\2\2\20E\3\2\2\2\22G\3\2\2\2\24O\3\2\2\2\26]\3\2")
        buf.write("\2\2\30\32\5\4\3\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3")
        buf.write("\2\2\2\33\34\3\2\2\2\34\3\3\2\2\2\35\36\7\3\2\2\36\37")
        buf.write("\7\r\2\2\37!\7\7\2\2 \"\5\6\4\2! \3\2\2\2!\"\3\2\2\2\"")
        buf.write("#\3\2\2\2#$\7\b\2\2$%\7\t\2\2%&\5\b\5\2&\5\3\2\2\2\',")
        buf.write("\7\r\2\2()\7\6\2\2)+\7\r\2\2*(\3\2\2\2+.\3\2\2\2,*\3\2")
        buf.write("\2\2,-\3\2\2\2-\7\3\2\2\2.,\3\2\2\2/\61\5\n\6\2\60/\3")
        buf.write("\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\t")
        buf.write("\3\2\2\2\648\5\f\7\2\658\5\16\b\2\668\5\20\t\2\67\64\3")
        buf.write("\2\2\2\67\65\3\2\2\2\67\66\3\2\2\28\13\3\2\2\29:\7\4\2")
        buf.write("\2:;\5\22\n\2;\r\3\2\2\2<=\7\5\2\2=>\7\7\2\2>?\5\22\n")
        buf.write("\2?@\7\b\2\2@\17\3\2\2\2AB\7\r\2\2BC\7\n\2\2CF\5\22\n")
        buf.write("\2DF\5\22\n\2EA\3\2\2\2ED\3\2\2\2F\21\3\2\2\2GL\5\24\13")
        buf.write("\2HI\7\f\2\2IK\5\24\13\2JH\3\2\2\2KN\3\2\2\2LJ\3\2\2\2")
        buf.write("LM\3\2\2\2M\23\3\2\2\2NL\3\2\2\2OT\5\26\f\2PQ\7\13\2\2")
        buf.write("QS\5\26\f\2RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\25")
        buf.write("\3\2\2\2VT\3\2\2\2W^\7\16\2\2X^\7\r\2\2YZ\7\7\2\2Z[\5")
        buf.write("\22\n\2[\\\7\b\2\2\\^\3\2\2\2]W\3\2\2\2]X\3\2\2\2]Y\3")
        buf.write("\2\2\2^\27\3\2\2\2\13\33!,\62\67ELT]")
        return buf.getvalue()


class PytoJavaParser ( Parser ):

    grammarFileName = "PytoJava.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "'print'", "','", 
                     "'('", "')'", "':'", "'='", "'*'", "'-'" ]

    symbolicNames = [ "<INVALID>", "DEF", "RETURN", "PRINT", "COMMA", "LPAREN", 
                      "RPAREN", "COLON", "ASSIGN", "MUL", "SUB", "ID", "NUMBER", 
                      "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_functionDef = 1
    RULE_parameters = 2
    RULE_statements = 3
    RULE_statement = 4
    RULE_returnStmt = 5
    RULE_printStmt = 6
    RULE_exprStmt = 7
    RULE_expression = 8
    RULE_mulExpr = 9
    RULE_atom = 10

    ruleNames =  [ "program", "functionDef", "parameters", "statements", 
                   "statement", "returnStmt", "printStmt", "exprStmt", "expression", 
                   "mulExpr", "atom" ]

    EOF = Token.EOF
    DEF=1
    RETURN=2
    PRINT=3
    COMMA=4
    LPAREN=5
    RPAREN=6
    COLON=7
    ASSIGN=8
    MUL=9
    SUB=10
    ID=11
    NUMBER=12
    NEWLINE=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PytoJavaParser.FunctionDefContext)
            else:
                return self.getTypedRuleContext(PytoJavaParser.FunctionDefContext,i)


        def getRuleIndex(self):
            return PytoJavaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = PytoJavaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.functionDef()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PytoJavaParser.DEF):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(PytoJavaParser.DEF, 0)

        def ID(self):
            return self.getToken(PytoJavaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(PytoJavaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PytoJavaParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(PytoJavaParser.COLON, 0)

        def statements(self):
            return self.getTypedRuleContext(PytoJavaParser.StatementsContext,0)


        def parameters(self):
            return self.getTypedRuleContext(PytoJavaParser.ParametersContext,0)


        def getRuleIndex(self):
            return PytoJavaParser.RULE_functionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)




    def functionDef(self):

        localctx = PytoJavaParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(PytoJavaParser.DEF)
            self.state = 28
            self.match(PytoJavaParser.ID)
            self.state = 29
            self.match(PytoJavaParser.LPAREN)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PytoJavaParser.ID:
                self.state = 30
                self.parameters()


            self.state = 33
            self.match(PytoJavaParser.RPAREN)
            self.state = 34
            self.match(PytoJavaParser.COLON)
            self.state = 35
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PytoJavaParser.ID)
            else:
                return self.getToken(PytoJavaParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PytoJavaParser.COMMA)
            else:
                return self.getToken(PytoJavaParser.COMMA, i)

        def getRuleIndex(self):
            return PytoJavaParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = PytoJavaParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(PytoJavaParser.ID)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PytoJavaParser.COMMA:
                self.state = 38
                self.match(PytoJavaParser.COMMA)
                self.state = 39
                self.match(PytoJavaParser.ID)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PytoJavaParser.StatementContext)
            else:
                return self.getTypedRuleContext(PytoJavaParser.StatementContext,i)


        def getRuleIndex(self):
            return PytoJavaParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = PytoJavaParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self.statement()
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PytoJavaParser.RETURN) | (1 << PytoJavaParser.PRINT) | (1 << PytoJavaParser.LPAREN) | (1 << PytoJavaParser.ID) | (1 << PytoJavaParser.NUMBER))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnStmt(self):
            return self.getTypedRuleContext(PytoJavaParser.ReturnStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(PytoJavaParser.PrintStmtContext,0)


        def exprStmt(self):
            return self.getTypedRuleContext(PytoJavaParser.ExprStmtContext,0)


        def getRuleIndex(self):
            return PytoJavaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PytoJavaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PytoJavaParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.returnStmt()
                pass
            elif token in [PytoJavaParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.printStmt()
                pass
            elif token in [PytoJavaParser.LPAREN, PytoJavaParser.ID, PytoJavaParser.NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.exprStmt()
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

    class ReturnStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(PytoJavaParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(PytoJavaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PytoJavaParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)




    def returnStmt(self):

        localctx = PytoJavaParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(PytoJavaParser.RETURN)
            self.state = 56
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrintStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(PytoJavaParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(PytoJavaParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(PytoJavaParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(PytoJavaParser.RPAREN, 0)

        def getRuleIndex(self):
            return PytoJavaParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)




    def printStmt(self):

        localctx = PytoJavaParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(PytoJavaParser.PRINT)
            self.state = 59
            self.match(PytoJavaParser.LPAREN)
            self.state = 60
            self.expression()
            self.state = 61
            self.match(PytoJavaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PytoJavaParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(PytoJavaParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(PytoJavaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PytoJavaParser.RULE_exprStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)




    def exprStmt(self):

        localctx = PytoJavaParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exprStmt)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(PytoJavaParser.ID)
                self.state = 64
                self.match(PytoJavaParser.ASSIGN)
                self.state = 65
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PytoJavaParser.MulExprContext)
            else:
                return self.getTypedRuleContext(PytoJavaParser.MulExprContext,i)


        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(PytoJavaParser.SUB)
            else:
                return self.getToken(PytoJavaParser.SUB, i)

        def getRuleIndex(self):
            return PytoJavaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = PytoJavaParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.mulExpr()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PytoJavaParser.SUB:
                self.state = 70
                self.match(PytoJavaParser.SUB)
                self.state = 71
                self.mulExpr()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MulExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PytoJavaParser.AtomContext)
            else:
                return self.getTypedRuleContext(PytoJavaParser.AtomContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(PytoJavaParser.MUL)
            else:
                return self.getToken(PytoJavaParser.MUL, i)

        def getRuleIndex(self):
            return PytoJavaParser.RULE_mulExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)




    def mulExpr(self):

        localctx = PytoJavaParser.MulExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_mulExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.atom()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PytoJavaParser.MUL:
                self.state = 78
                self.match(PytoJavaParser.MUL)
                self.state = 79
                self.atom()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(PytoJavaParser.NUMBER, 0)

        def ID(self):
            return self.getToken(PytoJavaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(PytoJavaParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(PytoJavaParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(PytoJavaParser.RPAREN, 0)

        def getRuleIndex(self):
            return PytoJavaParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = PytoJavaParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atom)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PytoJavaParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(PytoJavaParser.NUMBER)
                pass
            elif token in [PytoJavaParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(PytoJavaParser.ID)
                pass
            elif token in [PytoJavaParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.match(PytoJavaParser.LPAREN)
                self.state = 88
                self.expression()
                self.state = 89
                self.match(PytoJavaParser.RPAREN)
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





