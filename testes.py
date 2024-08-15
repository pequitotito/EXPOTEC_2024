

import random
from time import sleep

# Variável global para guardar os jogadores e acessar suas funções
jogadores = []


class Jogo:
    def __init__(self, usuario, player="computador", funcao=""):
        self.funcao = funcao # Função do jogador
        self.vida = 1 # Vida inicial
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
            sleep(0.25)
            print(f"{self.player}, você é um {funcao}! 🤫🤫🤫")


    def morte(self, morte):
        if morte:
            self.vida = 0
            if self.usuario == 0:
                print("")
                print(f"{self.player}, nesta madrugada você foi morto!")


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
    

    # Preenche os papéis dos jogadores que são computador
    for npc in range(1, 5):
        func = random.choice(funcoes) 
        jogadores.append(Jogo(npc, f"Jogador {npc}"))
        jogadores[npc].selecionar_papeis(func) 
        funcoes.remove(func)

    # Imprime a função de cada jogador -- apenas de teste para checar se o programa está correndo corretamente, na versão final isso deve ser retirado.
    for j in jogadores:
        print(f"Jogador {j.usuario}: {j.funcao}")

    rodada = 1

    while jogadores_vivos > 3:

        lista_jogadores_vivos = []

        sleep(0.5)
        print("")
        print(":: RODADA ", rodada, "::")
        print("")
        morto = matar()

        # Se o morto for o usuário
        if morto == 0:
            print(f"Durante a noite, o assassino fez algo terrível... Invadiu a casa de {jogadores[0].player} e cometeu um ato brutal.")
            sleep(0.5)
            print(f"Vítima de 23 facadas, {morto} infelizmente não resistiu.")

            sleep(1)
            print(f"\n{jogadores[0].player}, você morreu!! 😞😞")
            saida = input("Deseja continuar assistindo o jogo? (Responda com Sim ou Não): ").strip().title()
            try:
                if (saida == "Nao") or (saida == "N") or (saida == "Não") or (saida == "Ñ"):
                    break
                else:
                    print("Continuando como telespectador... \n")
            except:
                print("Resposta inválida.")

            jogadores_vivos -= 1
        
        if morto != 0:
            sleep(1)
            frases_morte = [f"Nesta última madrugada, o Jogador {morto} foi assassinado no local de trabalho.", f"Na noite passada, o Jogador {morto} foi encontrado morto dentro de sua casa.", f"Nesta noite, o assassino matou o Jogador {morto}"]
            print(random.choice(frases_morte))
            jogadores_vivos -= 1



        # Jogadores vivos
        for i in range(0, len(jogadores)):
            if jogadores[i].vida == 1:
                lista_jogadores_vivos.append(jogadores[i].player)
        print("")
        print("Jogadores vivos:", lista_jogadores_vivos)

        break
        


def matar():
    global jogadores
    mata = False

    if jogadores[0].funcao == "mafioso":

        # try except para tratar os erros do código (caso o usuario digite uma string invés de um número ou número fora do index)
        while mata == False:
            try:
                alvo = int(input("Digite o número do jogador que você deseja matar: "))

                # Checa se o alvo é válido
                if 0 < alvo < len(jogadores) and jogadores[alvo].vida == 1:
                    print("Alvo Válido.")
                    # Checar se o usuário morreu ou nao, matar e retirar da lista
                    mata = True
                    jogadores[alvo].morte(True) # O True aqui simboliza que o alvo estará morto     

                else:
                        print("Esse jogador já morreu.")
            except:
                print("Jogador inválido, digite corretamente.")
    
    else:
        while mata == False:
            alvo = random.randint(0, 4)
            if jogadores[alvo].funcao != "mafioso" and jogadores[alvo].vida == 1:
                mata = True
                jogadores[alvo].morte(True) # Alvo sinalizado como morto
    
    return alvo # Retorna o jogador que morreu

jogar()

