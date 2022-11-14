
import math
import random
import funcoes
from termcolor import colored

DADOS =  [

          {'titulo': 'Em que parte do corpo se encontra a epiglote?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Estômago', 'B': 'Pâncreas', 'C': 'Rim', 'D': 'Boca'},
          'correta': 'D'},

          {'titulo': 'Em que dia nasceu e em que dia foi registrado o Presidente Lula?',
          'nivel': 'dificil',
          'opcoes': {'A': '8 e 27 de outubro', 'B': '6 e 27 de outubro', 'C': '9 e 26 de outubro', 'D': '7 e 23 de outubro'},
          'correta': 'B'},
          #Essa pergunta deu 1 milhão de reais para uma pessoa na vida real

          {'titulo': 'Qual bebida traz uma larva dentro da sua garrafa?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Vinho', 'B': 'Rum', 'C': 'Saquê', 'D': 'Mezcal'},
          'correta': 'D'},

          {'titulo': 'Em qual cidade nasceu o presidente Delfin Moreira?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Cristina', 'B': 'Belém', 'C': 'Cabo Frio', 'D': 'Cuiabá'},
          'correta': 'A'},

          {'titulo': 'Como se chama um recife de coral formado em uma laguna?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Arqupélago', 'B': 'Mar Pequeno', 'C': 'Largo', 'D': 'Atol'},
          'correta': 'D'},

          {'titulo': 'Em qual cidade se localiza a "Cidade Proibida?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Pequim', 'B': 'Belém', 'C': 'Tóquio', 'D': 'Moscou'},
          'correta': 'A'},

          {'titulo': 'O cleptomaníaco tem como principal característica:',
          'nivel': 'dificil',
          'opcoes': {'A': 'mania de roubar', 'B': 'medo de escuro', 'C': 'mania de piscar', 'D': 'mania de perseguição'},
          'correta': 'A'},

          {'titulo': 'Que ramo da odontologia estuda os defeitos da dentição?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Ortodontia', 'B': 'Ortogradismo', 'C': 'Ortodoxia', 'D': 'Ortocinese'},
          'correta': 'A'},

          {'titulo': 'Que nome se dá à purificação por meio da água?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Abolição', 'B': 'Abnegação', 'C': 'Ablução', 'D': 'Abrução'},
          'correta': 'C'},

         {'titulo': 'Qual fruto é conhecido no Norte e Nordeste como "jerimum"?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Caju', 'B': 'Abóbora', 'C': 'Chuchu', 'D': 'Coco'},
          'correta': 'B'},


        ]



DADOS_NORMALIZADOS = funcoes.transforma_base(DADOS)

print(DADOS_NORMALIZADOS)