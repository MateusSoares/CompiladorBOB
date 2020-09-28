'''

    Analisador semantico para a linguagem Bob.

    Autores : Mateus Soares
            : Rodrigo Pacheco
    Data    : 28 de setembro de 2020

'''

from graphviz import Digraph

from sintaticoBob import AST, NodeAST, parser
from lexicoBob import tokens, lexer


class InterpretaAST:

    def __init__(self, tree):
        self.seed = 0
        self.tree = tree
        self.graph = Digraph('G', filename='semantico.gv')
        self.graph.attr(size='6,6')

    def __getID(self, nome):
        self.seed += 1
        return 'i' + str(self.seed) + '__' + nome

    def constroiDicionario(self):
        no1 = self.__getID('Programa')
        no2 = self.__lerNo(self.tree)
        self.graph.edge(no1, no2)

    def __lerNo(self, subtree):
        g: NodeAST = subtree
        if g.tipo == AST.IDENT:
            nodo = self.__getID('IDENT')
            folha = self.__getID(g.filhos[0])
            self.graph.edge(nodo, folha)
            return nodo
        elif g.tipo == AST.NUMBER:
            if g.filhos[0] == 'INT':
                nodo = self.__getID('INT')
                folha = self.__getID(g.filhos[1])
            elif g.filhos[0] == 'FLOAT':
                nodo = self.__getID('FLOAT')
                folha = self.__getID(g.filhos[1])
            self.graph.edge(nodo, folha)
            return nodo
        elif g.tipo == AST.STRING:
            nodo = self.__getID('STRING')
            folha = self.__getID(g.filhos[0])
            self.graph.edge(nodo, folha)
            return nodo
        elif g.tipo == AST.SEQ_COM:
            nodo = self.__getID('SEQ_COM')
            for com in g.filhos:
                nodoCom = self.__lerNO(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.COMANDO:
            nodo = self.__getID(g.filhos[0])
            for x in g.filhos[1:]:
                termo = self.__desenha(x)
                self.graph.edge(nodo, termo)
            return nodo
        elif g.tipo == AST.EXPRESSAO:
            nodo = self.__getID(g.filhos[0])
            if g.filhos[0] == 'NUMBER' or g.filhos[0] == 'NUMBER':
                folha = self.__getID(g.filhos[1])
                self.graph.edge(nodo, folha)
                return nodo
            for x in g.filhos[1:]:
                termo = self.__desenha(x)
                self.graph.edge(nodo, termo)
            return nodo
        else:
            raise TypeError('Tipo AST invalido')