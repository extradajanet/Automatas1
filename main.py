from antlr4 import *
from PytoJavaLexer import PytoJavaLexer
from PytoJavaParser import PytoJavaParser
from TranslatePytoJava import TranslatePytoJava
def main():
    in_code = input('File Name> ')
    
    fileopen= open(in_code)
    lexer = PytoJavaLexer(InputStream(fileopen.read()))
    stream = CommonTokenStream(lexer)
    parser = PytoJavaParser(stream)
    tree = parser.program()
        #print(tree.toStringTree(recog=parser))
    walker =ParseTreeWalker()
    walker.walk(TranslatePytoJava(),tree)
'.... . .-.. .-.. ---'  
if __name__=='__main__':
    main()