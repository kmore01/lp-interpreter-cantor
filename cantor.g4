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
    | extended_directive
    ;

main_directive
    : 'main' ID NL?
    ;

import_directive
    : 'import' ID NL?
    ;

extended_directive
    : 'extended' NL?
    ;

function_def
    : 'define' ID NL? body_line
    ;

body_line
    : DOC? (comp_op | pair_op | compair_op | mu_op | primrec_op) NL?
    ;

comp_op
    : 'comp' f g
    ;

pair_op
    : 'pair' f g
    ;

compair_op
    : 'compair' f g h
    ;

mu_op
    : 'mu' f
    ;

primrec_op
    : 'primrec' f g h
    ;

f : ID;
g : ID;
h : ID;

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
