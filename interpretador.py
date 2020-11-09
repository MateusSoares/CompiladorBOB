import sintaticoBob
from semanticoBob import Semantico
from sintaticoBob import AST, NodeAST, parser
from lexicoBob import tokens, lexer
from ambiente import Ambiente


def castVar(aux):
    if aux[1] == 'int':
        return int(aux[2])
    elif aux[1] == 'float':
        return float(aux[2])
    else:
        return aux[2]

def comparador(sinal, aux1, aux2):
    if sinal == '<':
        #print('LT')
        return aux1 < aux2
    elif sinal == '>':
        #print('GT')
        return aux1 > aux2
    elif sinal == '<=':
        #print('LE')
        return aux1 <= aux2
    elif sinal == '>=':
        #print('GE')
        return aux1 >= aux2
    elif sinal == '==':
        #print('EQ')
        return aux1 == aux2

def tipoVarRet(tipoop1, tipoop2, op1, op2):
    if tipoop1 == 'IDENT':
        aux1 = ambiente.get_value(op1)
        aux1 = castVar(aux1)
    elif tipoop1 == 'INT':
        aux1 = int(op1)
    elif tipoop1 == 'FLOAT':
        aux1 = float(op1)
    elif tipoop1 == 'STRING':
        aux1 = str(op1)
    if tipoop2 == 'IDENT':
        aux2 = ambiente.get_value(op2)
        aux2 = castVar(aux2)
    elif tipoop2 == 'INT':
        aux2 = int(op2)
    elif tipoop2 == 'FLOAT':
        aux2 = float(op2)
    elif tipoop2 == 'STRING':
        aux2 = str(op2)

    return aux1,aux2


def executaEnquanto(com):
    op1 = com[1].filhos[1].filhos[1].filhos[0]
    op2 = com[1].filhos[2].filhos[1].filhos[0]
    tipoop1 = com[1].filhos[1].filhos[0]
    tipoop2 = com[1].filhos[2].filhos[0]
    novaSeqCom = com[2]
    sinal = com[1].filhos[0]

    if tipoop1 == 'VETOR':
        tipoInd =com[1].filhos[1].filhos[2].filhos[0]
        index = com[1].filhos[1].filhos[2].filhos[1].filhos[0]
        tipoop1,op1 = tipoValorVetor(tipoInd, op1, index)



    if tipoop2 == 'VETOR':
        tipoInd = com[1].filhos[2].filhos[2].filhos[0]
        index = com[1].filhos[2].filhos[2].filhos[1].filhos[0]
        tipoop2, op2 = tipoValorVetor(tipoInd, op2, index)

    aux1, aux2 = tipoVarRet(tipoop1, tipoop2, op1, op2)

    comp = comparador(sinal,aux1,aux2)

    while(comp):
        executa(novaSeqCom)
        aux1,aux2 = tipoVarRet(tipoop1,tipoop2,op1,op2)
        comp = comparador(sinal, aux1, aux2)


def executaPara(com):
    #Atribuicao
    executaExp(com[1].filhos)
    # Condicao
    op1 = com[2].filhos[1].filhos[1].filhos[0]
    op2 = com[2].filhos[2].filhos[1].filhos[0]
    tipoop1 = com[2].filhos[1].filhos[0]
    tipoop2 = com[2].filhos[2].filhos[0]
    novaSeqCom = com[4]
    sinal = com[2].filhos[0]


    if tipoop1 == 'VETOR':
        tipoInd =com[1].filhos[1].filhos[2].filhos[0]
        index = com[1].filhos[1].filhos[2].filhos[1].filhos[0]
        tipoop1,op1 = tipoValorVetor(tipoInd, op1, index)



    if tipoop2 == 'VETOR':
        tipoInd = com[1].filhos[2].filhos[2].filhos[0]
        index = com[1].filhos[2].filhos[2].filhos[1].filhos[0]
        tipoop2, op2 = tipoValorVetor(tipoInd, op2, index)

    aux1, aux2 = tipoVarRet(tipoop1, tipoop2, op1, op2)


    comp = comparador(sinal, aux1, aux2)





    while (comp):
        executa(novaSeqCom)
        # incremento
        executaExp(com[3].filhos)
        #att variaveis
        aux1, aux2 = tipoVarRet(tipoop1, tipoop2, op1, op2)
        comp = comparador(sinal, aux1, aux2)



def executaMain(ast):
    arv = ast

    for op in arv.filhos:

        if op.tipo == AST.COMANDO:
            if len(op.filhos) == 1:
                executaExp(op.filhos[0].filhos)
            elif op.filhos[0] == 'IF':
                executaCond(op.filhos)
            elif op.filhos[0] == 'WHILE':
                executaEnquanto(op.filhos)
            elif op.filhos[0] == 'FOR':
                executaPara(op.filhos)
            else:
                pass


    ambiente.get_return_function(None)

