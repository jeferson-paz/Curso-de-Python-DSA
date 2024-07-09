import random
from os import system, name

class Forca:
    def __init__(self):
        self.palavras = [
            'banana', 'abacate', 'uva', 'morango', 'laranja',
            'manga', 'melancia', 'cereja', 'abacaxi', 'kiwi',
            'maracuja', 'pitanga', 'amora', 'pessego', 'framboesa',
            'carambola', 'graviola', 'tangerina', 'acerola', 'jabuticaba'
        ]
        self.palavra = random.choice(self.palavras)
        self.letras_descobertas = ['_' for _ in self.palavra]
        self.letras_erradas = []
        self.chances = len(self.palavra)

    def desenha_bonequinho(self):
        estagios = [
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
        print(estagios[len(self.letras_erradas)])

    def limpa_tela(self):
        _ = system('cls' if name == 'nt' else 'clear')

    def exibe_status(self):
        self.desenha_bonequinho()
        print("Palavra: ", " ".join(self.letras_descobertas))
        print("\nChances restantes:", self.chances)
        print("Letras erradas:", " ".join(self.letras_erradas))

    def tentar_letra(self, tentativa):
        if tentativa in self.palavra:
            self.letras_descobertas = [
                letra if letra == tentativa else self.letras_descobertas[index]
                for index, letra in enumerate(self.palavra)
            ]
        else:
            self.letras_erradas.append(tentativa)
            self.chances -= 1

    def jogar(self):
        while self.chances > 0:
            self.limpa_tela()
            self.exibe_status()
            tentativa = input("\nDigite uma letra: ").lower()
            if len(tentativa) != 1 or not tentativa.isalpha():
                print('Por favor, digite apenas uma letra.')
                continue
            if tentativa in self.letras_descobertas or tentativa in self.letras_erradas:
                print('Você já tentou essa letra. Tente novamente.')
                continue
            self.tentar_letra(tentativa)
            if "_" not in self.letras_descobertas:
                self.limpa_tela()
                self.exibe_status()
                print("\nVocê venceu, a palavra era:", self.palavra)
                break
        else:
            self.limpa_tela()
            self.exibe_status()
            print("\nVocê perdeu, a palavra era:", self.palavra)

class JogoDaForca:
    @staticmethod
    def main():
        while True:
            jogo = Forca()
            jogo.jogar()
            jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
            if jogar_novamente != 's':
                print("\nObrigado por jogar! Até a próxima.")
                break

if __name__ == "__main__":
    JogoDaForca.main()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")