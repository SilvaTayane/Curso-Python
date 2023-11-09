import json  # importando a biblioteca JSON pois Ele usa uma sintaxe leve e minimalista, tornando-o rápido de ser processado
import os  # esta biblioteca nos fornece uma maneira fácil de obter informações do sistema operacional com apenas uma linha de código.
import datetime  # utilizado para ter uma forma rapida e simples de acessar datas dentre outros


def exibir_tabela_carros(carros):
    '''Função para exibir a tabela de seleção dos veiculos'''

    print(" ".center(50), "LOCADORA DE VEÍCULOS\n")
    print("Código".ljust(14) , "Marca".ljust(14) , "Modelo".ljust(14) , "Ano".ljust(14)  , "Cor".ljust(14) , "Preço/Dia".ljust(14) , "Disponível".ljust(14) , "Placa" )

    for codigo, lista in carros.items(): #loop para que exiba uma tabela de informação dos veiculos disponivel.
        print(f"{codigo}".ljust(14), f"{lista[0]}".ljust(14), f"{lista[1]}".ljust(14), f"{lista[2]}".ljust(14), f"{lista[3]}".ljust(14), f"{lista[4]}".ljust(14), f"{lista[5]}".ljust(14), f"{lista[6]:<15}") #exibe as informações do arquivo carros.Json em um formato tabelado




def carregar_arquivo_carros():
    '''Função utilizada para abrir o arquivo Json no codigo e utilizar no corpo do codigo'''

    with open('carros.json', 'r') as f:
        texto = f.read()
        abrir_carros = json.loads(texto)
    return abrir_carros


def carregar_arquivo_pessoas_cadastradas():
    '''Função utilizada para carregar o arquivo json de pessoas cadastradas
    para ser utilizado na devolução do carro'''

    with open('pessoas_cadastradas.json', 'r') as f:
        texto = f.read()
        pessoas_cadastradas = json.loads(texto)
    return pessoas_cadastradas #pessoas_cadastradas é uma lista dentro do arquivo json e
                                # sera usada para adicionar pessoa ao nosso "banco de dados"


def escrever_json_carros(carros):
    '''Função para adicionar um carro como disponivel no estoque quando ele for devolvido.
     uma outra forma de explicar é para Reescrever/atualizar o arquivo "carros.json", abrindo no modo write
    podendo escrever ou retirar informações.'''

    with open('carros.json', 'w') as f:
        f.write(json.dumps(carros)) #o arquivo carros é um arquivo.json que tem uma lista dentro
                                    #que adiciona ou remove carros do nosso banco de dados


def escrever_json_pessoas_cadastradas(pessoas_cadastradas):
    '''Função para Reescrever/atualizar o arquivo "pessoas_cadastradas" abrindo o 
    arquivo no modo "write" podendo escrever ou retirar informações. '''

    with open('pessoas_cadastradas.json', 'w') as f:
        f.write(json.dumps(pessoas_cadastradas))


def reservar_carro(carros):
    '''função para utilizar quando a pessoa for alugar que ja foi
     reservado anteriormente recebendo qual modelo de carro e
    quantos dias a pessoa vai ficar com o carro,
    reservar um carro pelo codigo.
    ou retornar ao inicio'''

    codigo = input('Qual o código do carro:')
    dias = int(input('Quantidade de dias de aluguel:'))
    OpcaoDois = input('\n(1) Confirmar contrato'
                 '\n(2) Mudar o veiculo'
                 '\n(3) Encerrar\n')

    if (OpcaoDois == '1'):
        pessoas_cadastradas = alugar_carro(carros, codigo, dias)
        return pessoas_cadastradas
    elif (OpcaoDois == '2'):
        reservar_carro(carros)
    elif (OpcaoDois == '3'):
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
    print(''.center(55), 'CONTRATO DE LOCAÇÃO\n')
    print('{} portador do CPF {} e da CNH {} está alugando o veiculo {}'.format(nome_completo, cpf, cnh,
                                                                                carros[codigo][0]))
    print('no periodo de {} dias ,que ficará no valor de R${}'.format(dias, conta))
    print('e devolução do veiculo ficará para a data {}.'.format(data_entrega))
    print('-----ATENCAO: EM CASO DE ATRASO HAVERA COBRANÇA DE TAXA DE 100R$ AO DIA-----')
    print('Locação com sucesso!\n')
    print('================================================================\n\n')

    carros[codigo][5] -= 1
    escrever_json_carros(carros)

    pessoas_cadastradas = escrever_retornar_pessoa(nome_completo, idade, cpf, cnh, codigo, dias, conta, data_entrega)
    return pessoas_cadastradas


def escrever_retornar_pessoa(nome, idade, cpf, cnh, codigo, dias, conta, data_entrega):
    pessoas_cadastradas = {}

    while True:
        if os.path.exists('pessoas_cadastradas.json'):
            with open('pessoas_cadastradas.json', 'r') as f:
                texto = f.read()
                pessoas_cadastradas = json.loads(texto)

        pessoas_cadastradas[cpf] = [nome, idade, dias, conta, codigo, cnh, conta, data_entrega]
        with open('pessoas_cadastradas.json', 'w') as f:
            f.write(json.dumps(pessoas_cadastradas))
        return pessoas_cadastradas


def devolver_carro(carros, pessoas_cadastradas):
    cpf_pessoa = input('Digite seu CPF: ')
    dia_entregue = input('Dia de entrega (dd/mm/YYYY): ')

    print(type(dia_entregue))
    print(type(pessoas_cadastradas[cpf_pessoa][7]))

    if dia_entregue != pessoas_cadastradas[cpf_pessoa][7]:
        dia_entregue = datetime.datetime.strptime(dia_entregue, '%d/%m/%Y')
        data_entregue = datetime.datetime.strptime(pessoas_cadastradas[cpf_pessoa][7], '%d/%m/%Y')

        atraso = dia_entregue - data_entregue
        valor = atraso.days * 100
        print('Pague uma multa: ', valor)

    if cpf_pessoa in pessoas_cadastradas.keys():
        carros[pessoas_cadastradas[cpf_pessoa][4]][5] += 1
        del pessoas_cadastradas[cpf_pessoa]

        escrever_json_carros(carros)
        escrever_json_pessoas_cadastradas(pessoas_cadastradas)

        print('Devolvido com sucesso')


def menu():
    carros = carregar_arquivo_carros()
    while True:
        exibir_tabela_carros(carros)
        op = input(
            '\n(1) Reservar veiculo\n'
            '(2) Devolver veiculo\n'
            '(3) Finalizar\n')

        if (op == '1'):
            pessoas_cadastradas = reservar_carro(carros)
        elif (op == '2'):
            pessoas_cadastradas = carregar_arquivo_pessoas_cadastradas()
            devolver_carro(carros, pessoas_cadastradas)
        elif (op == '3'):
            break


if __name__ == '__main__':
    menu()
