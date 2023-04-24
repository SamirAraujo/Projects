
# By: Samir Araujo dos Santos
# !pip install colorama   Tire "#" dessa linha, caso for rodar no google collab
from colorama import init, Fore, Back, Style
import random
class Baralho: # Constrói o baralho 

    suits = ['♣', '♦', '♥', '♠']
    rankings = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    colors = [ 'B' , 'R' ]

    def __init__(self):
        self.cartas = [f'{rank}{suit}{color}' for suit in self.suits for rank in self.rankings for color in self.colors]

    def sortear_carta(self): # Retorna uma carta formada aleatoriamente
        return random.choice(self.cartas)

    def __str__(self):
        return ' '.join(self.cartas)
    
def make_hand(baralho): # Forma a mão dos jogadores de forma aleatoria
    carta1 = baralho.sortear_carta()
    carta2 = baralho.sortear_carta()
    carta3 = baralho.sortear_carta()
    carta4 = baralho.sortear_carta()
    carta5 = baralho.sortear_carta()
    carta6 = baralho.sortear_carta()
    carta7 = baralho.sortear_carta()
    return [carta1, carta2, carta3, carta4, carta5, carta6, carta7]

def descartar_hand(hand): # Atualiza a mão com o descarte
    print("Sua mão atual é: ")
    print(" ")
    print("    1°     2°     3°     4°     5°     6°     7° ")
    print(Style.BRIGHT,hand,Style.RESET_ALL)
    print(" ")
    descarte = input("Escolha duas cartas para descartar (digite o número da carta (1-7) separado por espaço): ").split()
    print(" ")
    while len(descarte) != 2 or not all([d.isdigit() for d in descarte]) or not all([1 <= int(d) <= 7 for d in descarte]) or len(set(descarte)) != 2:
        descarte = input("Entrada inválida. Por favor, escolha duas cartas (1-7) para descartar (digite o número da carta separado por espaço): ").split()
  
    descarte = [int(d) - 1 for d in descarte]
    new_hand = [hand[i] for i in range(len(hand)) if i not in descarte]
    print(" ")
    print("Sua nova mão é: ")
    print(Style.BRIGHT+" ".join(new_hand),Style.RESET_ALL)
    print("------------------- ")
    return new_hand

def imprimir_placar(Score1,Score2): # Imprime o placar
  
  print(" _________________________________")
  print("|      Pontos jogador1:", Score1, "        |")
  print("|      Pontos jogador2:", Score2, "        |")
  print("|_________________________________|")

def imprimir_vitorioso(Score1,Score2): # Verifica quem foi o ganhador da partida
    if Score1 > Score2:
      print(" ")
      print("O JOGADOR 1 GANHOU A PARTIDA, PARABÉNS")
      print(" ")
      print( Fore.YELLOW + '''        ##########################          
         ##########################          
    #####################################    
 #########################################  
####      ######################       #### 
###       ######################        ### 
##        ######################        ### 
###     ##########################      ### 
###    ############################    #### 
 ###   ### #################### ###    ###  
  ####  ### ################## ####  ####   
   ####  ######################### #####    
    ######## ################ #########     
      ######  ##############   ######       
               ############                 
                 ########                   
                   ####                     
                   ####                     
                   ####                     
                   ####                     
               ############                 
            ##################              
            ##################              
            ###            ###              
            ### JOGADOR 1  ###              
            ###            ###              
            ##################              
            ##################              
          ######################            
         ########################           
 ''' + Style.RESET_ALL)
      print(" ")

    else:
      print(" ")
      print("O JOGADOR 2 GANHOU A PARTIDA, PARABÉNS")
      print(" ")
      print( Fore.YELLOW + '''        ##########################          
        ##########################          
   #####################################    
 #########################################  
####      ######################       #### 
###       ######################        ### 
##        ######################        ### 
###     ##########################      ### 
###    ############################    #### 
 ###   ### #################### ###    ###  
  ####  ### ################## ####  ####   
   ####  ######################### #####    
    ######## ################ #########     
      ######  ##############   ######       
               ############                 
                 ########                   
                   ####                     
                   ####                     
                   ####                     
                   ####                     
               ############                 
            ##################              
            ##################              
            ###            ###              
            ### JOGADOR 2  ###              
            ###            ###              
            ##################              
            ##################              
          ######################            
         ########################           
 ''' + Style.RESET_ALL )
      print(" ")

