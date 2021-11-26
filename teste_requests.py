import requests


# GET Avaliações

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

#print(avaliacoes.status_code)

#print(avaliacoes.json())

#print(avaliacoes.json()['results'])

#print(avaliacoes.json()['results'][0])

#print(avaliacoes.json()['results'][0]['nome'])

#avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/5/')
#print(avaliacao.json())

headers = {'Authorization': 'Token 9d815592cb1d32891fe75d05d7b8f0e841280684'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())