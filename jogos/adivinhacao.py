print('********************************')
print('Bem vindo ao jogo de Advinhação!')
print('********************************')

numero_secreto = 36

chute_str = input('Digite um numero: ')

print('Você digitou o número', chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if (acertou):
    print('PARABÉNS!!! VOCÊ ACERTOU!')
else:
    if (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto.")

print('FIM DO JOGO')

