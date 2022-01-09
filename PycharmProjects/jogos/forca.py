import random


def marca_chute_correto(palavra_exibida, palavra_secreta, chute):
    indice = 0
    for letra in palavra_secreta:
        if (letra == chute):
            palavra_exibida[indice] = chute

        indice += 1


def jogar():

    imprime_mensagem_abertura("Seja muito bem vindo ao jogo de Forca")

    palavra_secreta = obter_palavra_secreta()

    palavra_exibida = ["_"] * len(palavra_secreta)
    tentativas = 7
    erros = 0
    enforcou = False
    acertou = False

    print(f"A palavra agora é: {' '.join(palavra_exibida)}")

    while (not enforcou and not acertou):
        chute = input("Digite uma letra: ").lower().strip()

        if (chute in palavra_secreta):
            marca_chute_correto(palavra_exibida, palavra_secreta, chute)
            print(f"Você acertou o chute! {' '.join(palavra_exibida)}")
        else:
            erros += 1
            desenha_forca(erros)

        acertou = (palavra_secreta == "".join(palavra_exibida))
        enforcou = (erros == tentativas)

    if (acertou):
        print(f"Parabéns! Você acertou a palavra secreta e só errou {erros} vezes.")
    else:
        print("Que pena... você não conseguiu acertar a palavra secreta. Tente outras vezes!")

    print("")
    print(f"Fim do jogo de forca!")


def imprime_mensagem_abertura(mensagem):
    print("*" * (len(mensagem) + 8))
    print(f"{'*' * 3} {mensagem} {'*' * 3}")
    print("*" * (len(mensagem) + 8))


def obter_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = [palavra.strip().lower() for palavra in arquivo]

    return palavras[random.randint(0, len(palavras) - 1)]


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \\     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \\|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar()
