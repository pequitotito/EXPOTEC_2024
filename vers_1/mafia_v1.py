


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
    '''Inicializa uma nova instância de um jogador no jogo, definindo atributos.
    O __init__ é responsável por criar e configurar um objeto jogador. Ele aceita
    três parâmetros: usuario, player, e função. Esses parâmetros são usados para 
    definir as características iniciais do jogador.'''

    
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

        '''Atribui um papel a um jogador com base na entrada fornecida e, se o jogador for o usuário, exibe a função atribuída.
        Este método recebe um argumento que define o papel do jogador (mafioso, doutor, xerife ou cidadão) e associa 
        essa função ao jogador. Dependendo do valor do argumento papel, a função correspondente é definida.'''


    
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
    global jogadores, jogadores_vivos
    modExplicacoes.inicio() #Dá boas vindas ao user e explicação sobre o jogo
    jogador = input("Digite seu nome antes de começarmos: ").strip().title()
    sleep(0.25)
    definir_funcoes(jogador) # Define as funções dos jogadores, recebe o jogador para falar o nome dele
    rodada = 1 # Inicia o contador de rodadas
    while jogadores_vivos > 2: # O jogo continua enquanto houver mais de 2 jogadores vivos
        sleep(0.5)
        modExplicacoes.mensagem_de_rodada(rodada)
        morto = matar() # O mafioso mata alguém durante a noite, o qual será guardado nessa variável
        if medico(morto): # O médico salvou alguém
            sleep(1)
            print("O assassino tentou matar alguém na última noite... Mas o médico trabalhou de forma certeira e salvou essa pessoa de seu terrível destino!")
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
    vencedor = definir_vencedor()
    if vencedor and jogador_venceu():
        print(f"\nParabéns {vencedor}! Você ganhou 1 ponto.")
        ranking_jogo(vencedor, 1)
    else:
        print(f"\n{jogador}, você não ganhou pontos por essa partida.")




# FUNÇÕES DE AÇÃO (Matar, investigar, médico, xerife)


def definir_funcoes(jogador: str):
    '''Função responsável por definir os papéis de cada jogador (usuário e os NPCs).
       Os papéis são: um doutor, um xerife, um mafioso e cinco cidadãos.'''
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
            alvo = random.randint(0, len(jogadores) - 1)
            if jogadores[alvo].funcao != "mafioso" and jogadores[alvo].vida == 1:
                mata = True
                jogadores[alvo].morte() # Alvo sinalizado como morto
    return alvo # Retorna o jogador que morreu




def medico(vitima: int) -> bool: 
    '''Essa função é para que o médico consiga escolher uma pessoa para proteger por noite. Caso o assassino tente matar o protegido pelo médico,
        esta pessoa não morrerá e 'reviverá' durante a noite.'''
    global jogadores
    reviveu = False
    escolha_feita = False
    medico_vivo = False
    for jogador in jogadores: # Verifica se existe um médico vivo no jogo
        if jogador.funcao == 'doutor' and jogador.vida == 1:
            medico_vivo = True
    if jogadores[0].funcao == "doutor" and medico_vivo:     # Se o usuário for o médico
        while not escolha_feita:
            try:
                escolhido_para_salvar = int(input("Digite o número do jogador que você deseja proteger nesta noite: "))
                if 0 <= escolhido_para_salvar < len(jogadores):
                    if escolhido_para_salvar == vitima:
                        jogadores[escolhido_para_salvar].revive()
                        reviveu = True
                    escolha_feita = True
                else:
                    print("Jogador inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número.")  
    elif medico_vivo:    # Se um NPC for o médico
        while not escolha_feita:
            escolha = random.randint(0, len(jogadores) - 1)
            if jogadores[escolha].vida == 1:  # Verifica se o jogador escolhido está vivo
                if escolha == vitima:
                    jogadores[escolha].revive()
                    reviveu = True
                escolha_feita = True
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
    '''Realiza a investigação do xerife, permitindo que ele identifique um jogador.
       A função verifica se o jogador que está chamando a função é o xerife e está vivo.'''
    global jogadores
    if jogadores[0].funcao == "xerife" and jogadores[0].vida == 1:
        xerife()




# FUNÇÕES AUXILIARES


def user_morto(jogador):
    '''Essa função serve para identificar quando o usuário for morto, informando que ele foi
    assassinado. Após a exibição da mensagem, o usuário é perguntado se deseja continuar
    assistindo ao jogo. Dependendo da resposta, o jogo pode ser finalizado ou continuar'''
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
        if saida in ["Não", "Nao", "N", "Ñ"]:
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
    '''Verifica se um jogador foi assassinado e atualiza o estado do jogo.'''
    global jogadores_vivos
    if morto == 0:
        if user_morto(jogadores[0].player):
            return True
        jogadores_vivos -= 1
    return False
    



def lista_jogadores_vivos() -> list[str]:
    '''Função responsável por retornar uma lista dos players vivos, que será utilizada na função de acusar.'''
    global jogadores
    players_vivos = []

    for jogador in jogadores:
        if jogador.vida == 1:
            players_vivos.append(jogador.usuario)

    return players_vivos






