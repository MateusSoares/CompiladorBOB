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
    CLASSE_DEF = 2
    MEMBRO_VAR = 3
    MEMBRO_FUNC = 4
    FUNCAO_DEF = 5
    COMANDO = 6
    EXPRESSAO = 7
    SEQ_COM = 8
    NUMBER = 9
    STRING = 10
    IDENT = 11



class NodeAST:

    def __init__(self, tipo, filhos=None):
        if not isinstance(tipo, AST):
            raise ValueError('Tipo nao definido para NodeAST')
        else:
            self.tipo = tipo

        # caso LISTA_DEFINICAO : Definicao de classes e funcoes
        # caso CLASSE_DEF : definicao de uma classe
        # caso MEMBRO_VAR : variaveis membros da classe
        # caso MEMBRO_FUNC : funcoes membros da classe
        # caso FUNCAO_DEF : definicao de uma funcao
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
        filhos = [ident, p[6]]
    else:
        ident = NodeAST(AST.IDENT, [p[2]])
        filhos = [ident, p[4]]
    p[0] = NodeAST(AST.CLASSE_DEF, filhos)



def p_ListaMembros(p):
    '''ListaMembros : ListaMembros DefinicaoMembro
                    | empty '''
    if len(p) == 3:
        filhos = p[1] + [p[2]]
    else:
        filhos = list()
    p[0] = filhos



def p_DefinicaoMembro(p):
    '''DefinicaoMembro : ModificadorOpcional VAR ListaVariaveis PONTOV
                       | ModificadorOpcional DEF IDENT ABREPAR ListaArgsFormaisOpcional FECHAPAR PONTOV '''
    if len(p) == 5:
        filhos = [p[1], p[3]]
        p[0] = NodeAST(AST.MEMBRO_VAR, filhos)
    else :
        ident = NodeAST(AST.IDENT, p[3])
        filhos = [p[1], ident, p[5]]
        p[0] = NodeAST(AST.MEMBRO_FUNC, filhos)


def p_ModificadorOpcional(p):
    '''ModificadorOpcional : STATIC
                           | empty '''
    p[0] = p[1]


def p_ListaVariaveis(p):
    '''ListaVariaveis : ListaVariaveis VIRG Variavel
                      | Variavel '''
    if len(p) == 4:
        filhos = p[1] + [p[3]]
    else:
        filhos = [p[1]]
    p[0] = filhos

def p_Variavel(p):
    '''Variavel : IDENT
                | IDENT ABRECOL INT FECHACOL '''
    if len(p) == 2:
        p[0] = NodeAST(AST.IDENT, p[1])
    else:
        ident = NodeAST(AST.IDENT, p[1])
        index = NodeAST(AST.NUMBER, p[3])
        p[0] = [ident, index]


def p_ListaArgsFormaisOpcional(p):
    '''ListaArgsFormaisOpcional : ListaArgsFormais
                                | empty '''
    p[0] = p[1]



def p_ListaArgsFormais(p):
    '''ListaArgsFormais : ListaArgsFormais VIRG IDENT
                        | IDENT '''
    if len(p) == 4:
        filhos = p[1] + [p[3]]
    else:
        filhos = [p[1]]
    p[0] = filhos


def p_DefinicaoFuncao(p):
    '''DefinicaoFuncao : DEF IDENT OPESCOPO IDENT ABREPAR ListaParametrosOpcionais FECHAPAR Bloco
                       | DEF IDENT ABREPAR ListaParametrosOpcionais FECHAPAR Bloco'''
    if len(p) == 9:
        ident1 = NodeAST(AST.IDENT, [p[2]])
        ident2 = NodeAST(AST.IDENT, [p[4]])
        filhos = [ident1, ident2, p[6], p[8]]
    else:
        ident = NodeAST(AST.IDENT, [p[2]])
        filhos = [ident, p[4], p[6]]

    p[0] = NodeAST(AST.FUNCAO_DEF, filhos)

    print(filhos)


def p_ListaParametrosOpcionais(p):
    'ListaParametrosOpcionais : ListaArgsFormaisOpcional ListaTemporariosOpcionais'
    p[0] = [p[1], p[2]]



def p_ListaTemporariosOpcionais(p):
    '''ListaTemporariosOpcionais : PONTOV ListaArgsFormais
                                 | empty '''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_Bloco(p):
    'Bloco : ABRECV ListaComandos FECHACV'
    p[0] = p[2]


