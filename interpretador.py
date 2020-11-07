import sintaticoBob
from semanticoBob import Semantico
from sintaticoBob import AST, NodeAST, parser
from lexicoBob import tokens, lexer
from ambiente import Ambiente





def executa(ast):
    arv = ast

    for op in arv.filhos:
        if op.tipo == AST.COMANDO:
            for com in op.filhos:
                if isinstance(com,sintaticoBob.NodeAST):
                    if com.tipo == AST.EXPRESSAO:
                        executaExp(com.filhos)
                elif com == 'RETURN':
                    variavelRet = op.filhos[1].filhos[1].filhos[0]
                    ret = ambiente.get_return_function(ambiente.get_value(variavelRet))



def executaMain(ast):
    arv = ast

    for op in arv.filhos:
        if op.tipo == AST.COMANDO:
            for com in op.filhos:
                if com.tipo == AST.EXPRESSAO:
                    executaExp(com.filhos)

    ambiente.get_return_function(None)


def executaAritimeticas(exp):
    op = exp[0]

    val1 = exp[1].filhos
    if op == '+':
        val2 = exp[2].filhos[1].filhos[0]
        try:
            auxS = int(val2)
        except:
            tup = ambiente.get_value(val2)
            auxS = int(tup[2])


        if val1[0] == '+' or val1[0] == '-' or val1[0] == '*' or val1[0] == '/':
            return executaAritimeticas(val1) + auxS
        else:
            return executaAritimeticas(val1) + auxS

    elif op == '-':
        val2 = exp[2].filhos[1].filhos[0]
        try:
            auxS = int(val2)
        except:
            tup = ambiente.get_value(val2)
            auxS = int(tup[2])

        if val1[0] == '+' or val1[0] == '-' or val1[0] == '*' or val1[0] == '/':
            return executaAritimeticas(val1) - auxS

        else:
            return executaAritimeticas(val1) - auxS

    elif op == '*':
        val2 = exp[2].filhos[1].filhos[0]
        try:
            auxS = int(val2)
        except:
            tup = ambiente.get_value(val2)
            auxS = int(tup[2])

        if val1[0] == '+' or val1[0] == '-' or val1[0] == '*' or val1[0] == '/':
            return executaAritimeticas(val1) * auxS
        else:
            return executaAritimeticas(val1) * auxS

    elif op == '/':
        val2 = exp[2].filhos[1].filhos[0]
        try:
            auxS = int(val2)
        except:
            tup = ambiente.get_value(val2)
            auxS = int(tup[2])

        if val1[0] == '+' or val1[0] == '-' or val1[0] == '*' or val1[0] == '/':
            return int(executaAritimeticas(val1) / auxS)
        else:
            return executaAritimeticas(val1) / auxS


    else:
        if exp[0] == 'IDENT':
            tup = ambiente.get_value(val1[0])
            return int(tup[2])

        else:
            return int(val1[0])



