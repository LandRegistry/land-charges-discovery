import pytest
#from unittest \
import mock
import requests
from service.server import app
from service import server
from service.model import LandCharge


class FakeQuery:
    def all(self):
        return [
            LandCharge(nature='PAB', date='30/01/1908', name='ARTHUR MURRAY', address='FLAT 2, HIGH ST. KENSINGTON')
        ]
fakeResults = FakeQuery()


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
        print(response.data)
        assert(1 == 1)
