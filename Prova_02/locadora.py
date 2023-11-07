import json
import os


def exibir_tabela_carros(carros):
    os.system("cls")
    print("================================ LOCADORA DE VEICULOS ================================")
    print("{:<10} {:<10} {:<15} {:<10} {:<10} {:<15} {:<10}".format("Categoria", "Marca", "Modelo", "Ano", "Cor", "Preço/Dia", "Disponível"))
    for categoria, carros_categoria in carros.items():
        for carro in carros_categoria:
            print("{:<10} {:<10} {:<15} {:<10} {:<10} R${:<14.2f} {:<10}".format(categoria, carro["marca"], carro["modelo"], carro["ano"], carro["cor"], carro["preco_por_dia"],carro["disponivel"]))



def carregar_arquivo_carros():
    with open('carros.json','r') as f:
        texto = f.read()
        abrir_carros = json.loads(texto)
    return abrir_carros


def menu():
    carros= carregar_arquivo_carros()
    while True:
        print(exibir_tabela_carros(carros)) 
        op = input('\n(1) Locação de Veículos\n(2) Visualizar lista de clientes\n:')
        
        if(op=='1'):
            alugar_carro(carros)
        elif(op=='2'):
            lista_de_clientes(carros)

            
def alugar_carro(carros):
    op = input("(1) Alugar veículo\n(2) Devolver um veículo alugado\n")
    if op == '1':
        #Cadastrar usuario a alugar carro
    elif op == '2':
        #devolver carro alugado pelo cliente


def lista_de_clientes(carros):
    #imprimir lista de clientes


if __name__=='__main__':
    menu()
