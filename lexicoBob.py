'''

    Analisador lexico para a linguagem Bob.

    Autores : Mateus Soares
            : Rodrigo Pacheco
    Data    : 06 de agosto de 2020

'''

import ply.lex as lex

# Dicionario de palavras reservadas

reserved = {
    'class': 'CLASS',
    'static': 'STATIC',
    'if': 'IF',
    'else': 'ELSE',
    'while': "WHILE",
    'do': 'DO',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'in': 'IN',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'new': 'NEW',
    'nil': 'NIL',
    'def': 'DEF',
    'var': 'VAR', }

# Lista com o nome de todos os tokens

tokens = [
    'IDENT',
    'INT',
    'FLOAT',
    'STRING',
    'ABRECV',
    'FECHACV',
    'DOISP',
    'PONTOV',
    'ABREPAR',
    'FECHAPAR',
    'VIRG',
    'ABRECOL',
    'FECHACOL',
    'OPESCOPO',
    'ATRIB',
    'ATRIBCOMP',
    'MENOSCOMP',
    'MULTCOMP',
    'DIVCOMP',
    'COND',
    'OULOG',
    'ELOG',
    'OU',
    'E',
    'DESLESQ',
    'DESLDIR',
    'IGUAL',
    'DIFER',
    'MAIORIGUAL',
    'MENORIGUAL',
    'MAIOR',
    'MENOR',
    'MAIS',
    'MENOS',
    'MULT',
    'DIV',
    'MOD',
    'DECREM',
    'INCREMEN',
    'NAO',
    'COMPLEM',
    'PONTEIRO',
    'ERRO', ] + list(reserved.values())


# Expressoes regulares para capturar tokens
def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENT') # Procura por palavras reservadas
    return t


def t_Float(t):
    r'\d+([.]\d*)?'
    indice = lexer.lexpos
    car = lexer.lexdata[indice]
    tam = 0
    while car.isalpha():
        t.value += car
        tam += 1
        car = lexer.lexdata[indice+tam]
    if tam > 0:
            t.type = 'ERRO'
            t.lexer.skip(tam)
    else:
        try:
            t.value = int(t.value)
            t.type = 'INT'
            return t
        except ValueError:
            pass
        try:
            t.value = float(t.value)
            t.type = 'FLOAT'
            return t
        except ValueError:
            pass
    return t

'''
def t_NUMBER(t):
    r'[+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*)(?:[eE][+-]?\d+)?'
    t.value = eval(t.value)
    return t
'''

def t_STRING(t):
    r'\"(.*)\"|\'(.*)\''
    t.value = t.value[1:-1]
    return t

# Definicao dos tokens

t_ABRECV = r'\{'
t_FECHACV = r'\}'
t_DOISP = r':'
t_PONTOV = r';'
t_ABREPAR = r'\('
t_FECHAPAR = r'\)'
t_VIRG = r','
t_ABRECOL = r'\['
t_FECHACOL = r'\]'
t_OPESCOPO = r'::'
t_ATRIB = r'='
t_ATRIBCOMP = r'\+='
t_MENOSCOMP = r'\-='
t_MULTCOMP = r'\*='
t_DIVCOMP = r'/='
t_COND = r'\?'
t_OULOG = r'\|\|'
t_ELOG = r'&&'
t_OU = r'\|'
t_E = r'&'
t_DESLESQ = r'<<'
t_DESLDIR = r'>>'
t_IGUAL = r'=='
t_DIFER = r'\!='
t_MAIORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_MAIOR = r'>'
t_MENOR = r'<'
t_MAIS = r'\+'
t_MENOS = r'\-'
t_MULT = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_DECREM = r'\-\-'
t_INCREMEN = r'\+\+'
t_NAO = r'\!'
t_COMPLEM = r'~'
t_PONTEIRO = r'\->'


# Expressao regular para tratar numero de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Descartar parte da entrada
t_ignore_SPACES = r'[ \t]+'  # espacos em branco
t_ignore_COMMENT = r'\#.*'   # comentarios


# Tratamento de erros
def t_error(t):
    t.type = 'ERRO'
    t.value = t.value[0]
    t.lexer.skip(1)
    return t


# Final do arquivo
def t_eof(t):
    return None


lexer = lex.lex()

if __name__ == '__main__':

    nomeArquivo = 'test_lex.txt'
    arquivo = open(nomeArquivo, 'r')
    text = arquivo.read()


    lexer.input(text)

    while True:
        tok = lexer.token()
        if tok is None:
            break
        print(tok)