def p_ListaComandos(p):
    '''ListaComandos : ListaComandos Comando
                     | empty '''
    if len(p) == 3:
        filhos = p[1].filhos + [p[2]]
    else:
        filhos = list()
    p[0] = NodeAST(AST.SEQ_COM, filhos)


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

    if p[1] == 'if':
        if len(p) == 6:
            filhos = ['IF', p[3], p[5]]
        else:
            filhos = ['IF', p[3], p[5], p[7]]
        p[0] = NodeAST(AST.COMANDO, filhos)
    elif p[1] == 'while':
        filhos = ['WHILE', p[3], p[5]]
        p[0] = NodeAST(AST.COMANDO, filhos)
    elif p[1] == 'do':
        filhos = ['DO', p[2], p[5]]
        p[0] = NodeAST(AST.COMANDO, filhos)
    elif p[1] == 'for':
        filhos = ['FOR', p[3], p[5], p[7], p[9]]
        p[0] = NodeAST(AST.COMANDO, filhos)
    elif p[1] == 'foreach':
        ident1 = NodeAST(AST.IDENT, p[2])
        ident2 = NodeAST(AST.IDENT, p[4])
        filhos = ['FOREACH', ident1, ident2, p[5]]
        p[0] = NodeAST(AST.COMANDO, filhos)
    elif p[1] == 'break':
        p[0] = NodeAST(AST.COMANDO, ['BREAK'])
    elif p[1] == 'continue':
        p[0] = NodeAST(AST.COMANDO, ['CONTINUE'])
    elif p[1] == 'return':
        p[0] = NodeAST(AST.COMANDO, ['RETURN', p[2]])
    elif len(p) == 3:
        p[0] = NodeAST(AST.COMANDO, [p[1]])
    else:
        p[0] = p[1]



def p_ExpOpc(p):
    '''ExpOpc : Exp
              | empty '''
    p[0] = p[1]


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
    if len(p) == 2:
        if isinstance(p[1], int):
            filhos = ['INT', str(p[1])]
            p[0] = NodeAST(AST.NUMBER, filhos)
        elif isinstance(p[1], float):
            filhos = ['FLOAT', str(p[1])]
            p[0] = NodeAST(AST.NUMBER, filhos)
        else:
            if p[1] == 'nil':
                filhos = ['NIL', p[1]]
                p[0] = NodeAST(AST.EXPRESSAO, filhos)
            elif p[1][0] == '"':
                p[0] = NodeAST(AST.STRING, p[1][1:-1])
            else:
                p[0] = NodeAST(AST.IDENT, p[1])
    elif len(p) == 3:
        if p[1] == '~':
            filhos = ['COMPLEM', p[1]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        elif p[1] == '!':
            filhos = ['NAO', p[1]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        elif p[1] == '++':
            filhos = ['INCREMEN', p[1]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        elif p[1] == '--':
            filhos = ['DECREMEN', p[1]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        elif p[2] == '++':
            filhos = ['INCREMEN', p[2]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        elif p[2] == '--':
            filhos = ['DECREMEN', p[2]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        elif p[1] == '+':
            filhos = ['MAIS', p[1]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        elif p[1] == '-':
            filhos = ['MENOS', p[1]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
    elif len(p) == 4:
        if p[1] == '(':
            filhos = ['ABREPAR', p[2]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        elif p[2] == '=':
            filhos = ['ATRIB', p[1], p[3]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        elif p[2] == '+=':
            filhos = ['ATRIBCOMP', p[1], p[3]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        elif p[2] == '-=':
            filhos = ['MENOSCOMP', p[1], p[3]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        elif p[2] == '*=':
            filhos = ['MULTCOMP', p[1], p[3]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        elif p[2] == '/=':
            filhos = ['DIVCOMP', p[1], p[3]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        else:
            filhos = [p[2], p[1], p[3]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
    elif len(p) == 5:
        filhos = ['IDENT', p[1], p[3]]
        p[0] = NodeAST(AST.EXPRESSAO, filhos)
    elif len(p) == 6:
        if p[1] == 'new':
            filhos = ['NEW', p[2], p[4]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
        else:
            filhos = ['COND', p[1], p[3], p[4]]
            p[0] = NodeAST(AST.EXPRESSAO, filhos)
    elif len(p) == 7:
        filhos = ['PONTEIRO', p[1], p[3], p[5]]
        p[0] = NodeAST(AST.EXPRESSAO, filhos)




def p_ArgumentosOpcionais(p):
    '''ArgumentosOpcionais : Argumentos
                           | empty '''
    p[0] = p[1]


def p_Argumentos(p):
    '''Argumentos : Argumentos VIRG Exp
                  | Exp '''
    if len(p) == 4:
        filhos = p[1] + [p[3]]
    else:
        filhos = [p[1]]
    p[0] = filhos


def p_EsqVal(p):
    '''EsqVal : IDENT ABRECOL Exp FECHACOL
              | IDENT '''
    if len(p) == 2:
        p[0] = NodeAST(AST.IDENT, p[1])
    else:
        ident = NodeAST(AST.IDENT, p[1])
        p[0] = [ident, p[3]]


def p_empty(p):
    'empty :'
    p[0] = None


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