def checksuit(hand):  # Conta o número de naipes na mão (desempate por naipe)
     numsuit = [0,0,0,0]
     for card in hand:
        if card.find('♣') >= 0:
           numsuit[0] += 1

        elif card.find('♦') >= 0:
            numsuit[1] += 1

        elif card.find('♥') >= 0:
                numsuit[2] += 1

        elif card.find('♠') >= 0:
                numsuit[3] += 1    

     return numsuit

def numReds(hand): # Conta o número de vermelhas (desempate pela cor do baralho)    
     reds = 0
     for card in hand:
         if card.find('R') >= 0 :
            reds += 1

     return reds

def desempate_carta(): # Jogadores puxam carta do deck, até alguem puxar a maior (desempate final)
   ranking = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
   while True:
      cartajog1 = baralho.sortear_carta()
      cartajog2 = baralho.sortear_carta()

      if ranking[cartajog1[0]] > ranking[cartajog2[0]] :

        print("O jogador 1 puxou:", cartajog1)
        print("O jogador 2 puxou:", cartajog2)
        print(" ")
        return ' Na puxada de cartas o Jogador 1 ganhou.'
      
      if ranking[cartajog2[0]]  > ranking[cartajog1[0]]:

         print("O jogador 1 puxou:", cartajog1)
         print("O jogador 2 puxou:", cartajog2)
         print(" ")
         return ' Na puxada de cartas o Jogador 2 ganhou.'     

