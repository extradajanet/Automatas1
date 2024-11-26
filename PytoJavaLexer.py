# Generated from PytoJava.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("X\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\7\fA\n\f\f")
        buf.write("\f\16\fD\13\f\3\r\6\rG\n\r\r\r\16\rH\3\16\5\16L\n\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\6\17S\n\17\r\17\16\17T\3\17\3")
        buf.write("\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\3\2\6\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\3\2\62;\4\2\13\13\"\"\2[\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2")
        buf.write("\2\2\5#\3\2\2\2\7*\3\2\2\2\t\60\3\2\2\2\13\62\3\2\2\2")
        buf.write("\r\64\3\2\2\2\17\66\3\2\2\2\218\3\2\2\2\23:\3\2\2\2\25")
        buf.write("<\3\2\2\2\27>\3\2\2\2\31F\3\2\2\2\33K\3\2\2\2\35R\3\2")
        buf.write("\2\2\37 \7f\2\2 !\7g\2\2!\"\7h\2\2\"\4\3\2\2\2#$\7t\2")
        buf.write("\2$%\7g\2\2%&\7v\2\2&\'\7w\2\2\'(\7t\2\2()\7p\2\2)\6\3")
        buf.write("\2\2\2*+\7r\2\2+,\7t\2\2,-\7k\2\2-.\7p\2\2./\7v\2\2/\b")
        buf.write("\3\2\2\2\60\61\7.\2\2\61\n\3\2\2\2\62\63\7*\2\2\63\f\3")
        buf.write("\2\2\2\64\65\7+\2\2\65\16\3\2\2\2\66\67\7<\2\2\67\20\3")
        buf.write("\2\2\289\7?\2\29\22\3\2\2\2:;\7,\2\2;\24\3\2\2\2<=\7/")
        buf.write("\2\2=\26\3\2\2\2>B\t\2\2\2?A\t\3\2\2@?\3\2\2\2AD\3\2\2")
        buf.write("\2B@\3\2\2\2BC\3\2\2\2C\30\3\2\2\2DB\3\2\2\2EG\t\4\2\2")
        buf.write("FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\32\3\2\2\2J")
        buf.write("L\7\17\2\2KJ\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\7\f\2\2NO\3")
        buf.write("\2\2\2OP\b\16\2\2P\34\3\2\2\2QS\t\5\2\2RQ\3\2\2\2ST\3")
        buf.write("\2\2\2TR\3\2\2\2TU\3\2\2\2UV\3\2\2\2VW\b\17\2\2W\36\3")
        buf.write("\2\2\2\7\2BHKT\3\b\2\2")
        return buf.getvalue()


class PytoJavaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DEF = 1
    RETURN = 2
    PRINT = 3
    COMMA = 4
    LPAREN = 5
    RPAREN = 6
    COLON = 7
    ASSIGN = 8
    MUL = 9
    SUB = 10
    ID = 11
    NUMBER = 12
    NEWLINE = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'return'", "'print'", "','", "'('", "')'", "':'", 
            "'='", "'*'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "RETURN", "PRINT", "COMMA", "LPAREN", "RPAREN", "COLON", 
            "ASSIGN", "MUL", "SUB", "ID", "NUMBER", "NEWLINE", "WS" ]

    ruleNames = [ "DEF", "RETURN", "PRINT", "COMMA", "LPAREN", "RPAREN", 
                  "COLON", "ASSIGN", "MUL", "SUB", "ID", "NUMBER", "NEWLINE", 
                  "WS" ]

    grammarFileName = "PytoJava.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


