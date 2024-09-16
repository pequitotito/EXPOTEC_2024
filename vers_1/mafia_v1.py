
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

    
    def morte(self, morte: bool) -> bool:
        # Esta função define o estado de vida do jogador como morto (vida = 0) caso ele seja assassinado.
        if morte:
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

    definir_funcoes(jogador)

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


        sleep(2)
        print("Agora os jogadores vão debater para tentar achar o mafioso!")
        acusacao = acusa(jogadores_vivos)
        
        if acusacao[0] == 0:
            break

        if acusacao[1] != -1:
            jogadores[acusa[1]].morte(True)
            sleep(0.5)
            print(f"O jogador {jogadores[acusa[1]].player} foi acusado e eliminado!")

            if acusacao[1] == 0:
                sleep(0.5)
                print("Você foi eliminado!")
                break
        

        rodada += 1 # Incrementa a rodada



def definir_funcoes(jogador: str) -> None:
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
                


def acusa(quantidade_vivos: int) -> list[int, bool]:
    global jogadores
    resultado = False
    ja_acusado = 0
    players_vivos = []

	
    for i in range(0, len(jogadores)):
        if jogadores[i].vida == 1:
            players_vivos.append(jogadores[i].usuario)


    if jogadores[0].vida == 0:
        print("\nJogadores vivos:", players_vivos)
        while not resultado:
            acusacao = False
            while not acusacao:
                escolha = random.randint(1, 4)
                if escolha < len(jogadores) and jogadores[escolha].vida == 1 and escolha != ja_acusado:
                    acusacao = True
                    print("\nOs jogadores decidiram acusar o player", str(escolha) + ".\nHora da votação!")

            voto = random.randint(1, 2)

            if voto == 2 and jogadores[escolha].funcao != "mafioso":
                sleep(1)
                print("\nVotação concluída! O jogador acusado foi eliminado.")
                print("Ele não era o mafioso!")
                resultado = True
                quantidade_vivos = quantidade_vivos - 1
                jogadores[escolha].morte(True)

            elif voto == 1 and jogadores[escolha].funcao == "mafioso":
                sleep(2)
                print("\nVotação concluída! O player acusado foi eliminado. \n\nEle era o mafioso!\nA CIDADE VENCEU!")
                resultado = True
                quantidade_vivos = 0

            else:
                sleep(2)
                print("\nVotação concluída! Após o debate, os jogadores concluíram que o jogador acusado não deve ser eliminado. Logo, outra acusação deverá ser feita.")
                ja_acusado = escolha

        return [quantidade_vivos, False]
    
    else:
        print("Jogadores vivos: ", players_vivos)

    while not resultado:
        usuario_eliminado = False
        acusacao = False
        escolha = False
        
        while escolha == False:
            escolha_usuario = int(input("\nDigite o número do player que você quer acusar: "))

            if escolha_usuario <= 0 or escolha_usuario > 8:
                print("Número inválido.")

            elif jogadores[escolha].vida == 0:
                print("\nEsse player já está morto. Escolha outro para acusar.")
            
            else:
                escolha = True
                print("Os jogadores estão decidindo quem eles querem acusar...")

        escolha_jogador = jogadores[escolha_usuario].usuario
        decisao = random.randint(1, 2)

        if decisao == 1 and escolha_jogador != ja_acusado:
            print(f"Outros jogadores concordaram com você, e o Jogador {escolha_usuario} está sendo acusado!")

        else:
            print("\nOs outros jogadores não concordaram com você e acusaram outro player.")
            
            while acusacao == False:
                escolha_usuario = random.randint(0, len(jogadores) - 1)
                if jogadores[escolha_usuario].vida == 1 and escolha_usuario != ja_acusado and escolha != escolha_jogador:
                    acusacao = True

                    if escolha == 0:
                        print("Os outros jogadores decidiram acusar você!!!")

                    else:
                        print(f"Os outros jogadores decidiram acusar o Jogador {escolha_usuario}.")

        if escolha_usuario == 0:
            defesa_usuario = input(f"{jogadores[0].player}, você pode tentar se defender para se salvar. Digite sua defesa: ")
            # a defesa do usuario nao serve para os npcs formarem opiniao, é apenas para o usuario ser uma sensação disso

        else:
            lista_defesas = ["Eu não fiz nada! Nem estava acordado na última noite.", 
                             "Estava jogando no meu computador a noite inteira! Vão acusar outra pessoa!", 
                             "Eu não sei nem o que falar para me defender, mas não fui eu, por favor!",
                             "Eu dormi cedo na última noite.", 
                             "Durante a última noite, eu estava saindo com a minha namorada."]
            print(f"O {jogadores[escolha_usuario].player} vai se defender: \n")
            print(random.choice(lista_defesas))
            voto_usuario = input("Você deseja acusá-lo ou não? ") # novamente, apenas para o jogador sentir que está votando
            sleep(2)
            print("Contabilizando os votos de todos os jogadores...")

        voto_final = random.randint(0, 1)

        if voto_final == 1 and jogadores[escolha_usuario].funcao != "mafioso":
            print(f"O {jogadores[escolha_usuario].usuario} não era o mafioso! Boa sorte votando da próxima vez.")
            resultado = True
            quantidade_vivos -= 1
            jogadores[escolha_usuario].morte(True)

        elif voto_final == 1 and jogadores[escolha_usuario].funcao == "mafioso":
            print(f"O {jogadores[escolha_usuario].usuario} ERA o mafioso!")
            print("A CIDADE VENCEU!")
            resultado = True
            quantidade_vivos = 0
            jogadores[escolha_usuario].morte(True)
            return 0, escolha
        
        else:
            print(f"\nVotação concluída! O {jogadores[escolha_usuario].usuario} não foi eliminado!")
            ja_acusado = escolha
			
            if voto_final == 1 and escolha == 0:
                usuario_eliminado = True
		
    return [quantidade_vivos, usuario_eliminado]




# Chama a função principal para iniciar o jogo

if __name__ == "__main__":
    jogar()
