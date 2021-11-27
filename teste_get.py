import requests

headers = {'Authorization': 'Token 9d815592cb1d32891fe75d05d7b8f0e841280684'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

assert resultado.status_code == 200

assert resultado.json()['count'] == 4