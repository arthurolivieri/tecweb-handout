from utils import adiciona_anotacao, build_response, deleta_anotacao
from utils import load_data, load_template
from urllib.parse import unquote_plus

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST / HTTP'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            # AQUI É COM VOCÊ
            frase = unquote_plus(chave_valor)
            frase = frase.split('=')
            params[frase[0]] = frase[1]
        adiciona_anotacao('banco', params)
        return build_response(code=303, reason='See Other', headers='Location: /')

    elif request.startswith('POST /delete'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n')
        id = partes[-1].split('=')[-1]
        deleta_anotacao('banco', id)
        return build_response(code=303, reason='See Other', headers='Location: /')

    elif request.startswith('GET /update'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        parte = request.split('\n')[0]
        parte = parte.split('?')[1]
        parte = parte.split(' ')[0]

        params = {}
        for chave_valor in parte.split('&'):
            # AQUI É COM VOCÊ
            frase = unquote_plus(chave_valor)
            frase = frase.split('=')
            params[frase[0]] = frase[1]

        corpo = load_template('edit.html')
        title = params['title']
        details = params['details']
        corpo = corpo.format(title=title, details=details)

        return build_response(body=corpo)
    
    
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=note.id, title=note.title, details=note.content)
        for note in load_data('banco')
    ]
    notes = '\n'.join(notes_li)

    corpo = load_template('index.html').format(notes=notes)
    
    return build_response(body=corpo)