

import random
from time import sleep

# Variável global para guardar os jogadores e acessar suas funções
jogadores = []


class Jogo:
    def __init__(self, usuario, player="", funcao=""):
        self.funcao = funcao # Função do jogador
        self.vida = 1 # Vida inicial do jogador
        self.player = player # Nome do jogador
        self.usuario = usuario # Identificador do jogador (0 para o usuário, outros números para NPCs)


    
    def selecionar_papeis(self, papel):
        # Esta função atribui uma função (mafioso, doutor, xerife, cidadão) ao jogador com base no papel selecionado.
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
        # Esta função define o estado de vida do jogador como morto (vida = 0) caso ele seja assassinado.
        if morte:
            self.vida = 0
            if self.usuario == 0:
                print("")
                print(f"{self.player}, nesta madrugada você foi morto!")


def jogar():
    # Função principal que controla o jogo.
    global jogadores

    print('''
MMMMMMMMM        MMMMMMMMMMMM              MMMMMMMMMMMM             MMMMMMMMMMMMMMMM    MMMM             MMMMMMMMMMMM                 ⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣤⣤       
MMMM   MMMM      MMMMM   MMMM             MMMM MMMM MMMM            MMMMMMMMMMMMMMMM    MMMM            MMMM MMMM MMMM                    ⢶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
MMMM    MMMM    MMMM     MMMM            MMMM        MMMM           MMMM                MMMM           MMMM        MMMM                  ⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
MMMM      MMM  MMM       MMMM           MMMM          MMMM          MMMM                MMMM          MMMM          MMMM                ⠠⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠛⠛⠋⠉
MMMM        MMM          MMMM          MMMM            MMMM         MMMMMMMMMM          MMMM         MMMM            MMMM  ⠀             ⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⠏⢠⣿⡀⠀⠀⢹⡟
MMMM         M           MMMM         MMMM    MMMMMMM   MMMM        MMMMMMMMMM          MMMM        MMMM    MMMMMMM   MMMM             ⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣀⣙⣂⣠⠼⠃⠀
MMMM                     MMMM        MMMM MMMMMMMMMMMMMM MMMM       MMMM                MMMM       MMMM MMMMMMMMMMMMMM MMMM              ⣾⣿⣿⣿⣿⣿⣿⣿⠁⠀
MMMM                     MMMM       MMMM                  MMMM      MMMM                MMMM      MMMM                  MMMM            ⢠⣿⣿⣿⣿⣿⣿⣿⡟⠀
MMMM                     MMMM      MMMM                    MMMM     MMMM                MMMM     MMMM                    MMMM           ⢸⣿⣿⣿⣿⣿⣿⣿⡇
MMMM                     MMMM     MMMM                      MMMM    MMMM                MMMM    MMMM                      MMMM           ⠛⠛⠛⠛⠻⠿⠛⠃
          ''')

    # O jogo inicia, explicação de como funciona o jogo e as funções (xerife, doutor, assassino e cidadãos)
    print("\nBem-vindo ao jogo Máfia! 🕵  🔪 🩸")
    print("")
    jogador = input("Digite seu nome antes de começarmos: ").strip().title()
    sleep(0.25)
    
    # INSERIR EXPLICAÇÃO SOBRE O JOGO // Em outra versão, escrever de modo mais bonitinho fazendo c uma interface, dentro de um quadrado

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

    rodada = 1 # Inicia o contador de rodadas

    while jogadores_vivos > 2: # O jogo continua enquanto houver mais de 2 jogadores vivos

        lista_jogadores_vivos = []

        sleep(0.5)
        print("")
        print(":: RODADA ", rodada, "::")
        print("")

        # O mafioso mata alguém durante a noite, o qual será guardado nessa variável
        morto = matar()

        # Se o morto for o usuário
        if morto == 0:
            print(f"Durante a noite, o assassino fez algo terrível... Invadiu a casa de {jogadores[0].player} e cometeu um ato brutal.")
            sleep(0.5)
            print(f"Vítima de 23 facadas, {jogadores[0].player} infelizmente não resistiu.")

            sleep(1)
            print(f"\n{jogadores[0].player}, você morreu!! 😞😞")
            sleep(0.5)
            saida = input("Deseja continuar assistindo o jogo? (Responda com Sim ou Não): ").strip().title()
            try:
                if (saida == "Nao") or (saida == "N") or (saida == "Não") or (saida == "Ñ"):
                    sleep(0.25)
                    print("Obrigado por jogar!")
                    break
                else:
                    sleep(0.25)
                    print("Continuando como telespectador... \n")
            except:
                print("Resposta inválida.")

            jogadores_vivos -= 1
        
        if morto != 0:
            sleep(1)
            frases_morte = [f"Nesta última madrugada, o Jogador {morto} foi assassinado no local de trabalho.", f"Na noite passada, o Jogador {morto} foi encontrado morto dentro de sua casa.", f"Nesta noite, o assassino matou o Jogador {morto}"]
            print(random.choice(frases_morte))
            jogadores_vivos -= 1

            xerife_investiga = xerife()  # O xerife realiza uma investigação
            if jogadores[0].funcao == "xerife" and jogadores[0].vida == 1:
                print(xerife_investiga)


        # Jogadores vivos
        for i in range(0, len(jogadores)):
            if jogadores[i].vida == 1:
                lista_jogadores_vivos.append(jogadores[i].player)
        print("")
        sleep(1)
        print("Jogadores vivos:", lista_jogadores_vivos)


        # Debate entre os jogadores para acusar o mafioso
        sleep(0.5)
        print("Agora a cidade irá debater para achar o mafioso!")
        sleep(0.5)

        acusado = False

        while acusado == False:

            if jogadores[0].vida == 0: # Caso o usuário esteja morto, a votação ocorre de maneira aleatória entre os NPCs
                suspeito = random.randint(1, len(lista_jogadores_vivos))
                if jogadores[suspeito].vida == 1:
                    print(f"Os jogadores decidiram acusar o {jogadores[suspeito].usuario}!")
                    acusado = True
            

            elif jogadores[0].vida == 1: # Caso o usuário esteja vivo, ele irá acusar alguém.
                sleep(0.5)
                suspeito_usuario = int(input("Digite o número do jogador que você deseja acusar:"))

                try: # Tratamento de erro caso o acusado seja inválido.
                    
                    if suspeito_usuario > 0 and suspeito_usuario < len(jogadores):
                        sleep(0.5)
                        print(f"Você acusou o {jogadores[suspeito_usuario].usuario}. Vamos ver se os outros jogadores concordam com você.")
                        acusado = True
                    
                    elif jogadores[suspeito_usuario].vida == 0:
                        sleep(0.5)
                        print(f"O {jogadores[acusado].player} está morto! Acuse com atenção, você pode estar matando alguém inocente.")
                    
                    else:
                        sleep(0.5)
                        print("Jogador inválido. Atenção na hora de acusar alguém!")

                except:
                    sleep(0.25)
                    print("Inválido, tente novamente.")


            npc_concordam_usuario = random.randint(1, 2) # 1 para SIM, CONCORDAM e 2 para NÃO CONCORDAM na decisão do acusado do usuário
        

            if npc_concordam_usuario == 1:
                    
                sleep(3)
                print(f"Os demais jogadores decidiram concordar com você e eliminar o {jogadores[suspeito_usuario].usuario}.")
                sleep(0.5)
                    
                if jogadores[suspeito_usuario].funcao == "mafioso":
                    # FUNÇÃO DE ACERTOU, MATAR O MAFIOSO, VITÓRIA DA CIDADE
                    print("Ele erá o mafioso!!!")
                    sleep(0.5)
                    resultado("vitoria_cidade")
                    jogadores[suspeito_usuario].morte(True)
                    break

                else:
                    # FUNÇÃO DE ERROU, MATAR O INOCENTE, CONTINUAR O JOGO
                    print(f"O {jogadores[suspeito_usuario].usuario} era inocente!! O mafioso continua solto por aí!")
                    jogadores[suspeito_usuario].morte(True)
                        
                        

            elif npc_concordam_usuario == 2:
                # print os usuarios n concordaram com vc e resolveram matar etc
                sleep(3)
                print(f"Os demais jogadores não concordaram com você e decidiram eliminar o {jogadores[suspeito].usuario}!")
                sleep(0.5)

                if jogadores[suspeito].funcao == "mafioso":
                        # FUNÇÃO DE ACERTOU, MATAR O MAFIOSO, VITÓRIA DA CIDADE
                    print("Ele erá o mafioso!!!")
                    sleep(0.5)
                    resultado("vitoria_cidade")
                    jogadores[suspeito_usuario].morte(True)
                    break

                else:
                    # FUNÇÃO DE ERROU, MATAR O INOCENTE, CONTINUAR O JOGO
                    print(f"O {jogadores[suspeito_usuario].usuario} era inocente!! O mafioso continua solto por aí!")
                    jogadores[suspeito_usuario].morte(True)
                        

            
        
        rodada += 1 # Incrementa a rodada

