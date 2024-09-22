

# FALTA ADC A FUNÇÃO DE MÉDICO FUNCIONALMENTE E ARQUIVO DE RANKING


import modExplicacoes
import random
from time import sleep

# Variável global para guardar os jogadores e acessar suas funções
jogadores = []
jogadores_vivos = 8

class Jogo:
    def __init__(self, usuario: int, player="", funcao=""):
        self.funcao = funcao # Função do jogador
        self.vida = 1 # Vida inicial do jogador
        self.player = player # Nome do jogador
        self.usuario = usuario # Identificador do jogador (0 para o usuário, outros números para NPCs)


    
    def selecionar_papeis(self, papel: str) -> None:
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

    
    def morte(self) -> None:
        # Esta função define o estado de vida do jogador como morto (vida = 0) caso ele seja assassinado.
        self.vida = 0
        if self.usuario == 0:
            print("")
            print(f"{self.player}, nesta madrugada você foi morto!")


    def revive(self) -> None:
        # Essa função é chamada quando o doutor escolher salvar alguém que seria assassinado, logo a pessoa "revive".
        self.vida = 1



def jogar() -> None: # Função principal que controla o jogo.
    global jogadores
    global jogadores_vivos

    modExplicacoes.inicio() #Dá boas vindas ao user e explicação sobre o jogo
    jogador = input("Digite seu nome antes de começarmos: ").strip().title()
    sleep(0.25)
    definir_funcoes(jogador) # Define as funções dos jogadores, recebe o jogador para falar o nome dele

    rodada = 1 # Inicia o contador de rodadas

    while jogadores_vivos > 2: # O jogo continua enquanto houver mais de 2 jogadores vivos
        sleep(0.5)
        modExplicacoes.mensagem_de_rodada(rodada)
        morto = matar() # O mafioso mata alguém durante a noite, o qual será guardado nessa variável

        if verificar_morte(morto) == True: # O jogador morreu e deseja encerrar o jogo
            break

        if morto != 0:
            sleep(1)
            modExplicacoes.mensagem_morte_npc(morto)
            jogadores_vivos -= 1
            investigacao_xerife()

        if debate() == True:
            break

        rodada += 1 # Incrementa a rodada



def user_morto(jogador):
    global jogadores
    terminar = False
    print(f"Durante a noite, o assassino fez algo terrível... Invadiu a casa de {jogador} e cometeu um ato brutal.")
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
            terminar = True
        else:
            sleep(0.25)
            print("Continuando como telespectador... \n")
    except:
        print("Resposta inválida.")
    return terminar



def verificar_morte(morto:int) -> bool:
    global jogadores_vivos
    if morto == 0:
        if user_morto(jogadores[0].player):
            return True
        jogadores_vivos -= 1
    return False
    


def definir_funcoes(jogador: str):
    funcoes = ["d", "x", "m", "c", "c", "c", "c", "c"]

    func = random.choice(funcoes)

    # Preenche o papel do usuário e imprime para ele
    jogadores.append(Jogo(0, jogador))
    jogadores[0].selecionar_papeis(func)
    funcoes.remove(func)

    # Preenche os papéis dos jogadores que são computador
    for npc in range(1, 8):
        func = random.choice(funcoes) 
        jogadores.append(Jogo(npc, f"Jogador {npc}"))
        jogadores[npc].selecionar_papeis(func) 
        funcoes.remove(func)

    # Imprime a função de cada jogador -- apenas de teste para checar se o programa está correndo corretamente, na versão final isso deve ser retirado.
    for j in jogadores:
        print(f"Jogador {j.usuario}: {j.funcao}")



def matar() -> int:
    ''' Essa função é responsável por selecionar e matar um jogador. Caso o usuário for o mafioso, ele escolhe a vítima.
        Caso contrário, a vítima é escolhida aleatoriamente. A função checa se o alvo é válido ou não e também utiliza
        try except para tratar os erros do código (caso o usuário digite uma string invés de um int ou um int fora do 
        index permitido). '''

    global jogadores
    mata = False

    if jogadores[0].funcao == "mafioso":

        while mata == False:
            try:
                alvo = int(input("Digite o número do jogador que você deseja matar: "))

                if 0 < alvo < len(jogadores) and jogadores[alvo].vida == 1:
                    print("Alvo Válido.")
                    mata = True
                    jogadores[alvo].morte() # O alvo estará morto 
                    if jogadores[alvo].vida == 0: 
                        sleep(1)
                        print(f"O jogador {alvo} foi assassinado com sucesso.")   

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


