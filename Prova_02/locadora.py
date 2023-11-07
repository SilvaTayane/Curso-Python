import json
import os

#Imprimir tabela de carros
def exibir_tabela_carros(carros):
    os.system("cls")
    print("================================ LOCADORA DE VEICULOS ================================")
    print(f"{'Código':<10}{'Produto':<25}{'Preço':<15}{'Estoque':<15}{'Vendas':<15}")
        for codigo, lista in estoque.items():
            print(f"{codigo:<10}{lista[0]:<25}{lista[1]:<15}{lista[2]:<15}{lista[3]:<15}")
 
   
#Carregar arquivo carros
def carregar_arquivo_carros():
    with open('carros.json','r') as f:
        texto = f.read()
        abrir_carros = json.loads(texto)
    return abrir_carros

def reservar_carro(carros):
    #Parte do João Vitor#
    # remover 1 da quantidade de veiculos disponivel
    tipo_carro = input('Qual modelo de carro:')
    dias = int(input('Quantidade de dias de aluguel:'))
    op_2 = input('\n(1) Confirmar contrato\n(2) Mudar o veiculo\n(3) Encerrar\n')
    if tipo_carro in carros.keys():
        
    if(op_2=='1'):
            alugar_carro(carros,  tipo_carro, dias)
    elif(op_2=='2'):
        reservar_carro(carros)
    elif(op_2=='3'):
        return None

    

def alugar_carro(carros, tipo_carro, dias):
    nome = input('Nome:')
    idade = int(input('Idade:'))
    if idade < 25:
        conta = dias * carros[tipo_carro][4] + 30
    else:
        conta = dias * carros[tipo_carro][4]
    cpf = int(input('CPF:'))
    while cpf < 11 :
        cpf = int(input('CPF:'))  
    
    print('======CONTRATO DE LOCAÇÃO======\n')
    print('{} portador do CPF {} está alugando o veiculo {} \nno periodo de {} dias , que ficará no valor de R${}'.format(nome, cpf, tipo_carro, dias, conta))




#Menu
def menu():
    carros= carregar_carros()
    while True:
        print(exibir_tabela_carros(carros)) 
        op = input('\n(1) Reservar veiculo\n(2) Devolver veiculo\n:')
        
        if(op=='1'):
            reservar_carro(carros)
        elif(op=='2'):
            devolver_carro(carros)

        


if __name__=='__main__':
    menu()
