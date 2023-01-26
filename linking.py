from forcasys import PartidaDeJogoDaForca
from interface import *
from random import choice

listaPalavras = []

with open("palavras.txt") as file:
    for line in file:
        listaPalavras.append(line.rstrip())
file.close()








# Lista salva os botões clicados, assim podendo serem bloqueados
# pelo setDisabled(True) mesmo depois de haver uma troca de mainWindow.
clickedButtons = []




# Esse arquivo era para ser mais povoado com funções como adivLetra() e adivPalavra() fazendo o link entre interface e o objeto do jogo.
# Mas eu percebi que 90% das vezes que eu precisava delas isso crashava o programa, então só fui passando as funções para o interface.py.
# Agora isso é praticamente um cemitério.
# Reformular o código com isso em mente seria o correto, I know.



# CLI test
"""
jogo1 = PartidaDeJogoDaForca("lava-roupa")
while not jogo1.finalizado:
    try:
        jogo1.adivinharLetra(input("Letra: "))

    except BaseException as erro:
        print(erro)

    finally:
        print(*jogo1.palavraStatus)
"""

