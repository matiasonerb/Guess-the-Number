import random

def adivinhe():
    print("Seja Bem-vindo ao jogo 'Adivinhe o Número'!")
    print("Estou pensando em um número entre 1 a 100. Tente adivinhar!")

    n_secreto = random.randint(1, 100)
    tentativas = 0
    while True:
        tentativa = input("Digite o seu palpite: ")

        if tentativa.isdigit():
            tentativa = int(tentativa)
            tentativas += 1

            if tentativa < n_secreto:
                print("Muito baixo! Tente novamente.")
            elif tentativa > n_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você adivinhou o número {n_secreto} em {tentativas} tentativas.")
                break
        else:
            print("Número inválido.")

adivinhe()