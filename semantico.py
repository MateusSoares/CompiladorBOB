# ------------------------------------------------------------
# semantico.py
#
# Para proposito de debug: imprime a AST produzida
# ------------------------------------------------------------

from graphviz import Digraph

from sintatico import AST, NodeAST, parser
from lexico import tokens, lexer

class InterpretaAST:

    def __init__(self, tree):
        self.seed = 0
        self.tree = tree
        self.graph = Digraph('G', filename='semantico.gv')
        self.graph.attr(size='6,6')

    def __getID(self, nome):
        self.seed += 1
        return 'i' + str(self.seed) + '__' + nome

    def constroiVisao(self):
        nodo1 = self.__getID('Programa')
        nodo2 = self.__desenha(self.tree)
        self.graph.edge(nodo1, nodo2)

    def __desenha(self, subtree):
        if isinstance(subtree, str):
            nodo = self.__getID(subtree)
            return nodo
        g : NodeAST = subtree
        if g.tipo == AST.IDENT:
            nodo = self.__getID('IDENT')
            folha = self.__getID(g.filhos[0])
            self.graph.edge(nodo, folha)
            return nodo
        elif g.tipo == AST.NUMBER:
            nodo = self.__getID('NUMBER')
            folha = self.__getID(g.filhos[0])
            self.graph.edge(nodo, folha)
            return nodo
        elif g.tipo == AST.BLOCO:
            nodo = self.__getID('BLOCO')
            for com in g.filhos:
                nodoCom = self.__desenha(com)
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

    def imprime(self):
        self.graph.view()

# ====================================================================

if __name__ == '__main__':
    nomeArquivo = 'teste.txt'
    arquivo = open(nomeArquivo, 'r')
    text = arquivo.read()

    result = parser.parse(text, lexer=lexer)
    visao = InterpretaAST(result)
    visao.constroiVisao()
    visao.imprime()
