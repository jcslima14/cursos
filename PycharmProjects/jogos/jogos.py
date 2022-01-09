import forca
import adivinhacao

print("********************************")
print("Bem vindo ao console de jogos Py")
print("********************************")

print("Temos estes jogos:")
print("(1) Adivinhação")
print("(2) Forca)")
print("")
opcao = int(input("Digite o número do jogo que deseja jogar: "))

if opcao == 1:
    adivinhacao.jogar()
else:
    forca.jogar()

print("")
print("Fim do Jogo!")
