class Ambiente:

    def __init__(self, dic_classe, dic_func):
        '''

        :param dic_classe: dicionario com infromacoes das classes
        :param dic_func: dicionario com infromacoes das funcoes

        struct da pilha:
        [nome_da_funcao, classe_da_funcao, se_e_static, variaveis]
        '''
        #pilha de ambiente
        self.ambiente = list()

        #definicao dos ambientes
        self.ambiente_local = list()
        self.ambiente_base = list()
        self.ambiente_instancia = list()
        self.ambiente_classe = list()

        self.dic_classe = dic_classe
        self.dic_func = dic_func

        pass

    def _inicia_ambientes(self):

        for func in self.dic_func:
            print(func)

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