def questao_para_texto(questao,numero):
    retorno = '''

----------------------------------------
QUESTAO {}

{}

RESPOSTAS:
A: {}
B: {}
C: {}
D: {}

'''.format(numero,questao['titulo'],questao['opcoes']['A'],questao['opcoes']['B'],questao['opcoes']['C'],questao['opcoes']['D'])
    return retorno



print(questao_para_texto({
  "titulo": "Qual destes parques não se localiza em São Paulo?!",
  "nivel": "facil",
  "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
  },
  "correta": "D"
},5))