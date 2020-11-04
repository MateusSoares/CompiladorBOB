import copy as cp


class Ambiente:

    def __init__(self, dic_classe, dic_func, dic_hierarquia):
        '''

        :param dic_classe: dicionario com infromacoes das classes
        :param dic_func: dicionario com infromacoes das funcoes

        struct da pilha:
        [nome_da_funcao, nome_classe, funcao_static, dict_variaveis, dic_instancia, var_de_retorno]

        '''
        #pilha de ambiente
        self.ambiente = list()

        #definicao dos ambientes
        self.ambiente_base = dict()
        self.ambiente_instancia = dict()
        self.ambiente_classe = dict()

        self.dic_classe = dic_classe
        self.dic_func = dic_func
        self.dic_hierarquia = dic_hierarquia

        self._init_ambiente()
        self.set_function('main', None, [])
        self.set_function('inicializa', None, ['func'])
        self.set_function('Baskara', None, [['x', 'int', '3'], ['y', 'int', '5'], ['y', 'int', '5']])

        self.__setitem__('x', ['var', 'int', '5'])

    def __setitem__(self, key, value):

        env = self.ambiente[-1]

        #caso esteja no ambiente local
        if key in env[3]:
            #caso não seja um objeto
            if not isinstance(env[3][key], dict):
                env[3][key] = value
            return

        #caso seja uma funcao static
        if env[2] == True:
            if key in self.ambiente_classe:
                self.ambiente_classe[key] = value
            return

        #caso seja uma funcao de classe
        if env[1] is not None:
            if key in env[4]:
                env[4][key] = value
            return

        raise Exception('Não existe a variável no ambiente atual.')

    def _init_ambiente(self):

        for classe_name in self.dic_classe:
            #cria um dicionario para as classes contendo as variaveis estaticas
            if classe_name not in self.ambiente_classe:
                aux = {classe_name: dict()}
                self.ambiente_classe.update(aux)
                aux = {classe_name: dict()}
                self.ambiente_instancia.update(aux)
            valor = self.dic_classe[classe_name]

            #preenche o dicionario do ambiente de classe
            for var_static in valor[0]:
                if len(var_static) == 1:
                    aux = {var_static[0]: ['var', None, None]}
                else:
                    aux = {var_static[0]: ['vetor', var_static[1], [None for i in range(0, var_static[1])]]}
                self.ambiente_classe[classe_name].update(aux)

            #verifica superclasse
            super_class = self.dic_hierarquia[classe_name][0]

            while super_class is not None:
                valor_aux = self.dic_classe[super_class]
                for var_static in valor_aux[0]:
                    if len(var_static) == 1:
                        aux = {var_static[0]: ['var', None, None]}
                    else:
                        aux = {var_static[0]: ['vetor', var_static[1], [None for i in range(0, var_static[1])]]}
                    self.ambiente_classe[classe_name].update(aux)
                super_class = self.dic_hierarquia[super_class][0]

            #preenche o dicionario do ambiente de instancia
            for var in valor[1]:
                if len(var) == 1:
                    aux = {var[0]: ['var', None, None]}
                else:
                    aux = {var[0]: ['vetor', var[1], [None for i in range(0, var[1])]]}
                self.ambiente_instancia[classe_name].update(aux)

            # verifica superclasse
            super_class = self.dic_hierarquia[classe_name][0]

            while super_class is not None:
                valor_aux = self.dic_classe[super_class]
                for var in valor_aux[1]:
                    if len(var) == 1:
                        aux = {var[0]: ['var', None, None]}
                    else:
                        aux = {var[0]: ['vetor', var[1], [None for i in range(0, var[1])]]}
                    self.ambiente_instancia[classe_name].update(aux)
                super_class = self.dic_hierarquia[super_class][0]

    def get_value(self, key):

        env = self.ambiente[-1]

        # caso esteja no ambiente local
        if key in env[3]:
            return env[3][key]

        # caso seja uma funcao static
        if env[2] == True:
            if key in self.ambiente_classe:
                return self.ambiente_classe[key]

        # caso seja uma funcao de classe
        if env[1] is not None:
            if key in env[4]:
                return env[4][key]

        raise Exception('Não existe a variável no ambiente atual.')

    def set_function(self, name_function, retorno, lista_argumentos):

        if name_function not in self.dic_func:
            raise Exception(f'Funcao nao encontrada: {name_function}')


        #funcao sem parametros ------------------------------------------------------
        if lista_argumentos == list():
            valor = self.dic_func[name_function]
            nome_classe = None
            funcao_static = None
            variaveis = dict()

            #verifica se tem variaveis temporarias
            if valor[2] != []:
                for var in valor[2]:
                    aux = None
                    aux = {var: ['var', None, None]}
                    variaveis.update(aux)

            tupla = [name_function, nome_classe, funcao_static, variaveis, dict(), retorno]

            #empilha o ambiente local
            self.ambiente.append(tupla)

            #retorna o SEQ_COM da funcao
            return valor[3]

        #funcao de classe ------------------------------------------------------
        elif isinstance(lista_argumentos[0], str):

            # pega informacoes da funcao
            valor = self.dic_func[name_function]
            nome_classe = valor[0]

            classe_valor = self.dic_classe[nome_classe]

            variaveis = dict()
            var_instancia = dict()

            #verifica se funcao e static
            if name_function in classe_valor[2]:
                funcao_static = True
            else:
                funcao_static = None
                var_instancia = self.ambiente[-1][3][lista_argumentos[0]]

            # verifica se tem passagem de parametro
            if valor[1] != []:
                if len(valor[1]) != len(lista_argumentos)-1:
                    raise Exception('Quantidade de argumentos diferentes.')
                cont = 1
                for var in valor[1]:
                    aux = {var: lista_argumentos[cont]}
                    variaveis.update(aux)
                    cont += 1

            # verifica se tem variaveis temporarias
            if valor[2] != []:
                for var in valor[2]:
                    aux = None
                    if len(var) == 1:
                        aux = {var: ['var', None, None]}
                    else:
                        aux = {var[0]: ['vetor', var[1], [None for i in range(0, var[1])]]}
                    variaveis.update(aux)

            tupla = [name_function, nome_classe, funcao_static, variaveis, var_instancia, retorno]

            # empilha o ambiente local
            self.ambiente.append(tupla)

            # retorna o SEQ_COM da funcao
            return valor[3]

        #funcao com parametros ------------------------------------------------------
        else:

            # pega informacoes da funcao
            valor = self.dic_func[name_function]
            nome_classe = valor[0]
            classe_valor = None

            if nome_classe != None:
                classe_valor = self.dic_classe[nome_classe]

            variaveis = dict()
            var_instancia = dict()
            funcao_static = None

            if classe_valor is not None:
                # verifica se funcao e static
                if name_function in classe_valor[2]:
                    funcao_static = True
                else:
                    funcao_static = None
                    if name_function == nome_classe:
                        aux = cp.copy(self.ambiente_instancia[name_function])
                        var_instancia.update(aux)

            # verifica se tem passagem de parametro
            if valor[1] != []:
                if len(valor[1]) != len(lista_argumentos):
                    raise Exception('Quantidade de argumentos diferentes.')
                cont = 0
                for var in valor[1]:
                    aux = {var: lista_argumentos[cont]}
                    variaveis.update(aux)
                    cont += 1

            # verifica se tem variaveis temporarias
            if valor[2] != []:
                for var in valor[2]:
                    aux = None
                    if len(var) == 1:
                        aux = {var: ['var', None, None]}
                    else:
                        aux = {var[0]: ['vetor', var[1], [None for i in range(0, var[1])]]}
                    variaveis.update(aux)

            tupla = [name_function, nome_classe, funcao_static, variaveis, var_instancia, retorno]

            # empilha o ambiente local
            self.ambiente.append(tupla)

            # retorna o SEQ_COM da funcao
            return valor[3]

        pass

    def get_return_function(self, value):

        #caso o nome da classe for igual ao nome da funcao retornar o obj
        env = self.ambiente[-1]
        if env[0] == env[1]:
            valor = cp.copy(env[4])
            var_retorno = env[-1]
            self.ambiente.pop()
            env = self.ambiente[-1]
            env[3][var_retorno] = valor
            return

        #caso tenha algo para retornar seta no ambiente anterior o recebido por parametro
        if env[-1] is not None:
            var_retorno = env[-1]
            self.ambiente.pop()
            env = self.ambiente[-1]
            env[3][var_retorno] = value
            return

        #caso não tenha o que retornar somente desempilha o ambiente
        self.ambiente.pop()

    def get_function_name(self):

        env = self.ambiente[-1]
        return env[1]

    def __str__(self):

        return str(self.ambiente[-1])

if __name__ == '__main__':

    print('alou')