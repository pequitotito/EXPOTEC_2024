

import random
from time import sleep

# Variável global para guardar os jogadores e suas funções
jogadores = []


class Jogo:
    def __init__(self, usuario, player="computador", funcao=""):
        self.funcao = funcao
        self.vida = 1
        self.player = player
        self.usuario = usuario


    
    def selecionar_papeis(self, papel):
        funcao = ""
        if papel == "m":
            funcao = "mafioso"
        if papel == "d":
            funcao = "doutor"
        if papel == "x":
            funcao = "xerife"
        if papel == "c":
            funcao = "cidadão"
        
        self.funcao = funcao

        # Se o papel que está sendo escolhido for o do usuário, imprime o nome e mostra a função do usuário
        if self.usuario == 0:
            print("")
            print(f"{self.player}, você é um {funcao}! 🤫🤫🤫")



def jogar():
    global jogadores

    # O jogo inicia, explicação de como funciona o jogo e as funções (xerife, doutor, assassino e cidadãos)
    print("Bem-vindo ao jogo Cidade Dorme! 🕵  🔪 🩸")
    print("")
    jogador = input("Digite seu nome antes de começarmos: ").strip().title()
    sleep(0.25)
    
    jogadores_vivos = 5


    # Define as funções disponíveis
    funcoes = ["d", "x", "m", "c", "c"]

    func = random.choice(funcoes)

    # Preenche o papel do usuário e imprime para ele
    jogadores.append(Jogo(0, jogador))
    jogadores[0].selecionar_papeis(func)
    funcoes.remove(func)
    
    for npc in range(1, 5):
        func = random.choice(funcoes) 
        jogadores.append(Jogo(npc))
        jogadores[npc].selecionar_papeis(func) 
        funcoes.remove(func)

    # Imprime a função de cada jogador
    #for j in jogadores:
    #    print(f"Jogador {j.usuario}: {j.funcao}")


    rodada = 1

    while jogadores_vivos > 3:

        sleep(0.5)
        print(":: RODADA ", rodada, "::")
        print()
        break

jogar()
