import math
import random
import funcoes
from termcolor import colored
#O programa funciona conforme o esperado, o jogo sempre apresenta para o jogador o estado atual do seu prêmio, 
# é apresentada uma mensagem ao final de cada jogo indicando se o jogador ganhou ou perdeu
#  e o jogador pode iniciar um novo jogo sem ter que executar o programa novamente.
# Adicionar 20 perguntas para A
#questoes = 1k, +4k, +5k, MEDIA+20k, +20k, +50k, DIFICIL+200k, +200k, +500k
DADOS =  [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Qual o coletivo de cães?',
          'nivel': 'facil',
          'opcoes': {'A': 'Matilha', 'B': 'Rebanho', 'C': 'Alcateia', 'D': 'Mandana'},
          'correta': 'A'},

          {'titulo': 'Qual é o triângulo que tem todos os lados diferentes?',
          'nivel': 'facil',
          'opcoes': {'A': 'Isóceles', 'B': 'Equilátero', 'C': 'Escaleno', 'D': 'Trapézio'},
          'correta': 'C'},

          {'titulo': 'Qual é o atantônimo de "malograr"?',
          'nivel': 'facil',
          'opcoes': {'A': 'Perder', 'B': 'Fracassar', 'C': 'Conseguir', 'D': 'Desprezar'},
          'correta': 'C'},

          {'titulo': 'Em que país nasceu Carmem Miranda?',
          'nivel': 'facil',
          'opcoes': {'A': 'Portugal', 'B': 'Brasil', 'C': 'Espanha', 'D': 'Desprezar'},
          'correta': 'A'},

          {'titulo': 'Qual foi o último Presidente do período da ditadura militar no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Emílio Medici', 'B': 'João Figueiredo', 'C': 'Ernesto Geisel', 'D': 'Arthur Antunes'},
          'correta': 'B'},

          {'titulo': 'O adjetivo "venoso" está relacionado a: ',
          'nivel': 'facil',
          'opcoes': {'A': 'Vela', 'B': 'Vento', 'C': 'Vênia', 'D': 'Veia'},
          'correta': 'D'},

          {'titulo': 'Quantos noves existem de 0 a 100',
          'nivel': 'facil',
          'opcoes': {'A': '10', 'B': '11', 'C': '20', 'D': '21'},
          'correta': 'C'},

          {'titulo': 'O que é aspartame?',
          'nivel': 'facil',
          'opcoes': {'A': 'Um jogo', 'B': 'Um prato francês', 'C': 'programa de televisão', 'D': 'Adoçante artificial'},
          'correta': 'D'},

          {'titulo': 'A qual grupo de samba pertence o vocalista netinho?',
          'nivel': 'medio',
          'opcoes': {'A': 'Negritude JR.', 'B': 'Katinguelê', 'C': 'Só para contrariar', 'D': 'Exaltasamba'},
          'correta': 'A'},

         {'titulo': 'Quem compôs o Hino da Independência?',
          'nivel': 'medio',
          'opcoes': {'A': 'Dom Pedro I', 'B': 'Manuel Bandeira', 'C': 'Castro Alvez', 'D': 'Maciel Calebe'},
          'correta': 'D'},
         
         {'titulo': 'Qual bicho transmite Doença de Chagas?',
          'nivel': 'medio',
          'opcoes': {'A': 'Abelha', 'B': 'Barata', 'C': 'Pulga', 'D': 'Barbeiro'},
          'correta': 'D'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

          {'titulo': 'Qual montanha se localiza entre a fronteira do Tibet com o Nepal?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Monte Everest', 'B': 'Monte Carlo', 'C': 'Monte Fuji', 'D': 'Monte Branco'},
          'correta': 'A'},

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

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
        ]

