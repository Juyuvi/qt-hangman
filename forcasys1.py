import utils

class PartidaDeJogoDaForca:


    def __init__(self, plvr):
        # Sempre que criar uma partida de Jogo da Forca, uma palavra para
        # ser adivinhada é exigida.
        self.palavra = plvr

        # Toda partida é um objeto e cada objeto
        # terá sua própria e única palavra.


        self.placar = ["_"] * len(self.palavra)
        # Um display com o status das letras acertadas e restantes.




    def validarString(self, string) -> bool:
        """
        Checa se a string é uma letra.

        Retorna True e um monte de erros.
        """

        # Se a string não tem o comprimento de apenas 1 caractere
        # (Senão não é uma letra, duuh).
        if (not len(string) == 1):
            raise Exception("string recebida não pode ser apenas uma letra")

        # Se a string por acaso é um número.
        elif (utils.isnumber(string)):
            raise Exception("string recebida é um número, não uma letra")

        else:
            return True

    def adivinharLetra(self, letra):
        if (self.validarString(letra)):

            if (letra in self.palavra):
                print("Taq")
            else:
                print("ta nao")


    def adivinharPalavra(self, palavra):
        print()

