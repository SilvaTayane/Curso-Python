from random import randint

computador = randint(0,5) #Faz o sorteio dos números entre 0 e 5
print('-=-' * 15)
print("Vou pensar em numero entre 0 e 5. Tente adivinhar...")
print('-=-' * 15)
jogador = int(input("Em que numero pensei: ")) #Jogador tenta adivinhar qual é o número
if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no numero {} e não no {}!".format(computador , jogador))
