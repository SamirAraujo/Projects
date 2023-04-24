## Feito por Samir Araújo

import random
import string

def jogar(tipo_jogo, dificuldade):

  # JOGO NÚMEROS

    if tipo_jogo == 'numeros':
        if dificuldade == 'muito facil':
            num_tentativas = 25
        elif dificuldade == 'facil':
            num_tentativas = 20
        elif dificuldade == 'medio':
            num_tentativas = 15
        elif dificuldade == 'dificil':
            num_tentativas = 10
        elif dificuldade == 'muito dificil':
            num_tentativas = 5
        elif dificuldade == 'vidente':
            num_tentativas = 1
        else:
            print('Dificuldade inválida.')
            print(" ")
            dificuldade = input('Escolha uma dificuldade válida: ').lower()
            jogar(tipo_jogo,dificuldade)
            return

        numero_secreto = 2 #random.randint(0, 200)
        print(f'Você tem {num_tentativas} tentativas para acertar o número secreto.')
        print(" ")

        for tentativa in range(num_tentativas):
            while True:
                try:
                    palpite = int(input('Digite um número entre 0 e 200: '))
                    if 0 <= palpite <= 200:
                        break
                    else:
                        print('Número inválido. Digite um número inteiro válido entre 0 e 200.')
                        print(" ")
                except ValueError:
                    print('Entrada inválida. Digite um número inteiro válido entre 0 e 200.')
                    print(" ")

            if palpite < numero_secreto:
                print('O número secreto é maior.')
                print(" ")
            elif palpite > numero_secreto:
                print('O número secreto é menor.')
                print(" ")
            else:
              if dificuldade == 'vidente':
                print(" ")
                print(f'Parabéns! Você acertou o número secreto em {tentativa + 1} tentativas.')
                print('''
                          ⣤⣼⣿⣿⣿⣿⣿⣿⣷⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣢⣾⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡟⠛⢻⠉⡉⠍⠁⠁⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠏⢠⢀⡼⡄⠃⠤⠀⠀⠀⠀⠀⡐⠸⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢰⣸⡎⣀⣷⣤⣶⣶⣶⣦⡀⠀⠈⠓⢿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣇⣤⣯⣿⣿⣿⣿⣿⣿⣿⣭⣯⡆⠀⠀⠘⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⣻⣿⣿⣼⠀⢹⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⢘⣿⠙⠡⢽⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣛⣿⣯⠏⠀⢀⣿⣿⣿⣯⣠⡀⠀⠀⠀⢀⣾⡏⠒⢻⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡟⢘⣏⣺⣤⣬⣭⣼⣿⣿⣯⡉⢻⣦⣌⣦⣾⣿⣿⡚⠾⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢹⡼⣿⣿⢼⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡿⣿⢿⡟⢳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣿⣧⡞⣻⣩⣽⡽⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⣇⣬⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⡿⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡛⣿⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡃⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⡟⠻⢿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣍⠓⠲⠤⢤⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠈⣿⡏⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠈⢯⡁⠀⠀⠀⠉⠹⠶⢤⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⢀⠹⣿⡆⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⣤⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⢩⠀⢸⡄⢹⣿⣦⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣤⡄⠀⢀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠋⡀⣀⣰⣿⠀⠄⠹⣾⣿⣿⡿⣿⠀⢠⣤⣀⣴⣤⣤⡴⠶⠶⠿⠿⠛⠛⠋⠉⠉⣠⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⢀⡱⠏⠉⡟⠃⠀⠀⠀⢸⣿⣿⠇⣿⡴⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠖⢋⣡⣶⣿⣂⡼⠁⠉⠙⠋⠙⠿⠟⣢⣄⢿⡟⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠈⠀⠀
⠀⠀⠀⢀⣠⠴⠚⠉⠉⠀⠀⠀⠀⠀⣸⡿⠟⠀⠀⠀⠀⠀⠀⠲⣾⡛⣿⣬⡄⠀⠀⠁⠠⣤⠆⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⡟⣿⡟⠀⠀⠂⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀
⠞⠁⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⡀⡀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠁⠆⠀⠀⠀
                
                ''')
                break
              else:
                print(" ")
                print(f'Parabéns! Você acertou o número secreto em {tentativa + 1} tentativas.')
                print(" ")
                break

            num_tentativas_restantes = num_tentativas - (tentativa + 1)
            print(f'Você tem {num_tentativas_restantes} tentativas restantes.')
          
        else:
            print(f'Você perdeu! O número secreto era {numero_secreto}.')
            

        while True:
              jogar_novamente = input('Deseja jogar novamente? (s/n)').lower()
              if jogar_novamente == 's':
                  print('Dificuldades disponíveis para jogo com numeros: muito facil, facil, medio, dificil, muito dificil, vidente')
                  print('Dificuldades disponíveis para jogo com letras:  facil, medio, dificil, vidente')
                  tipo_jogo = input("Escolha o tipo de jogo:",).lower()
                  dificuldade = input('Escolha uma dificuldade: ').lower()
                  jogar(tipo_jogo,dificuldade)
                  break
              elif jogar_novamente =='n':
                   print('Obrigado por jogar')
                   break
              else:
                    print('Resposta inválida')
