import os
import json

def extract_route(req):
    req = req.split(" ")
    if req[1].startswith("/"):
        req = req[1].replace("/", "", 1)
        return req
    
def read_file(path):
    with open(path, 'rb') as file:
        content = file.read()
    return content

def load_data(arq):
    path = "data/" + arq
    with open(path, 'r') as file:
        dic = json.load(file)
    return dic

def load_template(nome):
    path = "templates/" + nome
    with open(path, 'r') as file:
        content = file.read()
    return content

def adiciona_anotacao(arq, nota):
    data = load_data(arq) #dicionario
    data.append(nota)
    path = 'data/' + arq
    with open(path, 'w') as file:
        json.dump(data, file)
    return data
    

def build_response(body='', code=200, reason='OK', headers=''):
    response = 'HTTP/1.1 ' + str(code) + " " + reason + "\n" + headers + "\n" + body
    return response.encode()