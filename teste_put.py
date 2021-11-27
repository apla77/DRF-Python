import requests

headers = {'Authorization': 'Token 9d815592cb1d32891fe75d05d7b8f0e841280684'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

update = {
    "titulo": "Algoritmos e progamação em C/C++",
    "url": "http://www.apla77.com.br/programacao-c++"
}

resultado = requests.put(url=f'{url_base_cursos}7/', headers=headers, data=update)

assert resultado.status_code == 200

assert resultado.json()['titulo'] == update['titulo']