class PokerHand: # Define a mão ganhadora e quais são as combinações 

    def __init__(self, hand1, hand2):
        self.hand1 = hand1
        self.hand2 = hand2


    # Classifica a sequência de acordo com um valor retornado pela função "compare"
    def reason(self, value): 
         reasons = {
           9: "Straight flush",
           8: "Quina",
           7: "Quadra",
           6: "Full house",
           5: "Flush",
           4: "Sequencia",
           3: "Trinca",
           2: "Dois pares",
           1: "Par",
           0: "Carta Alta"
         } 
         return reasons[value[0]]
   
    # Define a mão ganhadora/Melhor combinação 
    def compare(self):
        cards = "23456789TJQKA"
        suits = "♣♦♥♠"

        # Transforma as cartas em um matrix 5x2
        def parse(hand):
          parsed = []
          for card in hand:
              parsed.append((cards.index(card[0]), suits.index(card[1])))
          parsed.sort(reverse=True)
          return parsed # e.g. parse("T♥ J♥ Q♥ K♥ A♥") = [(12, 2), (11, 2), (10, 2), (9,2), (8, 2)]

        # Conta o número de cada valor de carta na mão
        def count_values(parsed):
            count = [0] * 13
            for card in parsed:
                count[card[0]] += 1

            return count # e.g count_values(5♦ 5♣ 5♥ A♠ K♦) = [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 1]

        # Conta o número de cada suit de carta na mão
        def count_suits(parsed):
            count = [0] * 4
            for card in parsed:
                count[card[1]] += 1

            return count # count_suits(K♦ K♣ K♥ 2♠ A♠) --> [1, 1, 1, 2]

        # Verifica se é sequencia 
        def is_straight(parsed): 
            parsed.sort(reverse=True)  # Filtra as cartas por valor em ordem decrescente
            for i in range(4):
                if (parsed[i][0] - parsed[i + 1][0] != 1) and (parsed[i][0] - parsed[4][0] != 12):
                    return False
            return True
        
        def get_ace_value(parsed):
           parsed.sort(reverse=True)
           if (parsed[0][0]) == 12 and (parsed[4][0])  == 0:
              return 4
           return 0
      
        # Verifica se é flush
        def is_flush(parsed): 
            for i in range(4):
                if parsed[i][1] != parsed[i + 1][1]:
                    return False
            return True

        # Função que classifica as opção de mãos possiveis
        def best_hand(parsed):
            values = count_values(parsed)
            suits = count_suits(parsed)

            # Straight flush
            if is_straight(parsed) and is_flush(parsed):
               return (9, parsed[get_ace_value(parsed)][0])

            #Quina
            for i in range(13):
                if values[i] == 5:
                    return (8, i) 

            # Quadra
            for i in range(13):
                if values[i] == 4:
                    return (7, i)

            # Full house
            for i in range(13):
                if values[i] == 3:
                    for j in range(13):
                        if i != j and values[j] == 2:
                            return (6, i, j)

            # Flush
            if is_flush(parsed):
                return (5, parsed[0][0])

            # Sequencia
            if is_straight(parsed):
                return (4, parsed[get_ace_value(parsed)][0])

            # Trinca
            for i in range(13):
                if values[i] == 3:
                    return (3, i)

            # Dois pares
            pairs = []
            for i in range(13):
                if values[i] == 2:
                    pairs.append(i)
    
            if len(pairs) == 2:
                pairs.sort(reverse=True)
                return (2, pairs[0], pairs[1])

            # Par
            for i in range(13):
                if values[i] == 2:
                    return (1, i)

            # Carta alta
            return (0, parsed[0][0])

        parsed1 = parse(self.hand1)
        parsed2 = parse(self.hand2)
        hand1_value = best_hand(parsed1)
        hand2_value = best_hand(parsed2)
        handsuit1 = checksuit(self.hand1)
        handsuit2 = checksuit(self.hand2)
        reason1 = self.reason(hand1_value)
        reason2 = self.reason(hand2_value)
      
        if hand1_value > hand2_value:
          print(" ")
          return f"--> O jogador 1 vence,pois obteve: {reason1}, o outro jogador obteve: {reason2}"

        elif hand1_value < hand2_value:
          print(" ")
          return f" --> O jogador 2 vence,pois obteve: {reason2}, o outro jogador obteve: {reason1}"
        
        # Desempate por naipe
        elif handsuit1[3]>handsuit2[3] :
          return f"---> O Jogador 1 vence depois do empate de {reason1},pois tem cartas de naipe maior em mãos"

        elif handsuit1[3]<handsuit2[3] :
          return f"---> O jogador 2 vence depois do empate de {reason1},pois tem cartas de naipe maior em mãos"

        elif handsuit1[2]>handsuit2[2] :
          return f"---> O Jogador 1 vence depois do empate de {reason1},pois tem cartas de naipe maior em mãos" 

        elif handsuit1[2]<handsuit2[2] :
          return f"---> O jogador 2 vence depois do empate de {reason1},pois tem cartas de naipe maior em mãos"

        elif handsuit1[1]>handsuit2[1] :
          return f"---> O Jogador 1 vence depois do empate de {reason1},pois tem cartas de naipe maior em mãos"

        elif handsuit1[1]<handsuit2[1] :
          return f"---> O jogador 2 vence depois do empate de {reason1},pois tem cartas de naipe maior em mãos"
                  
        elif handsuit1[0]>handsuit2[0] :
          return f"---> O Jogador 1 vence depois do empate de {reason1},pois tem cartas de naipe maior em mãos"

        elif handsuit1[0]<handsuit2[0] :
          return f"---> O jogador 2 vence  depois do empate de {reason1},pois tem cartas de naipe maior em mãos"
        
        # Desempate por cor do baralho
        else:
            numred1 = numReds(self.hand1)
            numred2 = numReds(self.hand2)
            if numred1 > numred2:
              return f' ---> O Jogador 1 vence depois do empate de {reason1},pois tem mais cartas do baralho vermelho em mãos'
            
            elif numred2 > numred1:
              return f'---> O jogador 2 vence vence depois do empate de {reason1},pois tem mais cartas do baralho vermelho em mãos'
            
            else:
              return desempate_carta()

