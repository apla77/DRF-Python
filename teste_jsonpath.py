import requests, jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

primeiro = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')

print(primeiro)