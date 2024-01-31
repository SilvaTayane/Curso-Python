from django.shortcuts import render

LOREM_IPSUM = "Se eu preferiria ser temido ou amado? Fácil. Ambos. Eu quero que as pessoas tenham medo do quanto elas me amam.Às vezes, eu começo uma frase e eu nem sei aonde ela vai parar. Eu só espero encontrar o sentido ao longo do caminho."
def index_page(request):
    posts = [
        {'autor' : 'Michael Scott ',
        'data' : '31/01/24',
        'conteudo' : LOREM_IPSUM},
        {'autor' : 'Michael Scott ',
        'data' : '31/01/24',
        'conteudo' : LOREM_IPSUM},
        {'autor' : 'Michael Scott ',
        'data' : '31/01/24',
        'conteudo' : LOREM_IPSUM},
        
    ]
    return render(request, 'index.html', {'posts': posts})
