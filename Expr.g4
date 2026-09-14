grammar Expr;

root: expr EOF;

expr: '(' expr ')' # Parent

    | expr '^' expr # Pot

    | expr ('*'|'/') expr # MultDiv

    | expr ('+'|'-') expr # SomaSub

    | (abs_ | fact) # Func

    | ('-')? NUM # Number

    ;

abs_ : 'abs' '(' expr ')';

fact : 'fat' '(' expr ')';

NUM : [0-9]+('.'[0-9]+)?;

WS : [ \n\r\t]+ -> skip;