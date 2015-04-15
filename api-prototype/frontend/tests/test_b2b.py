import pytest
from unittest import mock
from client.api import app
import requests


class FakeResponse(requests.Response):
    def __init__(self, content='', status_code=200):
        super(FakeResponse, self).__init__()
        self._content = content
        self._content_consumed = True
        self.status_code = status_code

search_string = '[{"nature": "PAB", "id": 202, "address": "12 HIGH STREET", "date": "02/04/2015", "name": "JACK BLOGGS"}]'


fake_error = FakeResponse('Wibble', 500)
fake_success = FakeResponse('Wibble', 200)
fake_search = FakeResponse(str.encode(search_string), 200)


class TestB2B:
    def setup_method(self, method):
        self.app = app.test_client()

    @mock.patch('requests.get', return_value=fake_success)
    def test_remote_healthcheck(self, mock_get):
        response = self.app.get("/remote")
        assert response.status_code == 200

    @mock.patch('requests.post', return_value=fake_search)
    def test_search(self, mock_post):
        response = self.app.post("/search",
                                 data={'forename': 'Jack', 'surname': 'Bloggs', 'alternative': ''})
        assert('JACK BLOGGS' in response.data.decode())
        assert('12 HIGH STREET' in response.data.decode())

    fake_search = FakeResponse(str.encode(search_string), 201)
    @mock.patch('requests.post', return_value=fake_search)
    def test_b2bregister(self, mock_post):
        response = self.app.post('/b2b_register', data={'nature': 'WOB', 'name': 'John Forename', 'address': '12 high street'})
        assert response.status_code == 200

    @mock.patch('requests.post', return_value=fake_search)
    def test_b2bpostman(self, mock_post):
        headers = {'Content-Type': 'application/json'}
        response = self.app.post('/b2b_postman', data='{"nature": "WOB", "name": "John Forename", "address": "12 high street"}', headers=headers)
        assert response.status_code == 201

