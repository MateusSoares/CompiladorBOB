lista = list()


class Ambiente:
    def __init__(self):
        self.amb = dict()


    def get_value(self, item):
        return self.amb[item]

    def __setitem__(self,key,value):
        self.amb[key] = value


    def set_function(self , a, b ,c ):
        tup = (a , b  ,c )
        if tup[0] == 'print':
            print(tup)
        elif tup[0] == 'scanf':
            print('ok')
        else:
            print(tup)

    def get_return_function(lista_de_retorno):
        return()


    def get_function_name(self):
        return 'name'