import forca
import advinhacao

def escolhe_jogo():

    print("*********************************")
    print("***   Escolha o seu jogo      ***")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        advinhacao.jogar_adivinhacao()

if (__name__ == "__main__"):
    escolhe_jogo()