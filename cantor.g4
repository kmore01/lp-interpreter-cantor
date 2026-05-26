grammar cantor;

prog: line* EOF;

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

main_directive: 'main' ID NL?;
import_directive: 'import' ID NL?;
extended_directive: 'extended' NL?;

function_def: 'define' ID NL? DOC? NL* operation NL?;

operation
    : 'comp' ID ID        # CompOp
    | 'pair' ID ID        # PairOp
    | 'compair' ID ID ID  # CompairOp
    | 'mu' ID             # MuOp
    | 'primrec' ID ID ID  # PrimrecOp
    | ID                  # AliasOp
    ;

DOC: '[' ~[\r\n]* ']';
COMMENT: '#' ~[\r\n]* -> skip;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NL: '\r'? '\n';
WS: [ \t]+ -> skip;