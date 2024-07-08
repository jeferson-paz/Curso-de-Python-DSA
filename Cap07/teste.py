import random
import os

# Função para limpar a tela
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para desenhar o bonequinho enforcado
def desenha_bonequinho(erros):
    # Lista com as partes do boneco enforcado
    bonequinho = [
        """
         +---+
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]

    # Imprime apenas as linhas necessárias de acordo com o número de erros
    print(bonequinho[erros])

# Função para o jogo da forca
def jogo_forca():
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

    # Lista de letras descobertas
    letras_descobertas = ['_' for _ in palavra]

    # Número de chances baseado no número de letras na palavra
    chances = len(palavra)

    # Conjunto de letras erradas
    letras_erradas = set()

    while chances > 0:
        limpa_tela()
        desenha_bonequinho(len(letras_erradas))

        print("Palavra: ", " ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(sorted(letras_erradas)))

        # Solicita uma letra do jogador
        tentativa = input("\nDigite uma letra: ").lower()

        # Valida se a entrada é uma letra do alfabeto
        if not tentativa.isalpha() or len(tentativa) != 1:
            print('Por favor, digite apenas uma letra.')
            continue

        # Verifica se a letra já foi tentada
        if tentativa in letras_descobertas or tentativa in letras_erradas:
            print('Você já tentou essa letra. Tente novamente.')
            continue

        # Verifica se a letra está na palavra
        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    letras_descobertas[i] = tentativa
        else:
            letras_erradas.add(tentativa)

        chances -= 1

        # Verifica se o jogador ganhou
        if "_" not in letras_descobertas:
            limpa_tela()
            desenha_bonequinho(len(letras_erradas))
            print("\nVocê venceu, a palavra era:", palavra)
            break

    # Se o jogador não acertar a palavra
    if "_" in letras_descobertas:
        limpa_tela()
        desenha_bonequinho(len(letras_erradas))
        print("\nVocê perdeu, a palavra era:", palavra)

# Função principal para gerenciar o loop do jogo
def main():
    while True:
        jogo_forca()
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("\nObrigado por jogar! Até a próxima.")
            break

# Execução do jogo
if __name__ == "__main__":
    main()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")
