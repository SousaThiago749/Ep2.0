def transforma_base(perguntas):
    categoria = 'nivel'
    dicio2 = {}
    for pergunta in perguntas:
      quest = []
      if pergunta[categoria] not in dicio2.keys():
          dicio2[pergunta[categoria]] = []
          
      dicio2[pergunta[categoria]].append(pergunta)

    if perguntas == []:
        return {}

    return dicio2