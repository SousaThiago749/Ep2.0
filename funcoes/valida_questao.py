def valida_questao(dicio):
    contador = 0
    titulo = 0
    nivel = 0
    opcoes = 0
    correta = 0
    retorno = {}
    dicioletras = {}

    if dicio == {}:
        return {'titulo': 'nao_encontrado', 'nivel': 'nao_encontrado', 'opcoes': 'nao_encontrado', 'correta': 'nao_encontrado', 'outro': 'numero_chaves_invalido'}

    for item in dicio.keys():
        contador+=1
        if item == 'titulo':
            titulo=1
        elif item == 'nivel':
            nivel=1
        elif item == 'opcoes':
            opcoes=1
        elif item == 'correta':
            correta=1

    if contador != 4:
        retorno['outro'] = 'numero_chaves_invalido'
    
    if 'titulo' in dicio.keys():
        y = dicio['titulo'].strip()
        if len(y) == 0:
            retorno['titulo'] = 'vazio'

    if titulo != 1:
        retorno['titulo'] = 'nao_encontrado'

    if nivel == 1:
        for bag,level in dicio.items():
            if bag == 'nivel':
                if level!='medio' and level!='facil' and level!='dificil':
                    retorno['nivel'] = 'valor_errado'
    else:
        retorno['nivel'] = 'nao_encontrado'
    
    if opcoes == 1:
        contador2 = 0
        a = 0
        b = 0
        c = 0
        d = 0
        
        for quantidade,resp in dicio['opcoes'].items():
            contador2+=1
            if quantidade == 'A':
                a =1
            if quantidade == 'B':
                b =1
            if quantidade == 'C':
                c =1
            if quantidade == 'D':
                d =1
        soma = a+b+c+d
        if contador2 != 4:
            retorno['opcoes'] = 'tamanho_invalido'
        elif contador2 == 4:
            if soma !=4:
                retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'
            else:
                for letra,resp in dicio['opcoes'].items():
                    x = resp.strip()
                    if len(x) == 0:
                        dicioletras[letra] = 'vazia'
        for letra, resp in dicioletras.items():
            if '{}' not in letra or '{}' not in resp:
                retorno['opcoes'] = dicioletras
    else:
        retorno['opcoes'] = 'nao_encontrado'

    if correta == 1:
        for corr, resposta in dicio.items():
            if corr == 'correta':
                if resposta != 'A' and resposta!='B' and resposta!='C' and resposta!='D':
                    retorno['correta'] = 'valor_errado'
    else:
        retorno['correta'] = 'nao_encontrado'
    

    return retorno


    


    