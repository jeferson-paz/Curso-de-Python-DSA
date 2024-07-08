# Import
import random
from os import system, name

# Função para desenhar o bonequinho enforcado
def desenha_bonequinho(erros):
    if erros == 0:
        print(" +---+")
        print(" |   |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("=========")
    elif erros == 1:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("     |")
        print("     |")
        print("     |")
        print("=========")
    elif erros == 2:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print(" |   |")
        print("     |")
        print("     |")
        print("=========")
    elif erros == 3:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("     |")
        print("=========")
    elif erros == 4:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("     |")
        print("=========")
    elif erros == 5:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("     |")
        print("=========")
    else:
        print(" +---+")
        print(" |   |")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("     |")
        print("=========")

# Função para Limpar a tela a cada execução
def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')

# Função para o jogo da forca
def game():
    
    limpa_tela()
    print('\nBem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')

    # Lista de palavras para o jogo
    palavras = [
        'banana', 'abacate', 'uva', 'morango', 'laranja',
        'manga', 'melancia', 'cereja', 'abacaxi', 'kiwi',
        'maracuja', 'pitanga', 'amora', 'pessego', 'framboesa',
        'carambola', 'graviola', 'tangerina', 'acerola', 'jabuticaba'
    ]

    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # List comprehension
    letras_descobertas = ['_' for _ in palavra]

    # Número de chances baseado no número de letras na palavra
    chances = len(palavra)

    # Lista para as letras erradas
    letras_erradas = []

    # Loop enquanto número de chances for maior do que zero
    while chances > 0:
        
        # Printa o bonequinho
        desenha_bonequinho(len(palavra) - chances)

        # Print
        print("Palavra: ", " ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # Verifica se a entrada é válida (apenas uma letra)
        if len(tentativa) != 1 or not tentativa.isalpha():
            print('Por favor, digite apenas uma letra.')
            continue

        # Verifica se a tentativa já foi feita
        if tentativa in letras_descobertas or tentativa in letras_erradas:
            print('Você já tentou essa letra. Tente novamente.')
            continue

        # Condicional
        if tentativa in palavra:
            for index, letra in enumerate(palavra):
                if tentativa == letra:
                    letras_descobertas[index] = letra
        else:
            letras_erradas.append(tentativa)

        chances -= 1

        # Condicional
        if "_" not in letras_descobertas:
            limpa_tela()
            desenha_bonequinho(len(palavra) - chances)
            print("\nVocê venceu, a palavra era:", palavra)
            break

    # Condicional
    if "_" in letras_descobertas:
        limpa_tela()
        desenha_bonequinho(len(palavra))
        print("\nVocê perdeu, a palavra era:", palavra)

# Função principal para gerenciar o loop do jogo
def main():
    while True:
        game()
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("\nObrigado por jogar! Até a próxima.")
            break

# Bloco main
if __name__ == "__main__":
    main()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")
