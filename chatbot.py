import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, Vale muito a pena aprender Python, pois é uma das linguagens que mais cresce atualmente{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, A média salarial de um programador Python é em torno de R$ 150.000,00 por ano.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, Para se tornar um programador, você precisa estudar alguns temas que são relevantes para a profissão.\nÉ preciso se dedicar e estar sempre em busca de novos conhecimentos.\nTe indico um curso básico de Python: Pesquise no google Cursoemvideo.{os.linesep}')
    else:
        print('Digite apenas as opções 1, 2 e 3')

def start():
    # Apresentar o chatbot
    print('Olá. Bem vindo ao ChatBot')
    
    # Pedir o nome
    nome = input('Digite seu nome: ')
    
    while True:
        
        # Oferecer um menu de opções
        resposta = input(
            f'O que gostaria de saber hoje? {os.linesep}|1| Vale a pena aprender Python? {os.linesep} |2| Qual a média salarial de um profissional que trabalha com python? {os.linesep}|3| E como faço pra me tornar um programador?{os.linesep}')
        
        # Processar a resposta enviada
        processar_resposta(resposta, nome)

if __name__=='__main__':
    start()
