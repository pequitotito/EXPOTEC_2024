
import os
import random
from time import sleep


def inicio() -> None:
    '''Exibe a tela de início do jogo Máfia e introduz o jogador.
    A função pergunta ao jogador se ele deseja receber uma explicação sobre as regras do jogo. 
    Se o jogador optar por uma explicação, a função dar_explicacao é chamada. 
    Caso contrário, a função informa que o jogo começará sem mais explicações.'''

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
    sleep(0.25)
    print("\nBem-vindo ao jogo Máfia! 🕵  🔪 🩸") 
    sleep(0.25)
    quer_explicacao = input("Gostaria de uma explicação antes de iniciar o jogo?\nResponda com 'Sim' ou 'Não': ").strip().lower()
    if quer_explicacao in ['s', 'sim']:
        dar_explicacao()
    else:
        sleep(0.25)    
        print("\nJá que você não precisa de mais explicações... Vamos ao jogo!")

def dar_explicacao() -> None:
    '''Função com uma lista de mensagens que serão exibidas caso o usuário deseje uma explicação sobre o jogo.'''
    mensagens = [
        "\nHá nesta cidade um terrível assassino... Ele busca assassinar todos os jogadores a sangue frio\ne causar discórdia entre os moradores da cidade\n",
        "Há um narrador que dará informações durante todo o jogo. Logo no início sçao distribuídos papéis entre os jogadores.\nOs papéis são:\nMafioso\nMédico\nXerife\nCidadão\n\n",
        "Após a distribuição dos papéis o jogo começa...\n\n",
        "Existem três papéis que podem agir durante a noite: o assassino, o médico e o xerife.\nO assassino escolherá alguém para eliminar durante a noite. Após ele, o médico age para proteger alguém durante a noite.\n",
        "Caso o protegido do médico coincida com a pessoa que o mafioso tentou assassinar durante a noite, esta pessoa continuará sã e salva.\n",
        "O xerife age depois investigando quem ele acha que é o assassino.\nO narrador dirá se ele está certo ou não...\n",
        "O narrador ditará quando a cidade amanhecer. Quando isso ocorrer, todas os cidadãos se reunirão para tentar achar o assassino.\nPara isso, ocorrerá uma discussão e posteriormente uma votação para eliminar alguém. \n",
        "O acusado pode tentar se defender e após a sua defesa, os jogadores decidem se ele é culpado ou não.\n",
        "Caso decidam eliminá-lo e ele for o assassino, o jogo termina com vitória da Cidade!\n",
        "Caso decidam eliminá-lo e ele não for o assassino... Mais uma noite chega e o assassino irá agir.\n",
        "Se não decidirem eliminar o jogador, mais uma discussão ocorre até que alguém seja escolhido para morrer.\n",
        "O jogo termina com a vitória da Cidade ou do Mafioso! Boa sorte e bom jogo!!\n"
    ]
    for msg in mensagens:
        sleep(1.5)
        print(msg)
            
    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    
def mensagem_fim_de_jogo(vitoria: bool) -> None:
    '''Caso seja vitória da Cidade, exibe que foi vitória dos jogadores. Caso seja vitória do mafioso, 
        foi derrota dos jogadores.'''
    print("\n" + "*" * 50)
    
    if vitoria:
        print("\n" + " " * 10 + "PARABÉNS! VOCÊ VENCEU!!!".center(25))
    else:
        print("\n" + " " * 10 + "VOCÊ PERDEU. TENTE NOVAMENTE!".center(25))
    
    print("\n" + "*" * 50 + "\n")




def mensagem_de_rodada(rodada: int) -> None:
    '''Função feita apenas para exibir na tela a mensagem de qual rodada está começando.
       Feita para dividir a função principal 'jogar' em várias subfunções.'''
    print("\n" + "=" * 50)
    print(f"::: Início da Rodada {rodada} :::".center(25))
    print("=" * 50 + "\n")




def mensagem_morte_npc(morto: int) -> None:
    """Exibe uma mensagem aleatória sobre a morte de um NPC."""
    frases_morte = [
        f"\nNesta última madrugada, o Jogador {morto} foi assassinado no local de trabalho.",
        f"\nNa noite passada, o Jogador {morto} foi encontrado morto dentro de sua casa.",
        f"\nNesta noite, o assassino matou o Jogador {morto}."
    ]
    print(random.choice(frases_morte))
    
