# ------------------------------------------------------------
# sintatico.py
#
# Analisador sintatico para a linguagem Toy
# ------------------------------------------------------------

"""
 Linguagem Toy

    Gramatica::

    Prog* --> MAIN ( ) Block
    Block -->  { SeqCom }
    SeqCom --> SeqCom Com
        | Com
    Com --> Simple
        | Block
    Simple --> Atrib
        | Decision
        | Loop
        | Input
        | Output
        | Specials

    Atrib --> ident = Exp ;
    Decision --> if ( Test ) Com
        | if ( Test ) Com else Com
    Loop --> while ( Test ) Com
    Output --> print ( ident ) ;
    Input --> read ( ident ) ;
    Specials --> break ;
        | continue ;
    Test --> Exp

    Exp --> Exp and Exp
        | Exp or Exp
        | not Exp
        | Exp == Exp
        | Exp != Exp
        | Exp > Exp
        | Exp >= Exp
        | Exp < Exp
        | Exp <= Exp
        | Exp / Exp
        | Exp % Exp
        | Exp * Exp
        | Exp + Exp
        | Exp - Exp
        | - Exp
        | + Exp
        | ( Exp )
        | ident
        | num

    Tokens:: IDENT NUMBER ATRIB PTOVIR READ PRINT PLUS MINUS TIMES DIV MOD
             WHILE BREAK CONTINUE IF EQUAL DIF GT LT GTE LTE NOT AND OR
             OPENBLK CLOSEBLK OPENPAR CLOSEPAR ERROR MAIN

    Comentarios::  iniciam com # ate o fim da linha
"""

import ply.yacc as yacc
from lexico import tokens, lexer
from enum import Enum

class AST(Enum):
    BLOCO = 1
    COMANDO = 2
    EXPRESSAO = 3
    SEQ_COM = 4
    NUMBER = 5
    IDENT = 6

class NodeAST:
    def __init__(self, tipo, filhos=None):
        if not isinstance(tipo, AST):
            raise ValueError('Tipo nao definido para NodeAST')
        else:
            self.tipo = tipo

        # caso BLOCO: cada filho denota um COMANDO
        # caso COMANDO: primeiro filho define qual comando (str)
        # caso EXPRESSAO: primeiro filho define qual operador (str)
        # caso SEQ_COM: cada filho denota um comando
        # caso NUMBER: um filho que traz o valor
        # caso IDENT: um filho que traz o valor
        if filhos:
            self.filhos = filhos
        else:
            self.filhos = list()

precedence = (
     ('right', 'NOT'),
     ('left', 'AND', 'OR'),
     ('nonassoc', 'EQUAL', 'DIF', 'GT', 'LT', 'GTE', 'LTE'),  # Nonassociative operators
     ('left', 'PLUS', 'MINUS'),
     ('left', 'TIMES', 'DIV', 'MOD'),
     ('right', 'UMINUS', 'UPLUS'),   # Unary operators (sinalizados com %prec nas regras)
     )

def p_Prog(p):
    'Prog : MAIN OPENPAR CLOSEPAR Block'
    p[0] = p[4]

def p_Block(p):
    'Block : OPENBLK SeqCom CLOSEBLK'
    p[0] = NodeAST(AST.BLOCO, p[2].filhos)

def p_SeqCom(p):
    '''SeqCom : SeqCom Com
              | Com'''
    if len(p) == 3:
        filhos = p[1].filhos + [p[2]]
    else:
        filhos = [p[1]]
    p[0] = NodeAST(AST.SEQ_COM, filhos)

def p_Com(p):
    '''Com : Simple
           | Block'''
    p[0] = p[1]

def p_Simple(p):
    '''Simple : Atrib
              | Decision
              | Loop
              | Input
              | Output
              | Specials'''
    p[0] = p[1]

def p_Atrib(p):
    'Atrib : IDENT ATRIB Exp PTOVIR'
    ident = NodeAST(AST.IDENT, p[1])
    filhos = ['ATRIB', ident, p[3]]
    p[0] = NodeAST(AST.COMANDO, filhos)

def p_Decision(p):
    '''Decision : IF OPENPAR Test CLOSEPAR Com ELSE Com
                | IF OPENPAR Test CLOSEPAR Com'''
    if len(p) == 7:
        filhos = ['IF', p[3], p[5], p[7]]
    else:
        filhos = ['IF', p[3], p[5]]
    p[0] = NodeAST(AST.COMANDO, filhos)

def p_Loop(p):
    'Loop : WHILE OPENPAR Test CLOSEPAR Com'
    filhos = ['WHILE', p[3], p[5]]
    p[0] = NodeAST(AST.COMANDO, filhos)

def p_Output(p):
    'Output : PRINT OPENPAR IDENT CLOSEPAR PTOVIR'
    ident = NodeAST(AST.IDENT, [p[3]])
    filhos = ['PRINT', ident]
    p[0] = NodeAST(AST.COMANDO, filhos)

def p_Input(p):
    'Input : READ OPENPAR IDENT CLOSEPAR PTOVIR'
    ident = NodeAST(AST.IDENT, [p[3]])
    filhos = ['READ', ident]
    p[0] = NodeAST(AST.COMANDO, filhos)

def p_Specials(p):
    '''Specials : BREAK PTOVIR
                | CONTINUE PTOVIR'''
    if p[1] == 'break':
        p[0] = NodeAST(AST.COMANDO, ['BREAK'])
    else:
        p[0] = NodeAST(AST.COMANDO, ['CONTINUE'])

def p_Test(p):
    'Test : Exp'
    p[0] = p[1]

def p_Exp(p):
    '''Exp : Exp AND Exp
           | Exp OR Exp
           | NOT Exp
           | Exp EQUAL Exp
           | Exp DIF Exp
           | Exp GT Exp
           | Exp GTE Exp
           | Exp LT Exp
           | Exp LTE Exp
           | Exp DIV Exp
           | Exp MOD Exp
           | Exp TIMES Exp
           | Exp PLUS Exp
           | Exp MINUS Exp
           | MINUS Exp %prec UMINUS
           | PLUS Exp %prec UPLUS
           | OPENPAR Exp CLOSEPAR
           | IDENT
           | NUMBER'''
    if len(p) == 2:
        # IDENT e NUMBER
        if isinstance(p[1], int):
            filhos = ['NUMBER', str(p[1])]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        else:
            filhos = ['IDENT', p[1]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
    elif len(p) == 3:
        # operadores unarios MINUS, PLUS e NOT
        filhos = [p[1], p[2]]
        p[0] = NodeAST(AST.EXPRESSAO, filhos)
    elif not isinstance(p[1], NodeAST):
        # ( Exp )
        p[0] = p[2]
    else:
        p[0] = NodeAST(AST.EXPRESSAO, [p[2], p[1], p[3]])

# Error rule for syntax errors
def p_error(p):
    if p is None:
        print("Syntax error at EOF")
    else:
        print("Syntax error at token", p.type, "line=", p.lineno)

# Build the parser
parser = yacc.yacc()

# ====================================================================

if __name__ == '__main__':
    nomeArquivo = 'teste.txt'
    arquivo = open(nomeArquivo, 'r')
    text = arquivo.read()

    result = parser.parse(text, lexer=lexer)
    print(result)