def executaExp(exp):
    #print(exp)
    #print(ambiente.get_function_name())
    if exp[0] == 'ATRIB':
        pos1 = exp[1].filhos[0]
        pos2 = exp[2].filhos[0]
        if len(exp[1].filhos) == 2:
            print(exp[1].filhos[1].filhos[1].filhos)
        #print(exp[2].filhos)
        elif pos2 == 'FUNC_CALL':
            listaArgs = list()
            pos0 = exp[2].filhos[1].filhos[0]
            pos1 = exp[1].filhos[0]
            pos2 = exp[2].filhos[2]
            if pos2 is not None:
                for item in pos2.filhos:
                    if item.filhos[0].filhos[0] == 'STRING':
                        variav = item.filhos[0].filhos[1].filhos[0]
                        tup = ['var', 'string', variav]
                        listaArgs.append(tup)
                    elif item.filhos[0].filhos[0] == 'FLOAT':
                        variav = item.filhos[0].filhos[1].filhos[0]
                        tup = ['var', 'float', variav]
                        listaArgs.append(tup)
                    elif item.filhos[0].filhos[0] == 'INT':
                        variav = item.filhos[0].filhos[1].filhos[0]
                        tup = ['var', 'int', variav]
                        listaArgs.append(tup)
                    else:
                        variav = item.filhos[0].filhos[1].filhos[0]
                        valor = ambiente.get_value(variav)
                        listaArgs.append(valor)


            setF = ambiente.set_function(pos0, pos1, listaArgs)
            if setF is not None:
                if type(setF) is not sintaticoBob.NodeAST:
                    ambiente[pos1] = ['var', 'string', setF]
                elif isinstance(setF, sintaticoBob.NodeAST):
                    executa(setF)
                    if pos0.lower() == pos1.lower() :
                        ambiente.get_return_function(None)
                    else:
                        ambiente.get_return_function(ambiente.get_value(pos1))


        elif pos2 == 'INT':
            tup = ['var','int', exp[2].filhos[1].filhos[0]]
            ambiente[pos1] = tup
        elif pos2 == 'FLOAT':
            tup = ['var','float', exp[2].filhos[1].filhos[0]]
            ambiente[pos1] = tup
        elif pos2 == 'STRING':
            tup = ['var','string', exp[2].filhos[1].filhos[0]]
            ambiente[pos1] = tup
        elif pos2 == 'IDENT':
            valor = ambiente.get_value(exp[2].filhos[1].filhos[0])
            ambiente[pos1] = valor

        elif pos2 == '+' or pos2 == '-' or pos2 == '*' or pos2 == '/':
            valor = executaAritimeticas(exp[2].filhos)
            tup = ['var', 'int', valor]
            ambiente[pos1] = tup

        elif pos2 == 'PONTEIRO':
            listaArgs = list()
            aponta = exp[2].filhos[1].filhos[1].filhos[0]
            apontado = exp[2].filhos[2].filhos[0]
            listaArgs.append(aponta)
            if len(exp[2].filhos) > 3:
                pos3 = exp[2].filhos[3]
                if pos3 is not None:
                    for item in pos3.filhos:
                        if item.filhos[0].filhos[0] == 'STRING':
                            variav = item.filhos[0].filhos[1].filhos[0]
                            listaArgs.append(variav)
                        elif item.filhos[0].filhos[0] == 'INT':
                            variav = item.filhos[0].filhos[1].filhos[0]
                            listaArgs.append(variav)
                        elif item.filhos[0].filhos[0] == 'FLOAT':
                            variav = item.filhos[0].filhos[1].filhos[0]
                            listaArgs.append(variav)
                        else:
                            variav = item.filhos[0].filhos[1].filhos[0]
                            valor = ambiente.get_value(variav)
                            listaArgs.append(valor)
            res = ambiente.set_function(apontado , pos1, listaArgs)
            executa(res)
            #ret  = ambiente.get_return_function(ambiente.get_value(pos1))


        else:
            pass

    elif exp[0] == 'FUNC_CALL':
        listaArgs = list()
        pos1 = exp[1].filhos[0]
        pos2 = exp[2]
        for item in pos2.filhos:
            if item.filhos[0].filhos[0] == 'STRING':
                variav = item.filhos[0].filhos[1].filhos[0]
                tup = ['var', 'string', variav]
                listaArgs.append(tup)
            elif item.filhos[0].filhos[0] == 'FLOAT':
                variav = item.filhos[0].filhos[1].filhos[0]
                tup = ['var', 'float', variav]
                listaArgs.append(tup)
            elif item.filhos[0].filhos[0] == 'INT':
                variav = item.filhos[0].filhos[1].filhos[0]
                tup = ['var', 'int', variav]
                listaArgs.append(tup)
            else:
                variav = item.filhos[0].filhos[1].filhos[0]
                valor = ambiente.get_value(variav)
                listaArgs.append(valor)

        setF = ambiente.set_function(pos1, None, listaArgs)
        if setF is not None:
            if type(setF) is not sintaticoBob.NodeAST:
                ambiente[pos1] = ['var', 'string', setF]
            elif isinstance(setF,sintaticoBob.NodeAST):
                executa(setF)
                ambiente.get_return_function(ambiente.get_value(pos1))

    elif exp[0] == 'PONTEIRO':
        listaArgs = list()
        pos1 = exp[1].filhos[1].filhos[0]
        listaArgs.append(pos1)
        pos2 = exp[2].filhos[0]
        pos3 = exp[3]
        if pos3 is not None:
            for item in pos3.filhos:
                if item.filhos[0].filhos[0] == 'STRING':
                    variav = item.filhos[0].filhos[1].filhos[0]
                    listaArgs.append(variav)
                else:
                    variav = item.filhos[0].filhos[1].filhos[0]
                    valor = ambiente.get_value(variav)
                    listaArgs.append(valor)


        ambiente.set_function(pos2, None , listaArgs)



if __name__ == '__main__':
    #nomeArquivo = 'test_bob_classe.txt'
    nomeArquivo = 'teste_1_soma.bob'
    arquivo = open(nomeArquivo, 'r')
    text = arquivo.read()

    result = parser.parse(text, lexer=lexer)

    sem = Semantico(result)

    ambiente = Ambiente(sem.classe_tab_simbolos, sem.funcao_tab_simbolos, sem.hierarquia_classe)

    blocoMain  = ambiente.set_function('main', None, [])

    #blocoMain = result.filhos[0].filhos[3]

    executaMain(blocoMain)

'''
    if isinstance(item,sintaticoBob.NodeAST):
        #print(item.filhos)
'''

