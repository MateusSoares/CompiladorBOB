from lexicoBob import tokens, lexer
from sintaticoBob import AST, NodeAST, parser
from semanticoBob import Semantico
from ambiente import Ambiente

if __name__ == '__main__':
    nomeArquivo = 'teste_1_soma.bob'
    arquivo = open(nomeArquivo, 'r')
    text = arquivo.read()

    result = parser.parse(text, lexer=lexer)

    sem = Semantico(result)

    amb = Ambiente(sem.classe_tab_simbolos, sem.funcao_tab_simbolos, sem.hierarquia_classe)

    #fazendo manualmente os comandos do teste_1_soma.bob

    amb.set_function('main', None, [])
    x = amb.set_function('scanf', None, ['Digite o primeiro numero: '])
    amb['x'] = ['var', 'int', x]
    y = amb.set_function('scanf', None, ['Digite o segundo numero: '])
    amb['y'] = ['var', 'int', y]

    amb.set_function('Soma', 'soma', [amb.get_value('x'), amb.get_value('y')])
    amb['a'] = amb.get_value('x')
    amb['b'] = amb.get_value('y')
    amb.get_return_function(None)

    amb.set_function('calcula', 'resultado', ['soma'])
    a = amb.get_value('a')
    b = amb.get_value('b')
    valor = a[2] + b[2]
    amb['result'] = ['var', 'int', valor]
    amb.get_return_function(amb.get_value('result'))

    valor = str(amb.get_value('resultado')[2])
    amb.set_function('print', None, ['O resultado é: ', valor])

    '''
    
    Alguns testes para entendimento
    
    amb.set_function('main', None, [])
    print(amb)
    amb.set_function('Soma', 'soma', [['x', 'int', '3'], ['y', 'int', '5']])
    amb['b'] = ['x', 'int', '3']
    amb.get_return_function(None)
    #Teste para ver que a variavel n fica no ambiente caso desempilhe
    #amb['b'] = ['x', 'int', '3']
    print(amb)
    amb.set_function('calcula', None, ['soma', ['x', 'int', '3'], ['y', 'int', '5'], ['y', 'int', '5']])

    amb.set_function('print', None, ['Numero: ', ['var', 'int', '15']])
    a = amb.set_function('scanf', None, ['Digite o numero: '])
    print(a)

    print(amb)

    '''