# JOGO LETRAS
    elif tipo_jogo == 'letras':
        if dificuldade == 'facil':
             num_tentativas = 15
        elif dificuldade == 'medio':
            num_tentativas = 10
        elif dificuldade == 'dificil':
             num_tentativas = 5
        elif dificuldade == 'vidente':
             num_tentativas = 1
        else:
            print('Dificuldade inválida.')
            print(" ")
            dificuldade = input('Escolha uma dificuldade válida: ').lower()
            jogar(tipo_jogo,dificuldade)
            return

        letra_secreta = chr(random.randrange(ord('a'), ord('z')+1))
        print(f'Você tem {num_tentativas} tentativas para acertar a letra secreta.')
        print(" ")

        for tentativa in range(num_tentativas):
                while True:
                  try:
                    palpite = input('Digite uma letra de a-z: ').lower()
                    if len(palpite) == 1 and palpite.isalpha():
                        break
                    else:
                        print('Entrada inválida. Digite apenas uma única letra de a-z.')
                        print(" ")
                  except ValueError:
                    print('Entrada inválida. Digite apenas uma única letra de a-z.')
                    print(" ")

                if palpite < letra_secreta:
                  print('A letra secreta está depois da letra digitada.')
                  print(" ")

                elif palpite > letra_secreta:
                  print('A letra secreta está antes da letra digitada.')
                  print(" ")

                else:
                  print(f'Parabéns! Você acertou a letra secreta em {tentativa + 1} tentativas.')
                  print(" ")
                  break

                num_tentativas_restantes = num_tentativas - (tentativa + 1)
                print(f'Você tem {num_tentativas_restantes} tentativas restantes.')

        else:
            print(f'Você perdeu! A letra_secreta era {letra_secreta}.')

        while True:
            jogar_novamente = input('Deseja jogar novamente? (s/n)').lower()
            if jogar_novamente == 's':
                  print('Dificuldades disponíveis para jogo com numeros: muito facil, facil, medio, dificil, muito dificil, vidente')
                  print('Dificuldades disponíveis para jogo com letras:  facil, medio, dificil, vidente')
                  tipo_jogo = input("Escolha o tipo de jogo:",).lower()
                  dificuldade = input('Escolha uma dificuldade: ').lower()
                  jogar(tipo_jogo,dificuldade)
                  break
            elif jogar_novamente =='n':
                print('Obrigado por jogar')
                break
            else:
                print('Resposta inválida')

# TIPO DE JOGO INVÁLIDO

    else:
        print('Tipo de jogo inválido.')
        print(" ")
        tipo_jogo = input('Escolha um tipo de jogo válido: ').lower()
        jogar(tipo_jogo, dificuldade)
        
# ------------------------FIM FUNÇÃO-------------------------#

print(" _________________________________ ")
print("|                                 |")
print("|        JOGO ADIVINHAÇÃO         |")
print("|_________________________________|")
print(" ")

print('Dificuldades disponíveis para jogo com numeros: muito facil, facil, medio, dificil, muito dificil, vidente')
print('Dificuldades disponíveis para jogo com letras:  facil, medio, dificil, vidente')
tipo_jogo = input("Escolha o tipo de jogo:",).lower()
dificuldade = input('Escolha uma dificuldade: ').lower()
jogar(tipo_jogo,dificuldade)