def executa(ast):
    arv = ast

    for op in arv.filhos:
        if op.tipo == AST.COMANDO:
            if len(op.filhos) == 1:
                executaExp(op.filhos[0].filhos)
            elif op.filhos[0] == 'RETURN':
                variavelRet = op.filhos[1].filhos[1].filhos[0]
                ret = ambiente.get_return_function(ambiente.get_value(variavelRet))
            elif op.filhos[0] == 'IF':
                executaCond(op.filhos)
            elif op.filhos[0] == 'WHILE':
                executaEnquanto(op.filhos)
            elif op.filhos[0] == 'FOR':
                executaPara(op.filhos)
            else:
                pass

def tipoValorVetor(tipoInd, op1, index ):
    if tipoInd == 'INT':
        index = int(index)
    else:

        index = ambiente.get_value(index)
        index = int(index[2])


    vetAux = ambiente.get_value(op1)
    valor = vetAux[2][index]


    if isinstance(valor, int):
        tipoop1 = 'INT'
    elif isinstance(valor, float):
        tipoop1 = 'FLOAT'
    elif isinstance(valor, str):
        tipoop1 = 'STRING'
    return tipoop1,valor

def executaCond(op):
    op1 = op[1].filhos[1].filhos[1].filhos[0]
    op2 = op[1].filhos[2].filhos[1].filhos[0]
    tipoop1 = op[1].filhos[1].filhos[0]
    tipoop2 = op[1].filhos[2].filhos[0]
    novaSeqCom = op[2]
    sinal = op[1].filhos[0]

    if tipoop1 == 'VETOR':
        tipoInd =op[1].filhos[1].filhos[2].filhos[0]
        index = op[1].filhos[1].filhos[2].filhos[1].filhos[0]
        tipoop1,op1 = tipoValorVetor(tipoInd, op1, index)



    if tipoop2 == 'VETOR':
        tipoInd = op[1].filhos[2].filhos[2].filhos[0]
        index = op[1].filhos[2].filhos[2].filhos[1].filhos[0]
        tipoop2, op2 = tipoValorVetor(tipoInd, op2, index)

    aux1, aux2 = tipoVarRet(tipoop1, tipoop2, op1, op2)

    comp = comparador(sinal,aux1,aux2)

    if comp == True:
        executa(novaSeqCom)
    elif len(op) == 4:
        if op[3].filhos[0] == 'IF':
            executaCond(op[3].filhos)
        else:
            executa(op[3])


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


def setValor(tipo, valor):
    if tipo == 'IDENT':
        aux1 = ambiente.get_value(valor)
        aux1 = castVar(aux1)
    elif tipo == 'INT':
        aux1 = int(valor)
    elif tipo == 'FLOAT':
        aux1 = float(valor)
    elif tipo == 'STRING':
        aux1 = str(valor)


    return aux1


def atribVetor(exp):
    #print(exp)
    #nome do vetor
    pos1 = exp[1].filhos[0]
    #tipo do dado atribuido, ID, INT, etc
    tipo = exp[2].filhos[0]
    #index do vetor
    index = exp[1].filhos[1].filhos[1].filhos
    index = int(index[0])
    #valor que a posicao do vetor vai assumir
    valor = exp[2].filhos[1].filhos[0]
    #busca vetor que ja foi declarado no ambiente
    vet = ambiente.get_value(pos1)
    #tamanho do vetor
    tam_vet = vet[1]


    if tipo == 'VETOR':
        vetAux = ambiente.get_value(valor)
        tipo2 = exp[2].filhos[2].filhos[0]
        index2 = exp[2].filhos[2].filhos[1].filhos[0]
        if tipo2 == 'INT':
            index2 = exp[2].filhos[2].filhos[1].filhos[0]
            index2 = int(index2)
        else:
            index2 = ambiente.get_value(exp[2].filhos[2].filhos[1].filhos[0])
            index2 = int(index2)
        vet[2][index] = vetAux[2][index2]
    else:
        vet[2][index] = setValor(tipo, valor)
    tup = ['vetor', tam_vet, vet[2]]
    ambiente[pos1] = tup

    #print(ambiente.get_value(pos1)[2])








