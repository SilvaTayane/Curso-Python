from datetime import datetime
import os


class Identificacao:
    def __init__(self, name, data_nascimento_str, titulo,sx,naturalidade,nome_mae):
        self.name = name
        self.data_nascimento_str = data_nascimento_str
        self.titulo = titulo
        self.sx = sx
        self.naturalidade = naturalidade
        self.nome_mae = nome_mae




class Endereco:
   def __init__(self,cep, municipio, uf, logradouro, endereco, numero_residencia, ddd, numero_telefone, numero_celular, complemento, bairro ):
       self.cep = cep
       self.municipio = municipio
       self.uf = uf
       self.logradouro = logradouro
       self.endereco = endereco
       self.numero_residencia = numero_residencia
       self.ddd = ddd
       self.numero_telefone = numero_telefone
       self.numero_celular = numero_celular
       self.complemento = complemento
       self.bairro = bairro


def identificacao():
    while True:
        name = input("Nome: ")
        if len(name) > 3:
            print("Nome válido!\n")
            break
        else:
            print("Nome deve ter mais de 3 caracteres.\n")


    while True:
        data_nascimento_str = input("Digite a data de nascimento dd/mm/aaaa: ")
        try:
            data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
            print("Data de nascimento válida:", data_nascimento)
            break
        except ValueError:
            print("Data de nascimento inválida. Certifique-se de usar o formato dd/mm/aaaa.")
   
    while True:
        titulo = input("Titulo de eleitor: ")
        if len(titulo) == 12:
            print("Titulo de eleitor válido!\n")
            break
        else:
            print("Titulo de eleitor invalido.\n")
   
    while True:
        sx = input("Digite seu Sexo (f/m): ")
        if sx == 'f' or sx == 'm':
            print("Sexo válido!\n")
            break
        else:
            print("Sexo deve ser 'f' ou 'm'.\n")
   
    while True:
        naturalidade = input("Naturalidade: ")
        if len(naturalidade)>2:
            print("Naturalidade válido!\n")
            break
        else:
            print("Naturalidade invalida.\n")
           
    while True:
        nome_mae = input("Nome da mãe: ")
        if len(nome_mae)>3:
            print("nome da mãe válido!\n")
            break
        else:
            print("nome da mae invalida.\n")
   
    ident = Identificacao(name, data_nascimento_str, titulo,sx,naturalidade,nome_mae)
    os.system("cls")


    print("\n\nDados de Identificação:\n")
    print("Nome: ", ident.name,"\n")
    print("Data de Nacimento: ", ident.data_nascimento_str,"\n")
    print("Titulo: ", ident.titulo,"\n")
    print("Sexo: ", ident.sx,"\n")
    print("Naturalidade: ", ident.naturalidade,"\n")
    print("Nome da Mãe: ", ident.nome_mae,"\n")


    op = input("\nDeseja confirmar seus dados? [S][N]: ")


    if(op == "N"):
        identificacao()
#########################################################################


def endereco():
    while True:
        cep = input("CEP: ")
        if len(cep) == 8:
            print("CEP valido!\n")
            break
        else:
            print("CEP invalido.\n")


    while True:
        municipio = input("municipio: ")
        if len(municipio) > 2:
            print("municipio valido!\n")
            break
        else:
            print("municipio invalido.\n")
   
    while True:
        uf = input("UF: ")
        if len(uf) == 2:
            print("UF válido!\n")
            break
        else:
            print("UF invalido.\n")
   
    while True:
        logradouro = input("logradouro: ")
        if len(logradouro) > 2:
            print("logradouro válido!\n")
            break
        else:
            print("logradouro invalido.\n")
   
    while True:
        endereco = input("Endereco: ")
        if len(endereco)>5:
            print("Endereco válido!\n")
            break
        else:
            print("Endereco invalida.\n")
           
    while True:
        numero_residencia = input("Numero da residencia: ")
        if len(numero_residencia)>0:
            print("Numero de residencia Valido!\n")
            break
        else:
            print("Numero de residencia invalido.\n")
           
    while True:
        ddd = input("DDD: ")
        if len(ddd)==3:
            print("DDD Valido!\n")
            break
        else:
            print("DDD invalido.\n")


    while True:
        numero_telefone =input("Numero Telefone: ")
        if len(numero_telefone)==9:
            print("Numero de telefone Valido!\n")
            break
        else:
            print("Numero de telefone invalido.\n")


    while True:
        numero_celular = input("Numero celular: ")
        if len(numero_celular)==9:
            print("Numero de celular Valido!\n")
            break
        else:
            print("Numero de celular invalido.\n")


    while True:
        complemento = input("complemento: ")
        if len(complemento)>3:
            print("complemento válido!\n")
            break
        else:
            print("complemento invalida.\n")


    while True:
        bairro = input("bairro: ")
        if len(bairro)>3:
            print("bairro válido!\n")
            break
        else:
            print("bairro invalida.\n")


    ende = Endereco(cep, municipio, uf, logradouro, endereco, numero_residencia, ddd, numero_telefone, numero_celular, complemento, bairro)
    os.system("cls")




    print("\n\nDados de endereço:")
    print("Cep: ", ende.cep)
    print("Municipio: ", ende.municipio)
    print("Uf: ", ende.uf)
    print("Logradouro: ", ende.logradouro)
    print("EndereÇo: ", ende.endereco)
    print("Numero de residència: ", ende.numero_residencia)
    print("ddd: ", ende.ddd)
    print("Numero de telefone: ", ende.numero_telefone)
    print("Numero de celular: ", ende.numero_celular)
    print("Complemento: ", ende.complemento)
    print("Bairro: ", ende.bairro)




    op = input("\nDeseja confirmar seus dados? [S][N]")

    if(op == "N" ):
        endereco()




print("--------IDENTIFICAÇÃO--------\n")
identificacao()


print("\n--------ENDEREÇO--------\n")
endereco()




print("\n\nDados Cadastrados com sucesso!!")
