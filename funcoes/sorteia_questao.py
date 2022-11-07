from random import choice
def sorteia_questao(questoes,nivel):
    for level, questao in questoes.items():
        if level == nivel:
            sorteio = choice(questao)

    return sorteio