def executaExp(exp):
    #print(exp)
    #print(ambiente.get_function_name())
    if exp[0] == 'ATRIB':
        pos1 = exp[1].filhos[0]
        pos2 = exp[2].filhos[0]
        #Tratamento Vetor
        if len(exp[1].filhos) == 2:
            atribVetor(exp)
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
                    elif item.filhos[0].filhos[0] == 'VETOR':
                        tipoInd = item.filhos[0].filhos[2].filhos[0]
                        index = item.filhos[0].filhos[2].filhos[1].filhos[0]
                        variav = item.filhos[0].filhos[1].filhos[0]
                        tipo, variav = tipoValorVetor(tipoInd, variav, index)

                        tup = ['var', tipo.lower(), variav]
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
                    if pos0 == ambiente.get_class_name():
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

        elif pos2 == 'VETOR':
            valor = ambiente.get_value(exp[2].filhos[1].filhos[0])
            tipo = exp[2].filhos[2].filhos[0]
            if tipo == 'INT':
                index = exp[2].filhos[2].filhos[1].filhos[0]
                index = int(index)
            else:
                index = ambiente.get_value(exp[2].filhos[2].filhos[1].filhos[0])
                index = int(index)

            if isinstance(valor[2][index], int):
                tup = ['var','int', valor[2][index]]
            elif isinstance(valor[2][index], float):
                tup = ['var','float', valor[2][index]]
            elif isinstance(valor[2][index], str):
                tup = ['var','string', valor[2][index]]

            ambiente[pos1] = tup


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
                        elif item.filhos[0].filhos[0] == 'VETOR':
                            tipoInd = item.filhos[0].filhos[2].filhos[0]
                            index = item.filhos[0].filhos[2].filhos[1].filhos[0]
                            variav = item.filhos[0].filhos[1].filhos[0]
                            tipo, variav = tipoValorVetor(tipoInd, variav, index)

                            tup = ['var', tipo.lower(), variav]
                            listaArgs.append(tup)
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
            elif item.filhos[0].filhos[0] == 'VETOR':
                tipoInd = item.filhos[0].filhos[2].filhos[0]
                index = item.filhos[0].filhos[2].filhos[1].filhos[0]
                variav = item.filhos[0].filhos[1].filhos[0]
                tipo, variav = tipoValorVetor(tipoInd, variav, index)

                tup = ['var', tipo.lower() , variav]
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
        aponta = exp[1].filhos[1].filhos[0]
        apontado = exp[2].filhos[0]
        listaArgs.append(aponta)
        args = exp[3]
        #print(args.filhos[0].filhos[1].filhos[0])
        if args is not None:
            for item in args.filhos:
                #print(item.filhos[0].filhos[1].filhos[0])
                if item.filhos[0].filhos[0] == 'STRING':
                    variav = item.filhos[0].filhos[1].filhos[0]
                    listaArgs.append(variav)
                elif item.filhos[0].filhos[0] == 'INT':
                    variav = item.filhos[0].filhos[1].filhos[0]
                    listaArgs.append(variav)
                elif item.filhos[0].filhos[0] == 'FLOAT':
                    variav = item.filhos[0].filhos[1].filhos[0]
                    listaArgs.append(variav)
                elif item.filhos[0].filhos[0] == 'VETOR':
                    tipoInd = item.filhos[0].filhos[2].filhos[0]
                    index = item.filhos[0].filhos[2].filhos[1].filhos[0]
                    variav = item.filhos[0].filhos[1].filhos[0]
                    tipo, variav = tipoValorVetor(tipoInd, variav, index)

                    tup = ['var', tipo.lower(), variav]
                    listaArgs.append(tup)
                else:
                    variav = item.filhos[0].filhos[1].filhos[0]
                    valor = ambiente.get_value(variav)
                    listaArgs.append(valor)


        res = ambiente.set_function(apontado, None , listaArgs)
        #print(res.tipo)
        executa(res)

    elif exp[0] == 'ATRIBCOMP' or exp[0] == 'MENOSCOMP':
        variav = exp[1].filhos[0]
        tipo = exp[2].filhos[0]
        valor = exp[2].filhos[1].filhos[0]
        if tipo == 'INT':
            valor = int(valor)
        elif tipo == "FLOAT":
            valor = float(valor)
        elif tipo == "IDENT":
            valor = ambiente.get_value(variav)
            valor = castVar(valor)


        variavAux = ambiente.get_value(variav)
        valorVar = castVar(variavAux)

        if exp[0] == 'ATRIBCOMP':
            valorVar = valorVar + valor
        elif exp[0] == 'MENOSCOMP':
            valorVar = valorVar - valor
        tup = ['var', variavAux[1] , valorVar]
        ambiente[variav] = tup




    else :
        print('ola')
        pass



if __name__ == '__main__':
    #nomeArquivo = 'teste_1_soma.bob'
    nomeArquivo = 'testeCondRepet.txt'
    #nomeArquivo = 'testeVetor.txt'
    #nomeArquivo = 'teste_2_sort.bob'
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