tutorial = True
oferece_teste = True
jogo_comeca = True
Score1,Score2 = 0,0

# Inicio do jogo

print(Style.BRIGHT + " _________________________________ " + Style.RESET_ALL)
print(Style.BRIGHT + "|                                 |" + Style.RESET_ALL)
print(Style.BRIGHT + "|     JOGO POKER LEEGA ACADEMY    |" + Style.RESET_ALL)
print(Style.BRIGHT + "|_________________________________|" + Style.RESET_ALL)
print(" ")

# Oferece tutorial
while tutorial:
  asktutorial = input(" Você deseja ver o tutorial antes de partir para o jogo? (s/n) ")
  if asktutorial == 's' :
     print(" ")
     print(''' O jogo usa dois baralhos de cartas, um azul e um vermelho, ambos misturados.
A classificação das mãos é a mesma do poker com a adição da quina, segue: em ordem decrescente: "Straight flush", "Quina", "Quadra", "Full house", "Flush", "Sequencia", "Trinca", "Dois pares", "Par", "Carta Alta".
O primeiro caracter é o valor da carta, o segundo é o naipe e o terceiro é a cor do baralho da carta. O caracter T é o 10(Ten).
Exemplo: T♣R = Dez de paus do baralho vermelho(Red), J♦B = Valete de ouros do baralho azul(Blue).

Cada jogador receberá 7 cartas.
O objetivo do jogo é fazer a melhor mão possível descartando 2 cartas. 
O jogo segue um formato de melhor de 5, o que significa que o primeiro jogador a vencer 3 rodadas é o vencedor.

Antes de começar cada rodada, os jogadores deve escolher 2 cartas para descartar. Escolha sabiamente seu descarte, levando em consideração as combinções e os critérios de desempate.
Nessa versão só é possível jogar 2 jogadores simultâneos.
Depois dos jogadores terem descartados as cartas, o computador indica a mão vencedora.

Se houver um empate entre as mãos, a combinação com carta mais alta presente vence.
Exemplo: FullHouse = J♦B,J♣R,J♦B,Q♣R,Q♦B ganharia de outro como o seguinte: Fullhouse = 9♦R,9♣R,9♦R,Q♦R,Q♣B.
Caso ainda esteja empatado, o desempate será pela mão que possui o número de cartas com maiores naipes. Em ordem crescente é: ('♣', '♦', '♥', '♠').

Caso o naipe não desempate, o novo critério de desempate será o número de cartas do baralho vermelho em mãos.
Por exemplo, se um jogador tiver três cartas vermelhas em sua mão e o outro jogador tiver duas, o jogador com três cartas vermelhas vencerá a rodada.

Caso ainda haja o empate, o último critério de desempate será o valor de cartas puxadas do baralho. 
Cada jogador irá puxar uma carta do baralho, o ganhador do round será o jogador que tiver puxado a carta com valor(ranking) mais alto em relação aos outros.
Serão puxadas cartas até haver desempate. ''')
     print(" ")
     tutorial = False

  elif asktutorial == 'n':
     tutorial = False
  else:
     print("Insira uma opção válida")