# FUNÇÕES DE DEBATE E ACUSAÇÕES


def debate() -> bool:
    '''Função a qual foi reduzida, mas responsável por iniciar o debate entre os jogadores
        quando está de "dia" (ou seja, quando os cidadãos estão acordados e vão tentar achar
        o assassino). Ela chama a função acusa que começa a acusação entre os jogadores.'''
    global jogadores_vivos
    sleep(2)
    print("Agora os jogadores vão debater para tentar achar o mafioso!")
    acusacao = acusa(jogadores_vivos)

    if acusacao[0] == 0:
        return True

    if acusacao[1] != -1:
        jogadores[acusacao[1]].morte()
        sleep(0.5)
        print(f"O jogador {jogadores[acusacao[1]].player} foi sentenciado a morte por seus companheiros! Ele foi eliminado.")

        if acusacao[1] == 0:
            sleep(0.5)
            print("Você foi eliminado!")
            return True # Termina pois o user foi eliminado
        
    return False




def acusa(quantidade_vivos: int) -> list[int, bool]: 
    '''Função principal responsável por fazer o debate de acusação entre os 8 jogadores.'''
    global jogadores
    players_vivos = lista_jogadores_vivos()
    print("Jogadores vivos:", players_vivos)

    if jogadores[0].vida == 0:
        resultado, quantidade_vivos = acusacao_npcs(quantidade_vivos)
    else:
        resultado, quantidade_vivos = acusacao_jogadores(quantidade_vivos)

    return [quantidade_vivos, resultado]




def acusacao_npcs(quantidade_vivos: int) -> tuple[bool, int]:
    '''Função responsável por fazer a acusação dos NPCs, que será utilizada na função de acusar.'''
    global jogadores
    while True:
        escolha = random.randint(0, len(jogadores) - 1) 
        if jogadores[escolha].vida == 1:  
            voto = random.choice([1, 2])  
            if voto == 2:
                if escolha == 0:  
                    print(f"\nOs NPCs votaram contra você, {jogadores[0].player}. Você foi eliminado!")
                    jogadores[0].morte()  
                    sleep(1)
                    if user_morto(jogadores[0].player):  
                        return True, quantidade_vivos - 1  
                    return True, quantidade_vivos - 1  

                
                print(f"O jogador {escolha} foi eliminado, mas não era o mafioso.")
                jogadores[escolha].morte()
                return True, quantidade_vivos - 1
            elif voto == 1 and jogadores[escolha].funcao == "mafioso":
                print(f"O jogador {escolha} ERA o mafioso! A cidade venceu!")
                jogadores[escolha].morte()
                return True, 0  
            else:
                print(f"O jogador {escolha} não foi eliminado. Continuem as acusações.")
                return False, quantidade_vivos



def votacao_npc(escolha: int, voto: int, quantidade_vivos: int) -> tuple[bool, int]:
    '''Essa função processa a votação dos NPCs para eliminar um jogador.
        Ela verifica o voto do NPC sobre o jogador escolhido: o voto 1 indica que e o jogador
        for o mafioso, ele será eliminado e a cidade vence o jogo; se o voto for 2 e o jogador
        NÃO for o mafioso, ele será eliminado mas aparecerá que ele não era o mafioso.'''
    global jogadores
    if voto == 2 and jogadores[escolha].funcao != "mafioso":
        sleep(1)
        print("\nVotação concluída! O jogador acusado foi eliminado. Ele não era o mafioso!")
        quantidade_vivos -= 1
        jogadores[escolha].morte()
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
        print("\nOs jogadores estão decidindo quem acusar...")
        exibir_defesa_jogador(escolha_usuario)

        voto_final = random.randint(0, 1)

        if voto_final == 1: 
            if jogadores[escolha_usuario].funcao == "mafioso":
                print(f"O jogador {escolha_usuario} ERA o mafioso! A cidade venceu!")
                jogadores[escolha_usuario].morte()
                return True, 0
            else:
                print(f"O jogador {escolha_usuario} foi eliminado, mas não era o mafioso!")
                jogadores[escolha_usuario].morte()
                return True, quantidade_vivos - 1
        else:
            print(f"\nOs outros jogadores não aceitaram sua acusação, {jogadores[0].player}.")
            nova_acusacao = random.randint(1, len(jogadores) - 1)
            while jogadores[nova_acusacao].vida == 0 or nova_acusacao == escolha_usuario:
                nova_acusacao = random.randint(1, len(jogadores) - 1)
            
            print(f"Os jogadores decidiram acusar o jogador {nova_acusacao}.")

            # Agora o novo jogador será investigado
            return False, quantidade_vivos