def debate() -> bool:
    global jogadores_vivos
    sleep(2)
    print("Agora os jogadores vão debater para tentar achar o mafioso!")
    acusacao = acusa(jogadores_vivos)

    if acusacao[0] == 0:
        return True

    if acusacao[1] != -1:
        jogadores[acusa[1]].morte(True)
        sleep(0.5)
        print(f"O jogador {jogadores[acusa[1]].player} foi sentenciado a morte por seus companheiros! Ele foi eliminado.")

        if acusacao[1] == 0:
            sleep(0.5)
            print("Você foi eliminado!")
            return True
        
    return False



def medico(vitima: int) -> bool: 
    '''Essa função é para que o médico consiga escolher uma pessoa para proteger por noite. Caso o assassino tente matar o protegido pelo médico,
        esta pessoa não morrerá e 'reviverá' durante a noite.'''
    global jogadores
    reviveu = False
    escolha = False
    medico_vivo = False
    for buscando_vida in range(len(jogadores)):
        if jogadores[buscando_vida].funcao == 'doutor' and jogadores[buscando_vida].vida == 1:
            medico_vivo = True
    if jogadores[0].funcao == "doutor" and medico_vivo == True:
        while escolha == False:
            tentativa_de_salvar = int(input("Digite o nome do jogador que você deseja proteger nesta noite: "))
            if tentativa_de_salvar == vitima:
                jogadores[tentativa_de_salvar].revive()
                reviveu = True
                escolha = True
            elif tentativa_de_salvar != vitima and jogadores[tentativa_de_salvar].vida == 0:
                print("Este jogador morreu em outra noite... Infelizmente já é tarde demais para salvá-lo.")
            else:
                escolha = True
    elif medico_vivo == True:
        while escolha == False:
            escolha = random.randint(0, 7)
            if vitima == escolha:
                jogadores[tentativa_de_salvar].revive()
                reviveu = True
                escolha = True
            elif jogadores[tentativa_de_salvar].vida == 1:
                escolha = True
            
    return reviveu



def xerife() -> None:
    '''  Função responsável pela investigação do usuário quando ele for o xerife para tentar descobrir quem é o assassino.
         Caso o jogador descubra quem é o assassino, ele poderá tentar votar o assassino fora com os outros NPCs, que
         aleatoriamente irão concordar ou discordar dele.'''
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
                

def investigacao_xerife() -> None:
    global jogadores
    if jogadores[0].funcao == "xerife" and jogadores[0].vida == 1:
        xerife()


def acusa(quantidade_vivos: int) -> list[int, bool]: 
    '''Função principal responsável por fazer o debate de acusação entre os 8 jogadores.'''
    global jogadores
    resultado = False
    players_vivos = jogadores_vivos()

    if jogadores[0].vida == 0:
        print("\nJogadores vivos:", players_vivos)
        resultado, quantidade_vivos = acusacao_npcs(quantidade_vivos)
    else:
        print("Jogadores vivos:", players_vivos)
        resultado, quantidade_vivos = acusacao_jogadores(quantidade_vivos)

    return [quantidade_vivos, resultado]




def jogadores_vivos() -> list[str]:
    '''Função responsável por retornar uma lista dos players vivos, que será utilizada na função de acusar.'''
    global jogadores
    players_vivos = []

    for jogador in jogadores:
        if jogador.vida == 1:
            players_vivos.append(jogador.usuario)

    return players_vivos



def acusacao_npcs(quantidade_vivos: int) -> tuple[bool, int]:
    '''Função responsável por fazer a acusação dos NPCs, que será utilizada na função de acusar.'''
    global jogadores
    resultado = False
    ja_acusado = 0

    while not resultado:
        escolha = escolher_acusacao_npc(ja_acusado)
        voto = random.randint(1, 2)
        resultado, quantidade_vivos = votacao_npc(escolha, voto, quantidade_vivos)

        if not resultado:
            ja_acusado = escolha

    return resultado, quantidade_vivos



