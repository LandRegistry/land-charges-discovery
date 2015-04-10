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