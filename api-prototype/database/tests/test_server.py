import pytest
import mock
from service.server import app


class TestServer:
    def setup_method(self, method):
        self.app = app.test_client()

    def test_reality(self):
        assert 1 + 2 == 3

    def test_healthcheck(self):
        response = self.app.get("/")
        assert response.status_code == 200

    def test_notfound(self):
        response = self.app.get("/doesnt_exist")
        assert response.status_code == 404

    def test_searchall(self):
        response = self.app.get("/search_all")
        assert response.status_code == 200

    def test_searchname(self):
        headers = {'Content-Type': 'application/json'}
        name = '{"name": "ROBERT TREBOR"}'
        response = self.app.post('/search_name', data=name, headers=headers)
        assert response.status_code == 200
        assert 'FLAT' in response.data.decode()
        print(response.data.decode())

    def test_searchloop(self):
        data = [
            '{"name": "ROBERT TREBOR"}',
            '{"name": "Jack Bloggs"}',
            '{"name": "pat smith"}'
        ]
        headers = {'Content-Type': 'application/json'}
        num = 0
        for i in data:
            name = data[num]
            response = self.app.post('/search_name', data=name, headers=headers)
            assert response.status_code == 200
            print(response.data.decode())
            num = num + 1

    def test_register(self):
        headers = {'Content-Type': 'application/json'}
        data = '{"nature": "WOB", "name": "I.P. Freely", "address": "54 high street, plymouth"}'
        response = self.app.post('/register', data=data, headers=headers)
        assert response.status_code == 201
        print(response.data.decode())






