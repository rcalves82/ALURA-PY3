#coding: utf-8

print('********************************')
print('Bem vindo ao jogo de Advinhação!')
print('********************************')

numero_secreto = 36
total_de_tentativas = 3

for rodada  in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input('Digite um numero entre 1 e 100: ')
    print('Você digitou o número', chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Por favor! Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print('PARABÉNS!!! VOCÊ ACERTOU!')
        break

    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")


print('FIM DO JOGO')

