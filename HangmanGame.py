import random
import unicodedata

# Escolhe a palavra
while True:
    entrada = input("Digite uma palavra para ser adivinhada (sem símbolos, acentos serão ignorados): ").lower()
    print(" ")
    if entrada.isalpha() and not entrada.isdigit():
        # remove acentos da palavra
        palavra = unicodedata.normalize('NFKD', entrada).encode('ASCII', 'ignore').decode('ASCII')
        break
    else:
        print("A palavra não pode conter símbolos ou números. Tente novamente.")
        print(" ")

# Dica
print("\n" * 100)
dica = input("Insira a dica: ")


# Convidados
convidados = []
while len(convidados) < 5: 
    nome = input("Insira o nome de um convidado: ").lower()
    print(" ")
    if nome in convidados:
        print("Este nome já foi adicionado à lista. Tente novamente.")
        print(" ")
    else:
        convidados.append(nome)
        print("O convidado", nome, "foi adicionado à lista.")
        print(" ")

jogador = random.choice(convidados)
print('O jogador será', jogador)
print(" ")

# Letras erradas
letras_erradas = []

# Letras corretas
letras_corretas = []

# Desenho do boneco
boneco = [
    """
     +------+
     |      |
     |      
     |    
     |      
     |     
    ---
    """,
    """
     +------+
     |      |
     |      O
     |    
     |      
     |     
    ---
    """,
    """
     +------+
     |      |
     |      O
     |      |
     |      |
     |     
    ---
    """,
    """
     +------+
     |      |
     |      O
     |     \|
     |      |
     |     
    ---
    """,
    """
     +------+
     |      |
     |      O
     |     \|/
     |      |
     |      
    ---
    """,
     """
     +------+
     |      |
     |      O
     |     \|/
     |      |
     |     / 
    ---
    """,
    """
     +------+
     |      |
     |      O  
     |     \|/
     |      |
     |     / \
    ---
    """
]

# Loop principal do jogo
while True:
    # Mostra a palavra com as letras corretas adivinhadas
    print("Palavra: ", end="")
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

    # Mostra as letras erradas adivinhadas
    print("Letras erradas: ", end="")
    for letra in letras_erradas:
        print(letra, end=" ")
    print()

    # Verifica se o jogador ganhou
    ganhou = True
    for letra in palavra:
        if letra not in letras_corretas:
            ganhou = False
            break
    if ganhou:
        print("Parabéns, você ganhou e não foi enforcado!")
        break

    # Verifica se o jogador perdeu
    if len(letras_erradas) == 7:
        print("Você perdeu! A palavra era", palavra)
        print(boneco[7])
        break

    # Pede ao jogador para adivinhar uma letra
    letra = input("Adivinhe uma letra: ").lower()
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite uma única letra.")
        print(" ")
        continue

    # Verificar se a letra já foi adivinhada
    if letra in letras_corretas or letra in letras_erradas:
        print("Você já adivinhou essa letra!")
        print(" ")
        continue
      
    if letra in palavra:
        print("Você adivinhou uma letra correta!")
        print(" ")
        letras_corretas.append(letra)
        print("Dica: ",dica)

    else:
        print(" ")
        print("Você adivinhou uma letra errada!")
        print(" ")
        print("Dica: ",dica)
        print(" ")
        letras_erradas.append(letra)
        print(boneco[len(letras_erradas) - 1])
