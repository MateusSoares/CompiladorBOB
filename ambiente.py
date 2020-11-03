class Ambiente:

    def __init__(self, dic_classe, dic_func):
        '''

        :param dic_classe: dicionario com infromacoes das classes
        :param dic_func: dicionario com infromacoes das funcoes

        struct da pilha:
        [nome_da_funcao, dict_variaveis, var_de_retorno]
        '''
        #pilha de ambiente
        self.ambiente = list()

        #definicao dos ambientes
        self.ambiente_base = dict()
        self.ambiente_instancia = dict()
        self.ambiente_classe = dict()

        self.dic_classe = dic_classe
        self.dic_func = dic_func

        self._inicia_ambientes()

    def _inicia_ambientes(self):

        print(self.dic_func)
        for func_name in self.dic_func:

            values = self.dic_func[func_name]

            #se for funcao sem classe
            if values[0] is None:

                dados = {func_name: [None, None, values[1], values[2]]}

                print(func_name)



        pass

    def __setitem__(self, key, value):

        pass

    def get_value(self):

        pass

    def set_function(self):

        pass

    def get_return_function(self):

        pass


if __name__ == '__main__':



    print('alou')