def matar():
    # Função responsável por selecionar e matar um jogador, dependendo da função do jogador.
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
        # Se o jogador não for o mafioso, o alvo é escolhido aleatoriamente
        while mata == False:
            alvo = random.randint(0, 4)
            if jogadores[alvo].funcao != "mafioso" and jogadores[alvo].vida == 1:
                mata = True
                jogadores[alvo].morte(True) # Alvo sinalizado como morto
    
    return alvo # Retorna o jogador que morreu



def medico(): # Essa função será feita na outra versão do projeto. O médico trabalhará após o mafioso para tentar salvar alguém ou a si mesmo durante a noite.
    pass      # Caso o escolhido do médico seja quem o mafioso escolheu, essa pessoa revive e ninguém é morta durante a noite.



def xerife():
    # Função responsável pela investigação do xerife, que tenta identificar o assassino.
    global jogadores
    acusacao = False

    if jogadores[0].funcao == "xerife":

        while acusacao == False:

            try:
                sleep(1)
                acusado = int(input("Digite o número do jogador que você deseja investigar se é o assassino ou não: "))

                if 0 < acusado < len(jogadores) and jogadores[acusado].vida == 1:
                    if jogadores[acusado].funcao == "mafioso":
                        sleep(0.5)
                        print(f"O {jogadores[acusado].player} é o assassino!!!")
                        sleep(0.5)
                        print("Converse com os outros moradores da Cidade para o eliminar!")
                        acusacao = True

                    else:
                        sleep(0.5)
                        print(f"O {jogadores[acusado].player} não é o assassino... Ele ainda está a solta. ")
                        acusacao = True

                elif jogadores[acusado].vida == 0:
                    sleep(0.5)
                    print(f"O {jogadores[acusado].player} já está morto!! Investigue outro jogador.")

                else:
                    sleep(0.5)
                    print(f"Jogador inválido. Tome cuidado com a investigação, Xerife {jogadores[0].player}.")

            except:
                sleep(0.25)
                print("Inválido, tente novamente.")
                


def debate(jogadores_vivos):
    global jogadores
    acusado_debate = False




def resultado(resultado_final):

    if resultado_final == "vitoria_cidade":
        return "CIDADE VENCEU! O mafioso tentou, porém não foi o suficiente!"
    
    elif resultado_final == "derrota_cidade":
        return "O MAFIOSO VENCEU! Ninguém conseguiu parar o mafioso com seus truques..."



# Chama a função principal para iniciar o jogo

jogar()

# Jogadores vivos
''' for i in range(0, len(jogadores)):
            if jogadores[i].vida == 1:
                lista_jogadores_vivos.append(jogadores[i].player)
        print("")
        sleep(1)
        print("Jogadores vivos:", lista_jogadores_vivos)

        rodada += 1'''
