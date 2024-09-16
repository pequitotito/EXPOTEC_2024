

from time import sleep


def inicio():
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
    explicacao = input("Gostaria de uma explicação antes de iniciar o jogo?\nResponda com 'Sim' ou 'Não': ").strip().lower()
    if explicacao == 'sim' or explicacao == 's':
        return explicacao()
    else:
        sleep(0.25)    
        print("Já que você não precisa de mais explicações... Vamos ao jogo!")

def explicacao():
    sleep(0.25), print("\nHá nesta cidade um terrível assassino... Ele busca assassinar todos os jogadores a sangue frio\n",
                       "e causar discórdia entre os moradores da cidade.")
    
    sleep(0.5), print("Há um narrador que dará informações durante todo o jogo. Logo no início são distribuídos papéis entre\n",
                      "os jogadores. Eles podem ser:\n- Mafioso/Assassino\n- Médico\n- Xerife\n- Cidadão")
    
    sleep(0.5), print("Após a distribuição dos papéis o jogo começa...\n\n")

    sleep(0.5), print("Existem três papéis que podem agir durante a noite: o assassino, o médico e o xerife.\nO assassino escolherá",
                     "alguém para eliminar durante a noite. Após ele, o médico age para proteger alguém durante a noite.")
    
    sleep(0.5), print("Caso o protegido do médico coincida com a pessoa que o mafioso tentou assassinar durante a noite, esta pessoa continuará sã e salva.\n")
    sleep(0.5), print("O xerife age depois investigando quem ele acha que é o assassino.\nO narrador dirá se ele está certo ou não...")
    sleep(0.5), print("O narrador ditará quando a cidade amanhecer. Quando isso ocorrer, todas os cidadãos se reunirão para tentar achar o assassino.",
                      "\nPara isso, ocorrerá uma discussão e posteriormente uma votação para eliminar alguém. \n")
    sleep(0.5), print("O acusado pode tentar se defender e após a sua defesa, os jogadores decidem se ele é culpado ou não.")
    sleep(0.5), print("Caso decidam eliminá-lo e ele for o assassino, o jogo termina com vitória da Cidade!")
    sleep(0.5), print("Caso decidam eliminá-lo e ele não for o assassino... Mais uma noite chega e o assassino irá agir.")
    sleep(0.5), print("Se não decidirem eliminar o jogador, mais uma discussão ocorre até que alguém seja escolhido para morrer.\n")
    sleep(0.5), print("O jogo termina com a vitória da Cidade ou do Mafioso! Boa sorte e bom jogo!!\n")
