import os
import json
from database import Database, Note

def extract_route(req):
    req = req.split(" ")
    if req[1].startswith("/"):
        req = req[1].replace("/", "", 1)
        return req
    
def read_file(path):
    with open(path, 'rb') as file:
        content = file.read()
    return content

def load_data(db_name):
    db = Database(db_name)

    db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
    db.add(Note(title=None, content='Lembrar de tomar água'))

    notes = db.get_all()

    return notes

def load_template(nome):
    path = "templates/" + nome
    with open(path, 'r') as file:
        content = file.read()
    return content

def adiciona_anotacao(db_name, nota):
    db = Database(db_name)
    titulo = nota['titulo']
    conteudo = nota['detalhes']
    db.add(Note(title=titulo, content=conteudo))

    
def deleta_anotacao(db_name, id):
    db = Database(db_name)
    db.delete(id)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers != '':
        headers = '\n' + headers
    response = 'HTTP/1.1 ' + str(code) + ' ' + reason + headers + '\n\n' + body
    return response.encode()