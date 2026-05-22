grammar cantor;

prog
    : line* EOF
    ;

line
    : directive
    | function_def
    | NL
    ;

directive
    : main_directive
    | import_directive
    ;

main_directive
    : 'main' ID NL?
    ;

import_directive
    : 'import' ID NL?
    ;

function_def
    : 'define' ID NL? body_line
    ;

body_line
    : DOC? op f g NL?
    ;

op
    : 'comp'
    | 'pair'
    ;

f
    : ID
    ;

g
    : ID
    ;

DOC
    : '[' ~[\r\n]* ']'
    ;

COMMENT
    : '#' ~[\r\n]* -> skip
    ;

ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

NL
    : '\r'? '\n'
    ;

WS
    : [ \t]+ -> skip
    ;