def main():
  parar = False
  while parar == False:
    funcoes.inicio()
    DADOS_NORMALIZADOS = funcoes.transforma_base(DADOS)
    premio = [0,1000,5000,10000,30000,50000,100000,300000,500000,1000000]
    enter = '\nAperte ENTER para continuar...'
    
    print(enter)

    print('O jogo já vai começar! Lá vem a primeira questão!')
    #colocar/n
    print('Vamos começar com questões do nível FACIL!')
    #colocar/n
    print(enter)
    dificuldades = ['facil','facil','facil','medio','medio','medio','dificil','dificil','dificil']
    i = 0
    acertos = 0
    pular = 3
    dicas = 2
    questoes = []
    jogo = True 

    while jogo:
      questao = funcoes.sorteia_questao(DADOS_NORMALIZADOS,dificuldades[i])
      if funcoes.valida_questao(questao) == {} and questao not in questoes:
        questoes.append(questao)
        print(funcoes.questao_para_texto(questao,i+1))
        resposta = input('Qual alternativa? ')
        resposta = resposta.lower()
        if resposta == 'pular' and pular != 0:
          pular -= 1
          i = i
        elif resposta == 'pular' and pular == 0:
          i = i
          print('Você não tem mais pulos disponiveis')
          print(funcoes.questao_para_texto(questao,i+1))
          resposta = input('Qual alternativa? ')
          if resposta == questao['correta'].lower() or resposta == questao['correta']:
            acertos +=1
            print(colored('Você acertou! Seu prêmio atual é {}'.format(premio[acertos]), 'green'))
            i +=1
        elif resposta == questao['correta'].lower() or resposta == questao['correta']:
          acertos +=1
          print(colored('Você acertou! Seu prêmio atual é {}'.format(premio[acertos]), 'green'))
          i +=1
        elif resposta == 'parar':
          print('Você fez uma escolha boa, era melhor parar mesmo. Irá sair com {} reais de premiação! Parabéns!'.format(premio[acertos]))
          parar = True
          break
        elif resposta == 'a' or resposta == 'b' or resposta == 'c' or resposta == 'd' : 
          if acertos == 0:
            print(colored('Que pena! Você errou e vai sair sem nada :(', 'yellow' )) 
            res = input('\nDeseja jogar novamente?(y/n)')
            if res == 'n':
              parar = True
              break
            else:
              parar = False
              break
          else:
            print('Que pena! Você errou, mas irá sair com {} reais!'.format(premio[acertos]))
            res = input('\nDeseja jogar novamente?(y/n)')
            if res == 'n':
              parar = True
              break
            else:
              parar = False
              break
              
            
        elif resposta == 'ajuda' and dicas != 0:
          print(colored(funcoes.gera_ajuda(questao), 'green'))
          print(funcoes.questao_para_texto(questao,i+1))
          dicas -=1
          resposta = input('Qual alternativa? ')
          if resposta == 'ajuda':
            print(colored('Você já pediu ajuda nessa questão', 'red'))
            print(funcoes.questao_para_texto(questao,i+1))
            resposta = input('Qual alternativa? ')
          if resposta == questao['correta'].lower() or resposta == questao['correta']:
            acertos +=1
            print(colored('Você acertou! Seu prêmio atual é {}'.format(premio[acertos]), 'green'))
            i +=1
        elif resposta == 'ajuda' and dicas == 0:
          print(colored('Você não tem mais ajudas disponiveis', 'red'))
          print(funcoes.questao_para_texto(questao,i+1))
          resposta = input('Qual alternativa? ')
          if resposta == questao['correta'].lower() or resposta == questao['correta']:
            acertos +=1
            print(colored('Você acertou! Seu prêmio atual é {}'.format(premio[acertos]), 'green'))
            i +=1
        else:
          print(colored('Opção inválida', 'red'))
          print(funcoes.questao_para_texto(questao,i+1))
          resposta = input('Qual alternativa? ')
          if resposta == questao['correta'].lower() or resposta == questao['correta']:
            acertos +=1
            print(colored('Você acertou! Seu prêmio atual é {}'.format(premio[acertos]), 'green'))
            i +=1
          else:
            if acertos == 0:
              print(colored('Que pena! Você errou e vai sair sem nada :(', 'yellow' )) 
              res = input('\nDeseja jogar novamente?(y/n)')
              if res == 'n':
                parar = True
                break
              else:
                break
                
            else:
              print('Que pena! Você errou, mas irá sair com {} reais!'.format(premio[acertos]))
              res = input('\nDeseja jogar novamente?(y/n)')
              if res == 'n':
                parar = True
                break
              else:
                parar = False
                break
                
              
          
        # se a resposta for errada da print no que está em baixo
        #print('Que pena! Você errou e vai sair sem nada :(' ) colocar em amarelo
        #if resposta == 

        parar = True
      else:
        i = i

    if acertos == 9:
      print('PARABÉNS, você zerou o jogo e ganhou o maior prêmio possível!')
      parar = True
      break
main()
