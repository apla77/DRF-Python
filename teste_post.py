import requests

headers = {'Authorization': 'Token 9d815592cb1d32891fe75d05d7b8f0e841280684'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo = {
    "titulo": "Algoritmos e progamação em C++",
    "url": "http://www.apla77.com.br/programacaoC++"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo)

assert resultado.status_code == 201

assert resultado.json()['titulo'] == novo['titulo']







