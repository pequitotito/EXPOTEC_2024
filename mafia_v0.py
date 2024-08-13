from time import sleep
import random

def selecionar_papeis(jogadores, papel=["m", "x", "d", "c", "c"]):
    dic = {}

    for jogador in jogadores:
        func = random.choice(papel)
        papel.remove(func)
        dic[jogador] = func
    

    return dic

def jogar():
    # O jogo inicia, explicação de como funciona o jogo e as funções (xerife, doutor, assassino e cidadãos)
    print("Bem-vindo ao jogo Cidade Dorme! 🕵  🔪 🩸")
    print("")
    jogador = input("Digite seu nome antes de começarmos: ").strip().title()
    sleep(0.25)


    explicacao = input(f"{jogador}, você quer uma explicação breve sobre o jogo antes de jogar? (Responda com 'Sim' ou 'Não'): ").strip().capitalize()
    
    if explicacao == 'Sim':
        sleep(1)
        print("\n")
        print("Existe um narrador que dará informações durante o jogo inteiro e são distribuídos papéis para cada participante.")
        sleep(1)
    
        print("Esses papéis são as funções que cada jogador pode receber. São elas:")
        sleep(1)
        
        print("\n")
        print("- Cidadão")
        print("- Mafioso")
        print("- Doutor")
        print("- Xerife")
        sleep(1)
        print("\n")
        
        print("Após esses papéis serem distribuídos entre os jogadores, o jogo começa.")
        sleep(2)
        
        print("Durante a noite, todos os jogadores estão dormindo e o mafioso escolhe matar um participante.")
        sleep(2)
        
        print("Logo após, o doutor age para tentar salvar um participante (se a pessoa escolhida for a mesma que o mafioso tentou matar, essa pessoa continuará viva).")
        sleep(2)
        
        print("O xerife age depois do doutor escolhendo alguém que ele acha que é o mafioso, e o narrador responderá se ele está certo ou não.")
        sleep(2)
        
        print("Quando o narrador fala para a cidade acordar, todos os jogadores voltam a agir. O narrador deve anunciar quem morreu durante a noite")
        sleep(2)
        
        print("Caso ninguém tenha morrido, revela que alguém foi salvo pelo doutor durante a noite.")
        sleep(2)
        
        print("TODOS os jogadores discutem entre si para tentar achar o assassino e fazem uma votação para matá-lo.")
        sleep(2)
        
        print("O acusado pode tentar se defender e depois de sua breve defesa, os jogadores decidem se querem eliminá-lo ou não.")
        sleep(2)
        
        print("Caso eliminem, o narrador revela se ele era o mafioso. Se for o assassino, os cidadãos vencem (vitória da Cidade).")
        sleep(2)
        
        print("Se não for, a noite cai e o jogo continua se repetindo. ")
        sleep(2)

        print("Caso sobre apenas o mafioso ou ele e mais um cidadão, o jogo termina com a vitória da Máfia.")

        print("\n")
        print("Agora... Vamos ao que interessa!")
        sleep(1)

    else:
        print("OK! Então vamos começar!")
        print("")
        sleep(0.5)

    jogadores = [jogador, 1, 2, 3, 4]
    print(selecionar_papeis(jogadores))





if __name__ == "__main__":
    jogar()


#EMOJIS UTILIZADOS: 🤠  🔫
