'''

    Analisador lexico para a linguagem Bob.

    Autor : Mateus Soares
    Data  : 06 de agosto de 2020

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
    'nil': 'NIL', }

# Lista com o nome de todos os tokens

tokens = [
    'IDENT',
    'NUMERO',
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
    'MENOS,'
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
    pass

def t_NUMBER(t):
    r'\d+'
    pass

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
t_COND = r'?'
t_OULOG = r'||'
t_ELOG = r'&&'
t_OU = r'|'
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