# Oferece teste de empate
while oferece_teste:
   teste = input(" Antes de iniciar um jogo, deseja validar o desempate de 2 mãos com Royal Straight Flush por naipe,cor do baralho ou puxando cartas?  Selecione: (naipe/cor/carta/n)  ")
   baralho = Baralho()
   if teste == 'naipe':
      print(" ")
      newhand1 = ['T♠R', 'J♠R', 'Q♠R', 'K♠R', 'A♠R']
      newhand2 = ['T♥R', 'J♥R', 'Q♥R', 'K♥R', 'A♥R']
      print("Mão 1:",newhand1)
      print("Mão 2:",newhand2)  
      print(" ")
      game = PokerHand(newhand1, newhand2)
      result = game.compare()
      print(result)
      print(" ")
      continue
   
   elif teste == 'cor':
      print(" ")
      newhand1 = ['T♥B', 'J♥R', 'Q♥B', 'K♥R', 'A♥B']
      newhand2 = ['T♥B', 'J♥R', 'Q♥B', 'K♥R', 'A♥R']
      print("Mão 1:",newhand1)
      print("Mão 2:",newhand2)  
      print(" ")
      game = PokerHand(newhand1, newhand2)
      result = game.compare()
      print(result)
      print(" ")
      continue

   elif teste == 'carta':
      print(" ")
      newhand1 = ['T♠R', 'J♠R', 'Q♠R', 'K♠R', 'A♠R']
      newhand2 = ['T♠R', 'J♠R', 'Q♠R', 'K♠R', 'A♠R']
      print("Mão 1:",newhand1)
      print("Mão 2:",newhand2)
      print(" ")
      game = PokerHand(newhand1, newhand2)
      result = game.compare()
      print(result)
      print(" ")
      continue
  
   elif teste == 'n':
      print(" ")
      print("Prosseguindo para o jogo ...")
      print(" ")
      oferece_teste = False

   else:
      print("Insira uma opção válida")

# Oferece começar uma partida
while jogo_comeca:
  print(" ")
  jogar = input(" Deseja começar o jogo? (s/n) ")
  print(" ")

  if jogar == 's':
    print(" Começando um jogo novo...")
    jogo_rodando = True
    break

  elif jogar =='n':
    print(" Você não quis jogar :-( ")
    break
 
  else:
    print("Insira uma opção válida")
    continue

while jogo_rodando:
  print(Style.BRIGHT + Fore.BLUE + "____________________________________________NOVA RODADA____________________________________________" + Style.RESET_ALL)
# Embaralha os baralhos
  baralho = Baralho()

# Forma a mão inicial do jogador 1
  print(" ")
  print(Fore.RED + Style.BRIGHT + " É a vez do Jogador 1 jogar " + Style.RESET_ALL)
  print(" ")
  hand1 = make_hand(baralho)

# Descarta duas cartas da mão do jogador 1 e forma a nova mão
  newhand1 = descartar_hand(hand1)

# Forma a mão inicial do jogador 2
  print(" ")
  print(Fore.RED + Style.BRIGHT + " Vez do Jogador 2 jogar " + Style.RESET_ALL)
  print(" ")
  hand2 = make_hand(baralho)

# Descarta duas cartas da mão do jogador 2 e forma a nova mão
  newhand2= descartar_hand(hand2)
 
  # input manual de teste # newhand1 = ['A♥B', '2♥R', '3♠B', '4♥R', '5♥R']
  # input manual de teste # newhand2 = ['T♥B', 'J♥R', 'Q♠B', 'K♥R', 'A♥R']


# Compara as mãos para definir o vencedor do round
  print(" ")
  print(Fore.RED + Style.BRIGHT + "              JOGADOR 1                                JOGADOR 2" + Style.RESET_ALL)
  print(Style.BRIGHT , newhand1," VS ", newhand2 , Style.RESET_ALL)
  print(" ")
  game = PokerHand(newhand1, newhand2)
  result = game.compare() 
  print(result)
# Atribuição de ponto a cada rodada
  if result.find('1') >= 0 :
     Score1 += 1

  elif result.find('2') >= 0:
     Score2 +=1

  elif desempate_carta().find('1') >= 0:
     Score1 += 1

  elif desempate_carta().find('2') >= 0: 
     Score2 += 1

  # Imprime o placar toda rodada
  imprimir_placar(Score1,Score2)
  if Score1 >= 3 or Score2 >= 3:
     imprimir_vitorioso(Score1,Score2)
     playagain = input(" Jogar novamente? (s/n) ")
     if playagain == 's':
         Score1 = 0
         Score2 = 0
         jogo_rodando = True

     elif playagain == 'n':
         print(" Obrigado por jogar")
         jogo_rodando = False

     else:
         print("Insira uma opção válida")
         continue
