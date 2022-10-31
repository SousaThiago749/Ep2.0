from random import choice
def sorteia_questao_inedida(questoes, nivel, lista):
    for level, questao in questoes.items():
        if level == nivel:
            sorteio = choice(questao)
            if sorteio in lista:
                sorteio = choice(questao)
            else:
                lista.append(sorteio)
                return sorteio
