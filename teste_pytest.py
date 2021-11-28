import requests


class TestCursos:
    headers = {'Authorization': 'Token 9d815592cb1d32891fe75d05d7b8f0e841280684'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}6/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso PyTest Django",
            "url": "http://www.apla77.com.br/pytest/novocurso"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizar = {
            "titulo": "Curso PyTest Django Rest",
            "url": "http://www.apla77.com.br/pyTest"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}6/', headers=self.headers, data=atualizar)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizar['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}6/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0