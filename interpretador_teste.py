from lexicoBob import tokens, lexer
from sintaticoBob import AST, NodeAST, parser
from semanticoBob import Semantico
from ambiente import Ambiente

if __name__ == '__main__':
    nomeArquivo = 'test_bob.txt'
    arquivo = open(nomeArquivo, 'r')
    text = arquivo.read()

    result = parser.parse(text, lexer=lexer)

    sem = Semantico(result)

    amb = Ambiente(sem.classe_tab_simbolos, sem.funcao_tab_simbolos)

