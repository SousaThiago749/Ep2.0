import random
def gera_ajuda(questao):
    numero = random.randint(1,2)
    alternativas = []
    dica = []
    for alternativa, resposta in questao['opcoes'].items():
        if alternativa != questao['correta']:
            alternativas.append(resposta)
    
    i = 0

    while i < numero:
        sorteio = random.choice(alternativas)
        dica.append(sorteio)
        i+=1
      
    print(dica)

    if numero == 1:
    
      return 'DICA:\nOpções certamente erradas: {} | {}'.format(dica[0],dica[0])

    else:
      
      return 'DICA:\nOpções certamente erradas: {} | {}'.format(dica[0],dica[1])



print(gera_ajuda({
  "titulo": "Qual destes parques não se localiza em São Paulo?!",
  "nivel": "facil",
  "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
  },
  "correta": "D"
}))