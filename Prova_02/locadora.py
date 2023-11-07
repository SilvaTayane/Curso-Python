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



def alugar_carro(carros):
    op = input("(1) Alugar veículo\n(2) Devolver um veículo alugado\n")
    if op == '1':
        #Cadastrar usuario a alugar carro
    elif op == '2':
        #devolver carro alugado pelo cliente



#imprimir lista de clientes
def lista_de_clientes(carros):



#Menu
def menu():
    carros= carregar_arquivo_carros()
    while True:
        print(exibir_tabela_carros(carros)) 
        op = input('\n(1) Locação de Veículos\n(2) Visualizar lista de clientes\n:')
        
        if(op=='1'):
            alugar_carro(carros)
        elif(op=='2'):
            lista_de_clientes(carros)

        


if __name__=='__main__':
    menu()