def escolher_acusacao_jogador() -> int:
    '''Essa função serve para que o usuário escolha alguém para acusar durante o debate (ele só
        não pode acusar a si mesmo). Verifica se o escolhido está vivo e dentro dos limites para
        fazer a acusação.'''
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

    if escolha_usuario == 0:
        defesa_usuario = input(f"{jogadores[0].player}, você pode tentar se defender para se salvar. Digite sua defesa: ") 
        print(f"{jogadores[0].player} está tentando se defender!")
   
    else:
        exibir_defesa_jogador(escolha_usuario)

    voto_final = random.randint(0, 1)
    
    if voto_final == 1 and jogadores[escolha_usuario].funcao != "mafioso":
        print(f"O {jogadores[escolha_usuario].usuario} não era o mafioso! Boa sorte na próxima votação.")
        jogadores[escolha_usuario].morte()
        return True, quantidade_vivos - 1
    
    elif voto_final == 1 and jogadores[escolha_usuario].funcao == "mafioso":
        print(f"O {jogadores[escolha_usuario].usuario} ERA o mafioso! A CIDADE VENCEU!")
        jogadores[escolha_usuario].morte()
        return True, 0
    
    else:
        print(f"\nVotação concluída! O {jogadores[escolha_usuario].usuario} não foi eliminado.")
        return False, quantidade_vivos



def exibir_defesa_jogador(escolha_usuario: int):
    '''Essa função serve para que, quando o acusado for um NPC, ele se defenda utilizando
        a lista de defesas de forma aleatória, que será impressa para o usuário.'''
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



def escolher_acusacao_npc(ja_acusado: int) -> int:
    '''Função responsável por definir quem será o player acusado de forma aleatória. Será utilizada na função de acusar.'''
    global jogadores
    acusacao = False

    while not acusacao:
        escolha = random.randint(0, len(jogadores) - 1)

        if escolha < len(jogadores) and jogadores[escolha].vida == 1 and escolha != ja_acusado:
            acusacao = True
            print(f"\nOs jogadores decidiram acusar o player {escolha}. Hora da votação!")

    return escolha




# SISTEMA DE RANKEAMENTO DOS JOGADORES UTILIZANDO DE BASE A ATIVIDADE PASSADA EM SALA DE AULA

def definir_vencedor() -> str:
    """Função para definir o vencedor no final do jogo"""
    for jogador in jogadores:
        if jogador.vida == 1:
            return jogador.player
    return ""



def jogador_venceu() -> bool:
    """Verifica se o jogador venceu o jogo"""
    global jogadores

    if jogadores[0].funcao == "mafioso":
        return jogadores[0].vida == 1 and jogadores_vivos == 1
    
    else:
        for jogador in jogadores:
            if jogador.funcao == "mafioso" and jogador.vida == 0:
                return True
            
    return False



def ler_dados(arquivo: str) -> list:
    """Lê o arquivo de ranking e retorna uma lista de dados"""
    with open(arquivo, 'a+', encoding='UTF-8') as arq:
        arq.seek(0)  
        return arq.readlines()
        


def salvar_dados(data: list, arquivo: str) -> None:
    """Salva os dados no arquivo"""
    with open(arquivo, 'w', encoding='UTF-8') as arq:
        for line in data:
            arq.write(line)



def exibir_ranking() -> None:
    """Exibe o ranking de jogadores"""
    ranking = ler_dados('ranking.txt')
    if not ranking:
        print("Nenhum dado no ranking ainda.")
        return

    print("\nRanking de Jogadores:")
    for user in ranking:
        nome, pontos = user.replace('\n', '').split(';')
        print(f'{nome} - {pontos} pontos')

 

def atualizar_ranking(nome: str, pontos: int) -> None:
    """Atualiza o ranking com a pontuação do jogador"""
    ranking = ler_dados('ranking.txt')

    atualizado = False
    for i in range(len(ranking)): # Se o jogador já estiver no ranking
        jogador, pontuacao_atual = ranking[i].replace('\n', '').split(';')
        if jogador == nome:
            nova_pontuacao = int(pontuacao_atual) + pontos
            ranking[i] = f'{jogador};{nova_pontuacao}\n'
            atualizado = True
            break
    
    if not atualizado: # Se não estiver, vai adicionar
        ranking.append(f'{nome};{pontos}\n')

    # Rankeando por pontos de forma decrescente
    ranking.sort(key=lambda item: int(item.split(';')[-1]), reverse=True)

    # Ranking atualizado
    salvar_dados(ranking, 'ranking.txt')



 
def ranking_jogo(vencedor: str, pontos: int) -> None:
    """Função chamada ao final do jogo para atualizar o ranking"""
    print(f"\nParabéns {vencedor}! Você ganhou {pontos} pontos.")
    atualizar_ranking(vencedor, pontos)

    # Exibe o ranking atualizado
    exibir_ranking()




# Chama a função principal para iniciar o jogo

if __name__ == "__main__":
    jogar()

    '''Verifica se o script está sendo executado diretamente.
    Esta condição é usada para determinar se o arquivo python 
    está sendo executado como o programa principal. Se for o caso, 
    a função 'jogar()' é chamada, dando início ao jogo. '''
