grammar cantor;

prog: NL* main_directive NL* extended_directive? import_directive* line* EOF;

line
    : function_def
    | NL
    ;

main_directive: 'main' ID NL?;
import_directive: 'import' ID NL?;
extended_directive: 'extended' NL?;

function_def: 'define' ID NL? DOC? NL* operation NL?;

operation
    : 'comp' ID ID        # Comp
    | 'pair' ID ID        # Pair
    | 'compair' ID ID ID  # Compair
    | 'mu' ID             # Mu
    | 'primrec' ID ID ID  # Primrec
    | ID                  # Alias
    ;

DOC: '[' ~[\r\n\]]* ']';
COMMENT: '#' ~[\r\n]* -> skip;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NL: '\r'? '\n';
WS: [ \t]+ -> skip;
LEXICAL_ERROR : . ;