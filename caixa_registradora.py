'''

Caixa registradora /// Prova 01

'''
import os
os.system("cls")
totalMoney=0
quantidade=0
while(True):
    op = input("==== Menu de Compras ====\n[1] - Pipoca doce 400g (R$ 4,00)\n[2] - Sardinha 1kg (R$ 10,00)\n[3] - KitKat 180g (R$ 2.00)\n[S] - Sair\n")
    
    

    if(op=='1'):
        quantidade = int(input("Quantidade:"))
        totalMoney+=4*quantidade
    elif(op=='2'):
        quantidade = int(input("Quantidade:"))
        totalMoney+=10*quantidade
    elif(op=='3'):
        quantidade = int(input("Quantidade:"))
        totalMoney+=2*quantidade
    elif(op=='S'):
        break
    else:
        print("Código invalido!\n")
        

print("\nTotal da compra:R$",totalMoney)
