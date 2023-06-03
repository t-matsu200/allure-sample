# -*- coding: utf-8 -*-
import pytest
from app import create_app
from fastapi.testclient import TestClient


@pytest.fixture(scope='module')
def fixture_app_test():
    client = TestClient(create_app(is_test=True))
    return client
