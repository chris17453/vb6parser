grammar VB6;

// Define rules to capture class, function, and variable declarations
classDeclaration: 'Class' className=IDENTIFIER
                   (functionDeclaration | variableDeclaration)*
                 'End Class';

functionDeclaration: 'Function' functionName=IDENTIFIER
                     (parameterDeclaration)*
                     'As' returnType=IDENTIFIER
                     (statement)*
                   'End Function';

variableDeclaration: 'Dim' variableName=IDENTIFIER
                     'As' variableType=IDENTIFIER
                     (',' variableName=IDENTIFIER 'As' variableType=IDENTIFIER)*
                     ';';

// Other rules for statements and expressions go here

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;