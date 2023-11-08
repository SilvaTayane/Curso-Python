import json
import os
import datetime


def exibir_tabela_carros(carros):
    print("================================ LOCADORA DE VEÍCULOS ================================")
    print("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format("Código", "Marca", "Modelo", "Ano", "Cor", "Preço/Dia", "Disponível", "Placa"))
    for codigo, lista in carros.items():
        print(f"{codigo:<15}{lista[0]:<15}{lista[1]:<15}{lista[2]:<15}{lista[3]:<15}{lista[4]:<15}{lista[5]:<15}{lista[6]:<15}")




def carregar_arquivo_carros():
    with open('carros.json', 'r') as f:
        texto = f.read()
        abrir_carros = json.loads(texto)
    return abrir_carros




def carregar_arquivo_pessoas_cadastradas():
    with open('pessoas_cadastradas.json', 'r') as f:
        texto = f.read()
        pessoas_cadastradas = json.loads(texto)
    return pessoas_cadastradas




def escrever_json_carros(carros):
     with open('carros.json', 'w') as f:
            f.write(json.dumps(carros))






def escrever_json_pessoas_cadastradas(pessoas_cadastradas):
     with open('pessoas_cadastradas.json', 'w') as f:
            f.write(json.dumps(pessoas_cadastradas))






def reservar_carro(carros):
    tipo_carro = input('Qual modelo de carro:')
    dias = int(input('Quantidade de dias de aluguel:'))
    op_2 = input('\n(1) Confirmar contrato\n(2) Mudar o veiculo\n(3) Encerrar\n')

    if (op_2 == '1'):
        pessoas_cadastradas = alugar_carro(carros,  tipo_carro, dias)
        return pessoas_cadastradas
    elif (op_2 == '2'):
        reservar_carro(carros)
    elif (op_2 == '3'):
        return None






def alugar_carro(carros, codigo, dias):
    nome_completo = input('Nome completo:')
    idade = int(input('Idade:'))
    if idade < 18:
        alugar_carro(carros, codigo, dias)
    if idade < 25:
        conta = (dias * carros[codigo][4]) + 30
    else:
        conta = dias * carros[codigo][4]
    cnh = int(input('CNH:'))
    if cnh < 11:
        while cnh < 11:
            cnh = input('CNH:')
    cpf = input('CPF:')
    if len(cpf) < 11:
        while cpf < 11:
            cpf = int(input('CPF:'))
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=dias)
    data = now + delta
    formato = '%d/%m/%Y'
    data_entrega = data.strftime(formato)
    print('================================ CONTRATO DE LOCAÇÃO ================================\n')
    print('{} portador do CPF {} e da CNH {} está alugando o veiculo {}'.format(nome_completo, cpf, cnh, carros[codigo][0]))
    print('no periodo de {} dias ,que ficará no valor de R${}'.format(dias, conta))
    print('e devolução do veiculo ficará para a data {}.'.format(data_entrega))
    print('-----ATENCAO: EM CASO DE ATRASO HAVERA COBRANÇA DE TAXA DE 100R$ AO DIA-----')
    print('Locação com sucesso!\n')
    print('================================================================\n\n')

    carros[codigo][5]-=1
    escrever_json_carros(carros)

    pessoas_cadastradas = escrever_retornar_pessoa(nome_completo,idade, cpf, cnh, codigo,dias, conta,data_entrega)
    return pessoas_cadastradas









def escrever_retornar_pessoa(nome,idade, cpf, cnh, tipo_carro,dias, conta,data_entrega):

    pessoas_cadastradas = {}

    while True:
        if os.path.exists('pessoas_cadastradas.json'):
            with open('pessoas_cadastradas.json', 'r') as f:
                texto = f.read()
                pessoas_cadastradas = json.loads(texto)

        pessoas_cadastradas[cpf] = [nome, idade, dias, conta, tipo_carro, cnh, conta,data_entrega]
        with open('pessoas_cadastradas.json', 'w') as f:
            f.write(json.dumps(pessoas_cadastradas))
        return pessoas_cadastradas







def devolver_carro(carros,pessoas_cadastradas):
    cpf_pessoa = input('Digite seu CPF: ')
    dia_entregue = input('Dia de entrega (dd/mm/YYYY): ')
    
    print(type(dia_entregue))
    print(type(pessoas_cadastradas[cpf_pessoa][7]))


    if dia_entregue != pessoas_cadastradas[cpf_pessoa][7]:

        dia_entregue = datetime.datetime.strptime(dia_entregue, '%d/%m/%Y')
        data_entregue = datetime.datetime.strptime(pessoas_cadastradas[cpf_pessoa][7], '%d/%m/%Y')
        
        atraso = dia_entregue - data_entregue
        valor = atraso.days*100 
        print('Pague uma multa: ', valor)

    if cpf_pessoa in pessoas_cadastradas.keys():
        
        carros[pessoas_cadastradas[cpf_pessoa][4]][5]+=1
        del pessoas_cadastradas[cpf_pessoa]       
    
        escrever_json_carros(carros)
        escrever_json_pessoas_cadastradas(pessoas_cadastradas)

        print('Devolvido com sucesso')





def menu():
    carros = carregar_arquivo_carros()
    while True:
        exibir_tabela_carros(carros)
        op = input(
            '\n(1) Reservar veiculo\n(2) Devolver veiculo\n(3) Finalizar\n')

        if (op == '1'):
            pessoas_cadastradas = reservar_carro(carros)
        elif (op == '2'):
            pessoas_cadastradas = carregar_arquivo_pessoas_cadastradas()
            devolver_carro(carros,pessoas_cadastradas)
        elif (op == '3'):
            break




if __name__ == '__main__':
    menu()
