import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from app import create_app


@pytest.fixture
def api():
    app = create_app('testing')
    api = app.test_client()

    return api


def test_ping(api):
    resp = api.post('/api/ping')
    assert b'pong' in resp.data


def test_search(api):
    resp = api.post('/api/AAPL')
    assert b'buy', b'sell' in resp.data


def test_wrongsearch(api):
    resp = api.post('/api/NONEXISTINGCODE')
    assert b"Couldn't find any stock data. Try Again!" in resp.data
