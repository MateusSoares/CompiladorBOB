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
        self.graph = Digraph('G', filename='sort.gv')
        self.graph.attr(size='6,6')

    def __getID(self, nome):
        self.seed += 1
        if not isinstance(nome, str):
            #print(nome.filhos)
            #print('sss')
            pass
        return 'i' + str(self.seed) + '__' + nome

    def constroiDicionario(self):
        nodo1 = self.__getID('Programa')
        no2 = self.__lerNo(self.tree)
        self.graph.edge(nodo1, no2)

    def __lerNo(self, subtree):
        g: NodeAST = subtree
        if g == None :
            nodo = self.__getID('NONE')
            return nodo
        elif g == 'static' :
            nodo = self.__getID('STATIC')
            return nodo
        elif g == 'nil' :
            nodo = self.__getID('NIL')
            return nodo
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
        elif g.tipo == AST.STRING:
            nodo = self.__getID('STRING')
            folha = self.__getID(g.filhos[0])
            self.graph.edge(nodo, folha)
            return nodo
        elif g.tipo == AST.LISTA_DEFINICAO:
            nodo = self.__getID('DEFINICOES')
            for com in g.filhos:
                nodoCom = self.__lerNo(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.CLASSE_DEF:
            nodo = self.__getID('CLASSE')
            for com in g.filhos:
                #print(com)
                nodoCom = self.__lerNo(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.LISTA_MEMBROS:
            nodo = self.__getID('MEMBROS')
            for com in g.filhos:
                #print(com)
                nodoCom = self.__lerNo(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.LISTA_VAR:
            nodo = self.__getID('LISTA_VAR')
            for com in g.filhos:
                nodoCom = self.__lerNo(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.MEMBRO_VAR:
            nodo = self.__getID('VAR')
            for com in g.filhos:
                #print(com)
                nodoCom = self.__lerNo(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.MEMBRO_FUNC:
            nodo = self.__getID('FUNC')
            for com in g.filhos:
                #print(com)
                nodoCom = self.__lerNo(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.FUNCAO_DEF:
            nodo = self.__getID('FUNCAO')
            for com in g.filhos:
                nodoCom = self.__lerNo(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.PARAMETROS:
            nodo = self.__getID('PARAMETROS')
            for com in g.filhos:
                nodoCom = self.__lerNo(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.ARGS:
            nodo = self.__getID('ARGUMENTOS')
            for com in g.filhos:
                nodoCom = self.__lerNo(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.LISTA_ARGS:
            nodo = self.__getID('LISTA_ARGS')
            for com in g.filhos:
                nodoCom = self.__lerNo(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.LISTA_TEMP:
            nodo = self.__getID('LISTA_TEMP')
            for com in g.filhos:
                nodoCom = self.__lerNo(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.SEQ_COM:
            nodo = self.__getID('SEQ_COM')
            for com in g.filhos:
                nodoCom = self.__lerNo(com)
                self.graph.edge(nodo, nodoCom)
            return nodo
        elif g.tipo == AST.COMANDO:
            if len(g.filhos) == 1:
                if g.filhos[0] == 'CONTINUE' or g.filhos[0] == 'BREAK':
                    nodo = self.__getID(g.filhos[0])
                    self.graph.edge(nodo, '-COMANDO')
                    return g.filhos[0]
                else:
                    #print(g.filhos[0].filhos[0])
                    nodo = self.__getID(g.filhos[0].filhos[0])
                    termo = self.__lerNo(g.filhos[0])
                    self.graph.edge(nodo, termo)
                    return nodo
            nodo = self.__getID(g.filhos[0])
            for x in g.filhos[1:]:
                termo = self.__lerNo(x)
                self.graph.edge(nodo, termo)
            return nodo
        elif g.tipo == AST.EXPRESSAO:
            if len(g.filhos) == 1:
                nodo = self.__getID(g.filhos[0].filhos[0])
                termo = self.__getID(g.filhos[0].filhos[1].filhos[0])
                #termo = self.__lerNo(g.filhos[0].filhos[1].filhos[0])
                self.graph.edge(nodo, termo)
                return nodo
            if g.filhos[0] == 'STRING' or g.filhos[0] == 'IDENT':
                nodo = self.__getID(g.filhos[0])
                termo = self.__getID(g.filhos[1].filhos[0])
                self.graph.edge(nodo, termo)
                return nodo
            nodo = self.__getID(g.filhos[0])
            #print(nodo)
            for x in g.filhos[1:]:
                #print(g.filhos[1].filhos)
                termo = self.__lerNo(x)
                self.graph.edge(nodo, termo)
            return nodo
        else:
            #print(g.tipo)
            raise TypeError('Tipo AST invalido')

    def imprime(self):
        self.graph.view()

class Semantico:

    def __init__(self, raiz):

        self.raiz = raiz
        self.hierarquia_classe = dict()
        self.funcao_tab_simbolos = dict()
        self.classe_tab_simbolos = dict()

        self.analisa_ast()

    def analisa_classe(self):

        g = self.raiz
        buffer_hierarquia = list()

        for com in g.filhos:
            if com.tipo == AST.CLASSE_DEF:
                h = com.filhos
                classe_id = h[0].filhos[0]
                classe_base = h[1]
                if classe_base == None:
                    dic_aux = {classe_id: [None, list()]}
                else:
                    classe_base = classe_base.filhos[0]
                    dic_aux = {classe_id: [classe_base, list()]}
                    buffer_hierarquia.append([classe_base, classe_id])
                self.hierarquia_classe.update(dic_aux)
        for com in buffer_hierarquia:
            if com[0] in self.hierarquia_classe:
                self.hierarquia_classe[com[0]][1].append(com[1])
            else:
                raise Exception(f'Classe {com[1]} herdando de uma classe inexistente: {com[0]}.')
                exit()


    def analisa_tabela_simbolos_funcao(self):

        g = self.raiz

        for com in g.filhos:
            if com.tipo == AST.FUNCAO_DEF:
                lista_parametros = list()
                lista_var_temp = list()
                h = com.filhos
                funcao_id = h[0].filhos[0]
                classe_id = h[1]
                if classe_id != None:
                    classe_id = h[1].filhos[0]
                j = h[2].filhos

                parametros = j[0].filhos
                for par in parametros:
                    lista_parametros.append(par.filhos)

                var_temporarias = j[1].filhos
                for var in var_temporarias:
                    lista_var_temp.append(var.filhos)

                comandos = h[3]

                dic_aux = {funcao_id: [classe_id, lista_parametros, lista_var_temp, comandos]}

                self.funcao_tab_simbolos.update(dic_aux)


    def analisa_tabela_simbolos_classe(self):

        g = self.raiz

        for com in g.filhos:
            if com.tipo == AST.CLASSE_DEF:
                lista_var_classe = list()
                lista_var_inst = list()
                lista_met_classe = list()
                lista_met_inst = list()
                c = com.filhos
                classe_id = c[0].filhos[0]
                m = c[2].filhos
                #j = m[0].filhos[0]
                for mem in m:
                    if  mem.tipo == AST.MEMBRO_VAR:
                        if mem.filhos[0] == 'static':
                            for variav in mem.filhos[1].filhos:
                                lista_var_classe.append(variav.filhos)
                        else:
                            for variav in mem.filhos[1].filhos:
                                lista_var_inst.append(variav.filhos)
                    elif mem.tipo == AST.MEMBRO_FUNC:
                        if mem.filhos[0] == 'static':
                            lista_met_classe.append(mem.filhos[1].filhos)
                        else:
                            lista_met_inst.append(mem.filhos[1].filhos)

                # static - variaveis de classe

                dic_aux = {classe_id: [lista_var_classe, lista_var_inst, lista_met_classe, lista_met_inst]}
                self.classe_tab_simbolos.update(dic_aux)

    def analisa_ast(self):

        self.analisa_classe()
        self.analisa_tabela_simbolos_classe()
        self.analisa_tabela_simbolos_funcao()







if __name__ == '__main__':
    nomeArquivo = 'teste_2_sort.bob'
    arquivo = open(nomeArquivo, 'r')
    text = arquivo.read()

    result = parser.parse(text, lexer=lexer)

    sem = Semantico(result)

    visao = InterpretaAST(result)
    visao.constroiDicionario()
    visao.imprime()


    print(sem.funcao_tab_simbolos)
    print(sem.classe_tab_simbolos)
    print(sem.hierarquia_classe)


