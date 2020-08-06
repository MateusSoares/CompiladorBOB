'''

    Analisador sintático para a linguagem Bob.

    Autor : Mateus Soares
    Data  : 06 de agosto de 2020

'''

import ply.yacc as yacc
from lexicoBob import tokens, lexer

precedence = (
    ('right', 'NAO'),
    ('left', 'E', 'OU'),
    ('nonassoc', 'IGUAL', 'DIFER', 'MAIOR', 'MENOR', 'MAIORIGUAL', 'MENORIGUAL'),
    ('left', 'MAIS', 'MENOS'),
    ('left', 'MULT', 'DIV', 'MOD'),
    )


def p_Programa(p):
    'Programa : ListaDefinicoes'
    pass


def p_ListaDefinicoes(p):
    '''ListaDefinicoes : ListaDefinicoes
        | empty '''
    pass


def p_Definicao(p):
    ''' Definicao : DefinicaoClasse
        | DefinicaoFuncao '''
    pass


def p_DefinicaoClasse(p):
    'DefinicaoClasse : CLASS IDENT ClasseBaseOpcional ABRECV ListaMembros FECHACV'
    pass


def p_ClasseBaseOpcional(p):
    ''' ClasseBaseOpcional : DOISP IDENT
        | empty '''
    pass


def p_ListaMembros(p):
    '''ListaMembros : ListaMembros DefinicaoMembro
        | empty '''
    pass


def p_DefinicaoMembro(p):
    '''DefinicaoMembro : ModificadorOpcional ListaVariaveis PONTOV
        | ModificadorOpcional IDENT ABREPAR ListaArgsFormaisOpcional FECHAPAR PONTOV '''
    pass


def p_ModificadorOpcional(p):
    '''ModificadorOpcional : STATIC
        | empty '''
    pass


def p_ListaVariaveis(p):
    '''ListaVariaveis : ListaVariaveis VIRG Variavel
        | Variavel '''
    pass

def p_Variavel(p):
    '''Variavel : IDENT
        | IDENT ABRECOL NUMBER FECHACOL '''
    pass

def p_ListaArgsFormaisOpcional(p):
    '''ListaArgsFormaisOpcional : ListaArgsFormais
        | empty '''
    pass


def p_ListaArgsFormais(p):
    '''ListaArgsFormais : ListaArgsFormais VIRG IDENT
        | IDENT '''
    pass


def p_DefinicaoFuncao(p):
    'DefinicaoFuncao : ClasseEnvolucroOpcional IDENT ABREPAR ListaParametroOpcionais FECHAPAR Bloco'
    pass


def p_ClasseEnvolucroOpcional(p):
    '''ClasseEnvolucroOpcional : IDENT OPESCOPO
        | empty '''
    pass


def p_ListaParametrosOpcionais(p):
    'ListaParametrosOpcionais : ListaArgsFormaisOpcional ListaTemporariosOpcionais'
    pass


def p_ListaTemporariosOpcionais(p):
    '''ListaTemporariosOpcionais : PONTOV ListaArgsFormais
        | empty '''
    pass
