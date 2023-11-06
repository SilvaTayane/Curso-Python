import json
def exibir_tabela_carros(carros):
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
    x= carregar_carros()
    print(exibir_tabela_carros(x)) 
    op = input('Escolha a caegoria do carro:')
    dias = int(input('Quantidade de dias de aluguel:'))
    forma_pgto = input('Forma de pagamento:\n(1) Crédito\n(2) Débito\n(3) Pix')
def alugar_carro(x):
def atualizar_carro(x):
    
