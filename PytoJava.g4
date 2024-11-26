grammar PytoJava;

// Lexer Rules 
DEF         : 'def';
RETURN      : 'return';
PRINT       : 'print';
COMMA       : ',';
LPAREN      : '(';
RPAREN      : ')';
COLON       : ':';
ASSIGN      : '=';
MUL         : '*';
SUB         : '-';
ID          : [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER      : [0-9]+;
NEWLINE     : '\r'? '\n' -> skip;
WS          : [ \t]+ -> skip;


// Parser Rules
program     : functionDef+;

functionDef : DEF ID LPAREN parameters? RPAREN COLON statements;

parameters  : ID (COMMA ID)*;

statements  : statement+;

statement   : returnStmt | printStmt | exprStmt;

returnStmt  : RETURN expression;

printStmt   : PRINT LPAREN expression RPAREN;

exprStmt    : ID ASSIGN expression | expression;

expression  : mulExpr ((SUB) mulExpr)*;

mulExpr     : atom (MUL atom)*;

atom        : NUMBER | ID | LPAREN expression RPAREN;
