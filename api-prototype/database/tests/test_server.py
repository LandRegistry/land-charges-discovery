import pytest
#from unittest \
import mock
import requests
from service.server import app
from service import server
from service.model import LandCharge
import json


class FakeQuery:
    def __init__(self, data):
        self.data = data

    def filter_by(self, **kwargs):
        new_item = FakeQuery([
            LandCharge(nature='PAB', date='30/01/1908', name='ARTHUR MURRAY', address='FLAT 2, HIGH ST. KENSINGTON'),
            LandCharge(nature='WOB', date='30/01/1908', name='ARTHUR MURRAY', address='FLAT 2, HIGH ST. KENSINGTON')
        ])
        return new_item

    def all(self):
        return self.data


fakeResults = FakeQuery([
    LandCharge(nature='PAB', date='30/01/1908', name='ARTHUR MURRAY', address='FLAT 2, HIGH ST. KENSINGTON'),
    LandCharge(nature='WOB', date='30/01/1908', name='ARTHUR MURRAY', address='FLAT 2, HIGH ST. KENSINGTON'),
    LandCharge(nature='PAB', date='30/01/1908', name='BOB HOWARD', address='FLAT 79, HIGH ST. KENSINGTON')
])


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

    @mock.patch('service.server.session.query', return_value=fakeResults)
    def test_search_all(self, mock_query):
        response = self.app.get('/search_all')
        json_data = json.loads(response.data.decode())
        assert(len(json_data) == 3)
        assert(json_data[2]['name'] == "BOB HOWARD")

    @mock.patch('service.server.session.query', return_value=fakeResults)
    def test_search(self, mock_query):
        response = self.app.post('/search_name', data='{"name": "ARTHUR MURRAY"}',
                                 headers={'Content-Type': 'application/json'})
        json_data = json.loads(response.data.decode())
        assert(len(json_data) == 2)
        assert(json_data[1]['name'] == "ARTHUR MURRAY")

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

