import random


def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    print("Qual o nível de dificuldade?")

    nivel = int(input("(1) Fácil; (2) Médio; (3) Difícil: "))
    total_tentativas = (4 - nivel) * 5  # o total de tentativas será 5, 10 ou 15, de acordo com o nível escolhido
    pontos = 1000

    if nivel == 1:
        total_tentativas = 15
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    numero_secreto = random.randint(1, 100)
    # print(f"N° secreto: {numero_secreto}")

    for tentativa in range(1, total_tentativas + 1):
        print("")
        print(f"Tentativa {tentativa} de {total_tentativas}...")
        chute = int(input("Digite o seu palpite (entre 1 e 100): "))

        if (chute < 1 or chute > 100):
            print("O palpite deve ser um número entre 1 e 100")
            continue

        print("Você digitiou", chute)

        if (chute == numero_secreto):
            print("Você acertou!")
            break
        elif(chute > numero_secreto):
            print("Você errou... O seu palpite foi maior que o número secreto")
        else:
            print('Você errou... O seu palpite foi menor que o número secreto')

        pontos -= abs(numero_secreto - chute)

    print("")
    print(f"Fim do Jogo! O número secreto era {numero_secreto} e você fez {pontos} pontos")


if (__name__ == "__main__"):
    jogar()
