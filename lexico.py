# ------------------------------------------------------------
# lexico.py
#
# Analisador lexico para a linguagem Toy
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
             WHILE BREAK IF EQUAL DIF GT LT GTE LTE NOT AND OR
             OPENBLK CLOSEBLK OPENPAR CLOSEPAR ERROR MAIN

    Comentarios::  iniciam com # ate o fim da linha
"""

import ply.lex as lex

# Dicionario de palavras reservadas
reserved = {
    'read': 'READ',
    'print': 'PRINT',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'if': 'IF',
    'else': 'ELSE',
    'and': 'AND',
    'or': 'OR',
    'main': 'MAIN', }

# Lista com o nome de todos os tokens (sempre necessario)
tokens = [
    'IDENT',
    'NUMBER',
    'ATRIB',
    'PTOVIR',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'MOD',
    'EQUAL',
    'DIF',
    'GT',
    'LT',
    'GTE',
    'LTE',
    'NOT',
    'OPENBLK',
    'CLOSEBLK',
    'OPENPAR',
    'CLOSEPAR',
    'ERROR', ] + list(reserved.values())
     # EOF retorna token None

# Daqui seguem as expressoes regulares para capturar todos os tokens

def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENT')  # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ATRIB = r'='
t_PTOVIR = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_EQUAL = r'=='
t_DIF = r'\!='
t_GT = r'>'
t_LT = r'<'
t_GTE = r'>='
t_LTE = r'<='
t_NOT = r'\!'
t_OPENBLK = r'\{'
t_CLOSEBLK = r'\}'
t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'

# Define uma ExpReg para tratar line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define ExpRegs para descartar partes da entrada
t_ignore_SPACES = r'[ \t]+'     # espacos brancos
t_ignore_COMMENT = r'\#.*'  # comentarios

# Error handling rule
def t_error(t):
    t.type = 'ERROR'
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

# EOF handling rule
def t_eof(t):
    return None

# Build the lexer
lexer = lex.lex()

# ====================================================================

if __name__ == '__main__':

    data = '''
        3 + 4 * 10. # comentario 45 45
        + -20 *2 / / 77
        teste if reader read
        while ; ==>
        '''
    lexer.input(data)

    while True:
        tok = lexer.token()
        if tok is None:
            break  # No more input
        print(tok)
