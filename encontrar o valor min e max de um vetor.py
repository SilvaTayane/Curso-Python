import math
def maxvet(vet):
    maior = float('-inf')
    for numero in vet:
        if numero > maior:
            maior=numero
    return maior
def minvet(vet):
    menor= float('+inf')
    for numero in vet:
        if numero < menor:
            menor = numero
    return menor

vet=[2,3,5,100,10,82]
print('O número maior é:',maxvet(vet))
print('O menor número é:', minvet(vet))
