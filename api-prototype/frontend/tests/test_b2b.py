import pytest
import mock
from service.server import app


class TestB2B:
    def setup_method(self, method):
        self.app = app.test_client()

