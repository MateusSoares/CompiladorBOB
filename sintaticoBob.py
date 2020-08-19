'''

    Analisador sintático para a linguagem Bob.

    Autor : Mateus Soares
    Data  : 06 de agosto de 2020

'''

import ply.yacc as yacc
from lexicoBob import tokens, lexer

precedence = (
    ('left', 'ABREPAR', 'FECHAPAR', 'ABRECOL', 'FECHACOL', 'PONTEIRO'),
    ('right', 'INCREMEN', 'DECREM', 'NAO', 'COMPLEM'),
    ('left', 'MULT', 'DIV', 'MOD'),
    ('left', 'MAIS', 'MENOS'),
    ('left', 'DESLESQ', 'DESLDIR'),
    ('left', 'MENOR', 'MENORIGUAL', 'MAIORIGUAL', 'MAIOR'),
    ('left', 'IGUAL', 'DIFER'),
    ('left', 'E'),
    ('left', 'OU'),
    ('left', 'ELOG'),
    ('left', 'OULOG'),
    ('right', 'COND', 'DOISP'),
    ('right', 'ATRIB', 'MENOSCOMP', 'ATRIBCOMP', 'DIVCOMP', 'MULTCOMP'),
    ('left', 'VIRG'),
    )


def p_Programa(p):
    'Programa : ListaDefinicoes'
    pass


def p_ListaDefinicoes(p):
    '''ListaDefinicoes : ListaDefinicoes Definicao
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
    '''DefinicaoMembro : ModificadorOpcional VAR ListaVariaveis PONTOV
                       | ModificadorOpcional DEF IDENT ABREPAR ListaArgsFormaisOpcional FECHAPAR PONTOV '''
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
    'DefinicaoFuncao : DEF ClasseEnvolucroOpcional IDENT ABREPAR ListaParametrosOpcionais FECHAPAR Bloco'
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


def p_Bloco(p):
    'Bloco : ABRECV ListaComandos FECHACV'
    pass


def p_ListaComandos(p):
    '''ListaComandos : ListaComandos Comando
                     | empty '''
    pass


def p_Comando(p):
    '''Comando : IF ABREPAR ExpOpc FECHAPAR Comando ELSE Comando
               | IF ABREPAR ExpOpc FECHAPAR Comando
               | WHILE ABREPAR ExpOpc FECHAPAR Comando
               | DO Comando WHILE ABREPAR ExpOpc FECHAPAR PONTOV
               | FOR ABREPAR ExpOpc PONTOV ExpOpc PONTOV ExpOpc FECHAPAR Comando
               | FOREACH IDENT IN IDENT Comando
               | BREAK PONTOV
               | CONTINUE PONTOV
               | RETURN ExpOpc PONTOV
               | ExpOpc PONTOV
               | Bloco '''
    pass


def p_ExpOpc(p):
    '''ExpOpc : Exp
              | empty '''
    pass


def p_Exp(p):
    '''Exp : Exp VIRG Exp
           | EsqVal ATRIB Exp
           | EsqVal ATRIBCOMP Exp
           | EsqVal MENOSCOMP Exp
           | EsqVal MULTCOMP Exp
           | EsqVal DIVCOMP Exp
           | Exp COND Exp DOISP Exp
           | Exp OULOG Exp
           | Exp ELOG Exp
           | Exp OU Exp
           | Exp E Exp
           | Exp DESLESQ Exp
           | Exp DESLDIR Exp
           | Exp IGUAL Exp
           | Exp DIFER Exp
           | Exp MAIORIGUAL Exp
           | Exp MENORIGUAL Exp
           | Exp MAIOR Exp
           | Exp MENOR Exp
           | Exp MAIS Exp
           | Exp MENOS Exp
           | Exp MULT Exp
           | Exp DIV Exp
           | Exp MOD Exp
           | DECREM EsqVal
           | INCREMEN EsqVal
           | EsqVal DECREM
           | EsqVal INCREMEN
           | NAO Exp
           | COMPLEM Exp
           | NEW IDENT ABREPAR ArgumentosOpcionais FECHAPAR
           | IDENT ABREPAR ArgumentosOpcionais FECHAPAR
           | Exp PONTEIRO IDENT ABREPAR ArgumentosOpcionais FECHAPAR
           | IDENT
           | IDENT ABRECOL Exp FECHACOL
           | NUMBER
           | STRING
           | NIL '''
    pass


def p_ArgumentosOpcionais(p):
    '''ArgumentosOpcionais : Argumentos
                           | empty '''
    pass


def p_Argumentos(p):
    '''Argumentos : Argumentos VIRG Exp
                  | Exp '''
    pass


def p_EsqVal(p):
    '''EsqVal : IDENT
              | IDENT ABRECOL Exp FECHACOL '''
    pass


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if p is None:
        print("Sintax error at EOF")
    else:
        print("Sintax error at token", p.type, "line=", p.lineno)


parser = yacc.yacc()

if __name__ == '__main__':
    nomeArquivo = 'testeBob.bob'
    arquivo = open(nomeArquivo, 'r')
    text = arquivo.read()

    result = parser.parse(text, lexer=lexer)
    print(result)