def escolher_acusacao_npc(ja_acusado: int) -> int:
    '''Função responsável por definir quem será o player acusado. Será utilizada na função de acusar.'''
    global jogadores
    acusacao = False

    while not acusacao:
        escolha = random.randint(1, 4)

        if escolha < len(jogadores) and jogadores[escolha].vida == 1 and escolha != ja_acusado:
            acusacao = True
            print(f"\nOs jogadores decidiram acusar o player {escolha}. Hora da votação!")

    return escolha



def votacao_npc(escolha: int, voto: int, quantidade_vivos: int) -> tuple[bool, int]:
    global jogadores
    if voto == 2 and jogadores[escolha].funcao != "mafioso":
        sleep(1)
        print("\nVotação concluída! O jogador acusado foi eliminado. Ele não era o mafioso!")
        quantidade_vivos -= 1
        jogadores[escolha].morte(True)
        return True, quantidade_vivos
    elif voto == 1 and jogadores[escolha].funcao == "mafioso":
        sleep(2)
        print("\nVotação concluída! O jogador acusado foi eliminado. Ele era o mafioso! A CIDADE VENCEU!")
        return True, 0
    else:
        sleep(2)
        print("\nVotação concluída! O jogador acusado não deve ser eliminado. Outra acusação será feita.")
        return False, quantidade_vivos



def acusacao_jogadores(quantidade_vivos: int) -> tuple[bool, int]:
    global jogadores
    resultado = False
    while not resultado:
        escolha_usuario = escolher_acusacao_jogador()
        resultado, quantidade_vivos = votacao_jogador(escolha_usuario, quantidade_vivos)
    return resultado, quantidade_vivos



def escolher_acusacao_jogador() -> int:
    global jogadores
    escolha = False
    while not escolha:
        escolha_usuario = int(input("\nDigite o número do player que você quer acusar: "))
        if escolha_usuario <= 0 or escolha_usuario > 8:
            print("Número inválido.")
        elif jogadores[escolha_usuario].vida == 0:
            print("\nEsse player já está morto. Escolha outro.")
        else:
            escolha = True
            print("Os jogadores estão decidindo quem eles querem acusar...")
    return escolha_usuario



def votacao_jogador(escolha_usuario: int, quantidade_vivos: int) -> tuple[bool, int]:
    global jogadores

    defesa_usuario = input(f"{jogadores[0].player}, você pode tentar se defender para se salvar. Digite sua defesa: ") 

    if escolha_usuario == 0:
        print(f"{jogadores[0].player} está tentando se defender!")
   
    else:
        exibir_defesa_jogador(escolha_usuario)

    voto_final = random.randint(0, 1)
    
    if voto_final == 1 and jogadores[escolha_usuario].funcao != "mafioso":
        print(f"O {jogadores[escolha_usuario].usuario} não era o mafioso! Boa sorte na próxima votação.")
        jogadores[escolha_usuario].morte(True)
        return True, quantidade_vivos - 1
    
    elif voto_final == 1 and jogadores[escolha_usuario].funcao == "mafioso":
        print(f"O {jogadores[escolha_usuario].usuario} ERA o mafioso! A CIDADE VENCEU!")
        jogadores[escolha_usuario].morte(True)
        return True, 0
    
    else:
        print(f"\nVotação concluída! O {jogadores[escolha_usuario].usuario} não foi eliminado.")
        return False, quantidade_vivos



def exibir_defesa_jogador(escolha_usuario: int):
    global jogadores
    lista_defesas = [
        "Eu não fiz nada! Nem estava acordado na última noite.",
        "Estava jogando no meu computador a noite inteira! Vão acusar outra pessoa!",
        "Eu não sei nem o que falar para me defender, mas não fui eu, por favor!",
        "Eu dormi cedo na última noite.",
        "Durante a última noite, eu estava saindo com a minha namorada."
    ]
    print(f"O {jogadores[escolha_usuario].player} vai se defender: \n")
    print(random.choice(lista_defesas))





# Chama a função principal para iniciar o jogo

if __name__ == "__main__":
    jogar()
