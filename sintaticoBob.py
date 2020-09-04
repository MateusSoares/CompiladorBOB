'''

    Analisador sintático para a linguagem Bob.

    Autores : Mateus Soares
            : Rodrigo Pacheco
    Data    : 06 de agosto de 2020

'''

import ply.yacc as yacc
from lexicoBob import tokens, lexer
from enum import Enum


class AST(Enum):
    LISTA_DEFINICAO = 1
    CLASSE_DEF = 3
    MEMBRO_VAR = 4
    MEMBRO_FUNC = 5
    FUNCAO_DEF = 7
    COMANDO = 8
    EXPRESSAO = 9
    SEQ_COM = 10
    NUMBER = 11
    STRING = 12
    IDENT = 13



class NodeAST:

    def __init__(self, tipo, filhos=None):
        if not isinstance(tipo, AST):
            raise ValueError('Tipo nao definido para NodeAST')
        else:
            self.tipo = tipo

        # caso LISTA_DEFINICAO : Definicao de classes e funcoes
        # caso CLASSE : definicao de uma classe
        # caso CLASSE_MEMBRO : membros da classe
        # caso MEMBRO_VAR : variaveis membros da classe
        # caso MEMBRO_FUNC : funcoes membros da classe
        # caso FUNCAO : definicao de uma funcao
        # caso BLOCO_FUNC: cada filho denota um COMANDO
        # caso COMANDO: primeiro filho define qual comando (str)
        # caso EXPRESSAO: primeiro filho define qual operador (str)
        # caso SEQ_COM: cada filho denota um comando
        # caso NUMBER: um filho que traz o valor
        # caso STRING: um filho que traz o valor
        # caso IDENT: um filho que traz o valor

        if filhos:
            self.filhos = filhos
        else:
            self.filhos = list()


        def __str__(self):
            return f'Tipo: {self.tipo} Filhos: {self.filhos}'

precedence = (
    ('right', 'ATRIB', 'MENOSCOMP', 'ATRIBCOMP', 'DIVCOMP', 'MULTCOMP'),
    ('right', 'COND', 'DOISP'),
    ('left', 'OULOG'),
    ('left', 'ELOG'),
    ('left', 'OU'),
    ('left', 'E'),
    ('nonassoc', 'IGUAL', 'DIFER'),
    ('nonassoc', 'MENOR', 'MENORIGUAL', 'MAIORIGUAL', 'MAIOR'),
    ('left', 'DESLESQ', 'DESLDIR'),
    ('left', 'MAIS', 'MENOS'),
    ('left', 'MULT', 'DIV', 'MOD'),
    ('right', 'UMENOS', 'UMAIS'),
    ('right', 'INCREMEN', 'DECREM', 'NAO', 'COMPLEM'),
    ('left',  'PONTEIRO'),
    )


def p_Programa(p):
    'Programa : ListaDefinicoes'
    p[0] = p[1]


def p_ListaDefinicoes(p):
    '''ListaDefinicoes : ListaDefinicoes Definicao
                       | empty '''
    if len(p) == 3:
        filhos = p[1].filhos + [p[2]]
    else:
        filhos = list()
    p[0] = NodeAST(AST.LISTA_DEFINICAO, filhos)



def p_Definicao(p):
    ''' Definicao : DefinicaoClasse
                  | DefinicaoFuncao '''
    p[0] = p[1]



def p_DefinicaoClasse(p):
    ''' DefinicaoClasse : CLASS IDENT DOISP IDENT ABRECV ListaMembros FECHACV
                        | CLASS IDENT ABRECV ListaMembros FECHACV '''
    if len(p) == 8:
        ident = NodeAST(AST.IDENT, [p[2]])
        filhos = ['CLASSE', ident, p[6]]
    else:
        ident = NodeAST(AST.IDENT, [p[2]])
        filhos = ['CLASSE', ident, p[4]]
    p[0] = NodeAST(AST.CLASSE_DEF, filhos)



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
                | IDENT ABRECOL INT FECHACOL '''
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
    '''DefinicaoFuncao : DEF IDENT OPESCOPO IDENT ABREPAR ListaParametrosOpcionais FECHAPAR Bloco
                       | DEF IDENT ABREPAR ListaParametrosOpcionais FECHAPAR Bloco'''
    if len(p) == 9:
        ident1 = NodeAST(AST.IDENT, [p[2]])
        ident2 = NodeAST(AST.IDENT, [p[4]])
        filhos = ['CLASSE', ident1, 'FUNCAO', ident2, p[6], p[8]]
    else:
        ident = NodeAST(AST.IDENT, [p[2]])
        filhos = ['FUNCAO', ident, p[4], p[6]]

    p[0] = NodeAST(AST.FUNCAO_DEF, filhos)


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
    '''Exp : EsqVal ATRIB Exp
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
           | ABREPAR Exp FECHAPAR
           | DECREM EsqVal
           | INCREMEN EsqVal
           | EsqVal DECREM
           | EsqVal INCREMEN
           | NAO Exp
           | COMPLEM Exp
           | MENOS Exp %prec UMENOS
           | MAIS Exp %prec UMAIS
           | NEW IDENT ABREPAR ArgumentosOpcionais FECHAPAR
           | IDENT ABREPAR ArgumentosOpcionais FECHAPAR
           | Exp PONTEIRO IDENT ABREPAR ArgumentosOpcionais FECHAPAR
           | IDENT
           | IDENT ABRECOL Exp FECHACOL
           | FLOAT
           | INT
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
    nomeArquivo = 'test_bob.txt'
    arquivo = open(nomeArquivo, 'r')
    text = arquivo.read()

    result = parser.parse(text, lexer=lexer)
    print(result)