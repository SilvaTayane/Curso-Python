import json
import os

def exibir_tabela_carros(carros):
    os.system("cls")
    print("================================ LOCADORA DE VEICULOS ================================")
    print("{:<10} {:<10} {:<15} {:<10} {:<10} {:<15} {:<10}".format("Categoria", "Marca", "Modelo", "Ano", "Cor", "Preço/Dia", "Disponível"))
    for categoria, carros_categoria in carros.items():
        for carro in carros_categoria:
            print("{:<10} {:<10} {:<15} {:<10} {:<10} R${:<14.2f} {:<10}".format(categoria, carro["marca"], carro["modelo"], carro["ano"], carro["cor"], carro["preco_por_dia"],carro["disponivel"]))

def carregar_carros():
    with open('carros.json','r') as f:
        texto = f.read()
        abrir_carros = json.loads(texto)
    return abrir_carros

def menu():
    carros= carregar_carros()
    while True:
        print(exibir_tabela_carros(carros)) 
        op = input('\n(1) Locar veiculo\n(2) Devolver veiculo\n:')
        
        if(op=='1'):
            alugar_carro(carros)
        elif(op=='2'):
            devolver_carro(carros)
def alugar_carro(carros):
    dias = int(input('Quantidade de dias de aluguel:'))
    forma_pgto = input('Forma de pagamento:\n(1) Crédito\n(2) Débito\n(3) Pix')

def devolver_carro(carros):

if __name__=='__main__':
    menu()
